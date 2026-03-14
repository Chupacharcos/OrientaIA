"""
Base de datos de carreras con datos reales del mercado español (2025)
"""

CAREERS = {
    "ingenieria_software": {
        "name": "Ingeniería de Software / Desarrollo",
        "description": "Diseño y desarrollo de aplicaciones, sistemas y software.",
        "interests": ["tecnología", "lógica", "resolver problemas", "videojuegos", "matemáticas"],
        "values": ["autonomía", "creatividad", "impacto", "innovación"],
        "skills": ["análisis", "concentración", "aprendizaje continuo"],
        "salary_range": "28.000€ – 80.000€/año",
        "demand": "Muy alta",
        "paths": ["DAM/DAW (FP)", "Ingeniería Informática", "Bootcamp + portfolio"],
        "work_style": "híbrido/remoto",
    },
    "medicina": {
        "name": "Medicina",
        "description": "Diagnóstico, tratamiento y prevención de enfermedades.",
        "interests": ["biología", "ayudar a personas", "ciencias", "cuerpo humano"],
        "values": ["vocación", "responsabilidad", "impacto social"],
        "skills": ["empatía", "memoria", "resistencia"],
        "salary_range": "35.000€ – 120.000€/año",
        "demand": "Alta",
        "paths": ["Selectividad + Grado en Medicina (6 años) + MIR"],
        "work_style": "presencial",
    },
    "diseno_grafico": {
        "name": "Diseño Gráfico / UX-UI",
        "description": "Creación visual de marcas, interfaces y experiencias digitales.",
        "interests": ["arte", "estética", "tecnología", "comunicación", "dibujo"],
        "values": ["creatividad", "expresión", "autonomía"],
        "skills": ["atención al detalle", "comunicación visual", "empatía"],
        "salary_range": "18.000€ – 50.000€/año",
        "demand": "Alta (UX especialmente)",
        "paths": ["Grado en Diseño", "FP Diseño Gráfico", "Autodidacta + portfolio"],
        "work_style": "híbrido",
    },
    "psicologia": {
        "name": "Psicología",
        "description": "Estudio del comportamiento humano y apoyo a la salud mental.",
        "interests": ["personas", "comportamiento", "escuchar", "ayudar"],
        "values": ["empatía", "impacto social", "comprensión"],
        "skills": ["escucha activa", "análisis", "paciencia"],
        "salary_range": "20.000€ – 45.000€/año",
        "demand": "Media-alta (en auge)",
        "paths": ["Grado en Psicología (4 años) + Máster habilitante"],
        "work_style": "presencial/híbrido",
    },
    "marketing_digital": {
        "name": "Marketing Digital",
        "description": "Estrategias de comunicación y ventas en entornos digitales.",
        "interests": ["redes sociales", "comunicación", "tendencias", "negocios"],
        "values": ["creatividad", "resultados", "dinamismo"],
        "skills": ["comunicación", "análisis de datos", "creatividad"],
        "salary_range": "20.000€ – 55.000€/año",
        "demand": "Alta",
        "paths": ["Grado en Marketing/Publicidad", "Cursos especializados + experiencia"],
        "work_style": "híbrido/remoto",
    },
    "educacion": {
        "name": "Educación / Docencia",
        "description": "Enseñanza y formación en distintas etapas educativas.",
        "interests": ["niños", "enseñar", "comunicación", "paciencia"],
        "values": ["vocación", "impacto social", "estabilidad"],
        "skills": ["paciencia", "comunicación", "organización"],
        "salary_range": "24.000€ – 45.000€/año (funcionario)",
        "demand": "Estable",
        "paths": ["Magisterio (Infantil/Primaria)", "Grado + Máster MAES (Secundaria)"],
        "work_style": "presencial",
    },
    "derecho": {
        "name": "Derecho / Abogacía",
        "description": "Asesoramiento legal, defensa y representación jurídica.",
        "interests": ["debate", "justicia", "argumentación", "sociedad"],
        "values": ["justicia", "rigor", "impacto"],
        "skills": ["argumentación", "lectura", "memoria", "negociación"],
        "salary_range": "22.000€ – 80.000€+ /año",
        "demand": "Media (competitivo)",
        "paths": ["Grado en Derecho (4 años) + Máster de Acceso"],
        "work_style": "presencial",
    },
    "videojuegos": {
        "name": "Desarrollo de Videojuegos",
        "description": "Diseño, programación y producción de videojuegos.",
        "interests": ["videojuegos", "programación", "arte", "narrativa", "tecnología"],
        "values": ["creatividad", "pasión", "innovación"],
        "skills": ["programación", "diseño", "trabajo en equipo"],
        "salary_range": "22.000€ – 60.000€/año",
        "demand": "Media (sector en crecimiento)",
        "paths": ["FP Desarrollo de Videojuegos", "Grado en Ingeniería + especialización"],
        "work_style": "presencial/híbrido",
    },
}


def get_all_careers():
    return CAREERS


def get_career(career_id: str):
    return CAREERS.get(career_id)


def match_careers(profile: dict, top_n: int = 3) -> list:
    """Score simple basado en coincidencia de intereses y valores."""
    scores = []
    interests = [i.lower() for i in profile.get("interests", [])]
    values = [v.lower() for v in profile.get("values", [])]
    skills = [s.lower() for s in profile.get("skills", [])]

    for career_id, career in CAREERS.items():
        score = 0
        for interest in interests:
            for ci in career["interests"]:
                if interest in ci.lower() or ci.lower() in interest:
                    score += 3
        for value in values:
            for cv in career["values"]:
                if value in cv.lower() or cv.lower() in value:
                    score += 2
        for skill in skills:
            for cs in career["skills"]:
                if skill in cs.lower() or cs.lower() in skill:
                    score += 1
        scores.append((career_id, score, career))

    scores.sort(key=lambda x: x[1], reverse=True)
    return [
        {"id": cid, "score": s, **c}
        for cid, s, c in scores[:top_n]
    ]
