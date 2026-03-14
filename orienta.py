"""
OrientaIA — Motor de orientación vocacional con LangChain + Groq/LLaMA
Flujo: exploración conversacional → extracción JSON de perfil → matching carreras → simulador de día
"""
import os
import json
import re
from langchain_groq import ChatGroq
from langchain_classic.memory import ConversationSummaryBufferMemory
from langchain_classic.chains import ConversationChain
from langchain_core.prompts import PromptTemplate
from careers_data import match_careers

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ── Prompts ───────────────────────────────────────────────────────────────────

EXPLORATION_PROMPT = """Eres OrientaIA, un orientador vocacional conversacional para adolescentes de 14-18 años. Tu misión es ayudarles a descubrir qué camino profesional encaja con ellos a través de una charla natural y cercana.

FASE ACTUAL: {phase}

Reglas:
- Habla como un amigo mayor, no como un psicólogo o formulario.
- Haz UNA sola pregunta por turno (máximo dos).
- Muestra genuino interés. Conecta lo que dice con preguntas más profundas.
- Nunca menciones que estás "extrayendo datos" o "analizando un perfil".
- Si llevas más de 8 turnos explorando, empieza a guiar hacia el cierre.

Preguntas guía según fase:
- exploración: qué les gusta, qué odian, qué harían si no tuvieran que trabajar, qué admiran de otras personas
- valores: qué es más importante: dinero, impacto, creatividad, autonomía, estabilidad
- habilidades: qué se les da bien (aunque no les guste), qué dicen los demás de ellos

Conversación anterior:
{history}

Adolescente: {input}
OrientaIA:"""

EXTRACTION_PROMPT = """Analiza esta conversación de orientación vocacional y extrae un perfil JSON estructurado.

Conversación:
{conversation}

Devuelve ÚNICAMENTE un JSON válido con esta estructura (sin markdown, sin explicaciones):
{{
  "interests": ["lista de intereses detectados"],
  "values": ["lista de valores detectados"],
  "skills": ["lista de habilidades detectadas"],
  "avoid": ["cosas que quiere evitar en su trabajo"],
  "work_style": "presencial/remoto/híbrido/no importa",
  "confidence": 0.0
}}"""

SIMULATOR_PROMPT = """Eres un narrador que describe un día laboral real en segunda persona para un adolescente que está explorando la carrera de {career_name}.

Perfil del adolescente: intereses en {interests}, valores de {values}.

Genera una narración inmersiva de UN día laboral típico. Usa segunda persona ("Son las 9:00, entras a...").
Incluye:
- Mañana: inicio del día y primera tarea importante
- Mediodía: interacción con equipo o cliente
- Tarde: reto del día y cómo lo resuelves
Sé específico y realista. Máximo 250 palabras."""

# ── Sesiones ──────────────────────────────────────────────────────────────────

_sessions: dict[str, dict] = {}


def get_or_create_session(session_id: str) -> dict:
    if session_id not in _sessions:
        llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model="llama-3.1-8b-instant",
            temperature=0.8,
            max_tokens=600,
        )
        memory = ConversationSummaryBufferMemory(
            llm=llm,
            max_token_limit=1200,
            return_messages=False,
        )
        prompt = PromptTemplate(
            input_variables=["history", "input"],
            template=EXPLORATION_PROMPT.format(
                phase="exploración",
                history="{history}",
                input="{input}",
            ),
        )
        chain = ConversationChain(llm=llm, memory=memory, prompt=prompt, verbose=False)
        _sessions[session_id] = {
            "chain": chain,
            "memory": memory,
            "llm": llm,
            "turn_count": 0,
            "profile": None,
            "careers": None,
            "phase": "exploration",  # exploration → profile_ready → done
            "conversation_log": [],
        }
    return _sessions[session_id]


def chat(session_id: str, message: str) -> dict:
    session = get_or_create_session(session_id)
    session["turn_count"] += 1
    session["conversation_log"].append(f"Adolescente: {message}")

    response = session["chain"].invoke({"input": message})
    reply = response["response"] if isinstance(response, dict) else str(response)
    session["conversation_log"].append(f"OrientaIA: {reply}")

    # Tras 6 turnos extraemos el perfil automáticamente
    ready_for_profile = session["turn_count"] >= 6 and session["phase"] == "exploration"

    return {
        "reply": reply,
        "turn": session["turn_count"],
        "session_id": session_id,
        "phase": session["phase"],
        "ready_for_profile": ready_for_profile,
    }


def extract_profile(session_id: str) -> dict:
    session = get_or_create_session(session_id)
    if session["profile"]:
        return session["profile"]

    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model="llama-3.1-8b-instant",
        temperature=0.2,
        max_tokens=400,
    )
    conversation_text = "\n".join(session["conversation_log"])
    prompt = EXTRACTION_PROMPT.format(conversation=conversation_text)

    raw = llm.invoke(prompt)
    content = raw.content if hasattr(raw, "content") else str(raw)

    # Extraer JSON del response
    match = re.search(r'\{.*\}', content, re.DOTALL)
    if match:
        try:
            profile = json.loads(match.group())
        except json.JSONDecodeError:
            profile = {"interests": [], "values": [], "skills": [], "avoid": [], "work_style": "no importa", "confidence": 0.5}
    else:
        profile = {"interests": [], "values": [], "skills": [], "avoid": [], "work_style": "no importa", "confidence": 0.5}

    session["profile"] = profile
    session["phase"] = "profile_ready"

    # Matching de carreras
    careers = match_careers(profile, top_n=3)
    session["careers"] = careers

    return {"profile": profile, "careers": careers}


def simulate_day(session_id: str, career_id: str) -> dict:
    session = get_or_create_session(session_id)
    profile = session.get("profile", {})
    careers = session.get("careers", [])

    career = next((c for c in careers if c["id"] == career_id), None)
    if not career:
        from careers_data import get_career
        career = get_career(career_id) or {"name": career_id}

    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model="llama-3.1-8b-instant",
        temperature=0.9,
        max_tokens=500,
    )
    prompt = SIMULATOR_PROMPT.format(
        career_name=career.get("name", career_id),
        interests=", ".join(profile.get("interests", ["varios temas"])),
        values=", ".join(profile.get("values", ["autonomía"])),
    )
    raw = llm.invoke(prompt)
    narrative = raw.content if hasattr(raw, "content") else str(raw)

    return {
        "career_id": career_id,
        "career_name": career.get("name", career_id),
        "narrative": narrative,
    }
