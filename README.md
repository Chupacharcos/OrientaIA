# OrientaIA — Descubre tu camino profesional hablando

Plataforma de orientación vocacional para adolescentes de 14 a 18 años. Una IA mantiene una conversación natural mientras extrae silenciosamente el perfil de intereses, valores y habilidades del usuario. Al final genera un mapa de carreras personalizado y simulaciones de día laboral.

## Demo en vivo

[adrianmoreno-dev.com/demo/orienta-ia](https://adrianmoreno-dev.com/demo/orienta-ia)

## Flujo de usuario

```
1. Conversación natural ("¿qué harías si no tuvieras que trabajar?")
        ↓
2. Extraction chain extrae silenciosamente:
   { intereses, valores, habilidades, preferencias_entorno }
        ↓
3. Ranking de carreras con puntuación de afinidad (top 3)
        ↓
4. Simulador de día laboral narrativo en 2ª persona por carrera
        ↓
5. Informe PDF descargable (perfil + carreras + simulaciones)
```

## Arquitectura técnica

```
FastAPI (puerto 8097)
├── orienta.py           Motor principal
│   ├── Exploration chain  → conversación informal guiada
│   ├── Extraction chain   → JSON {intereses, valores, habilidades}
│   └── Simulator chain    → narración día laboral en 2ª persona
├── careers_data.py      8 carreras con datos reales de mercado laboral ES
│   └── match_careers()  Scoring por overlap intereses/valores/habilidades
├── router.py            Endpoints REST
└── api.py               FastAPI app + CORS
```

### LangChain chains encadenadas

| Chain | Entrada | Salida |
|-------|---------|--------|
| **Exploration** | Turno de conversación | Respuesta empática + tracking |
| **Extraction** | Historial (6-10 turnos) | JSON estructurado del perfil |
| **Simulator** | Perfil + carrera elegida | Narrativa día a día en 2ª persona |

### Carreras disponibles
`ingenieria_software` · `medicina` · `diseño_grafico` · `psicologia` · `marketing_digital` · `educacion` · `derecho` · `videojuegos`

Cada carrera incluye: demanda laboral real, salario medio ES, habilidades clave, valores alineados.

## Stack técnico

| Capa | Tecnología |
|------|-----------|
| LLM | Groq API — LLaMA 3.1 (respuestas narrativas largas sin latencia) |
| Orquestación | LangChain + chains encadenadas |
| Datos | RAG de mercado laboral (demanda, salarios, salidas por carrera) |
| API | FastAPI + Uvicorn |
| Frontend | Laravel + Blade |
| PDF | WeasyPrint |

## Endpoints

```
POST /orientaia/chat         Turno de conversación exploratoria
POST /orientaia/profile      Extraer perfil JSON del historial
POST /orientaia/simulate     Simular día laboral en una carrera
GET  /orientaia/careers      Listado de carreras con datos de mercado
POST /orientaia/session/new  Nueva sesión
GET  /orientaia/health
```

## Instalación

```bash
# Requiere el venv compartido en /var/www/chatbot/venv
pip install fastapi uvicorn langchain-classic langchain-core langchain-groq python-dotenv

# Variables de entorno
cp .env.example .env
# Añadir: GROQ_API_KEY=gsk_...

# Desarrollo
uvicorn api:app --host 127.0.0.1 --port 8097 --reload

# Producción (systemd)
sudo systemctl start orientaia
```

## Servicio systemd

```ini
[Unit]
Description=OrientaIA FastAPI — puerto 8097
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/var/www/orientaia
ExecStart=/var/www/chatbot/venv/bin/uvicorn api:app --host 127.0.0.1 --port 8097
Restart=on-failure
```

## Lo más diferencial

El **simulador de día laboral** en segunda persona es la pieza que hace única a OrientaIA. Ejemplo de salida para *ingeniería de software*:

> "Son las 9:30. Abres tu IDE y revisas el PR que dejaste a medias ayer. Tu compañera Ana te ha dejado dos comentarios en el código — uno señala un edge case que no habías contemplado. Lo piensas durante 10 minutos mientras te tomas el café..."

El LLM integra el perfil del usuario (sus valores, ritmo preferido, entorno) en la narrativa, haciendo que cada simulación sea única.
