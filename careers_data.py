"""
Base de datos de carreras con datos reales del mercado español (2025)
40+ carreras con perfiles RIASEC para orientación vocacional
"""

CAREERS = {
    # ── TECNOLOGÍA ────────────────────────────────────────────────────────────
    "ingenieria_software": {
        "name": "Ingeniería de Software / Desarrollo",
        "description": "Diseño y desarrollo de aplicaciones, sistemas y software. Trabajo con código, algoritmos y resolución de problemas técnicos complejos.",
        "interests": ["tecnología", "lógica", "resolver problemas", "videojuegos", "matemáticas", "programación"],
        "values": ["autonomía", "creatividad", "impacto", "innovación"],
        "skills": ["análisis", "concentración", "aprendizaje continuo", "lógica"],
        "avoid_tags": ["sangre", "deportes", "naturaleza", "arte físico"],
        "salary_range": "28.000€ – 80.000€/año",
        "demand": "Muy alta",
        "paths": ["DAM/DAW (FP)", "Ingeniería Informática", "Bootcamp + portfolio"],
        "work_style": "híbrido/remoto",
        "riasec": {"R": 30, "I": 80, "A": 40, "S": 20, "E": 40, "C": 60},
    },
    "data_science": {
        "name": "Ciencia de Datos / Data Scientist",
        "description": "Análisis de grandes conjuntos de datos, machine learning y extracción de insights para tomar decisiones de negocio basadas en evidencia.",
        "interests": ["estadística", "matemáticas", "programación", "patrones", "negocios", "tecnología"],
        "values": ["innovación", "impacto", "conocimiento", "autonomía"],
        "skills": ["análisis", "pensamiento crítico", "programación", "visualización"],
        "avoid_tags": ["trabajo manual", "atención al público", "rutina sin análisis"],
        "salary_range": "30.000€ – 90.000€/año",
        "demand": "Muy alta",
        "paths": ["Estadística/Matemáticas + Máster DS", "Ingeniería Informática", "Bootcamp ML/AI"],
        "work_style": "híbrido/remoto",
        "riasec": {"R": 20, "I": 90, "A": 30, "S": 20, "E": 40, "C": 70},
    },
    "ciberseguridad": {
        "name": "Ciberseguridad",
        "description": "Protección de sistemas y redes contra amenazas digitales. Análisis de vulnerabilidades, ethical hacking y defensa de infraestructuras críticas.",
        "interests": ["tecnología", "hacking ético", "misterio", "resolver puzzles", "seguridad", "redes"],
        "values": ["reto", "proteger", "innovación", "responsabilidad"],
        "skills": ["análisis", "concentración", "pensamiento lateral", "aprendizaje continuo"],
        "avoid_tags": ["trabajo físico", "naturaleza", "arte"],
        "salary_range": "30.000€ – 85.000€/año",
        "demand": "Muy alta",
        "paths": ["FP ASIR / Redes", "Grado Ingeniería + especialización", "Certificaciones CEH/OSCP"],
        "work_style": "híbrido/remoto",
        "riasec": {"R": 40, "I": 85, "A": 20, "S": 20, "E": 50, "C": 60},
    },
    "inteligencia_artificial": {
        "name": "Inteligencia Artificial / ML Engineer",
        "description": "Desarrollo de modelos de inteligencia artificial y aprendizaje automático. Investigación y aplicación de redes neuronales, NLP y visión artificial.",
        "interests": ["matemáticas", "tecnología", "filosofía", "cerebro humano", "programación", "investigación"],
        "values": ["conocimiento", "innovación", "impacto global", "vanguardia"],
        "skills": ["matemáticas", "programación", "investigación", "abstracción"],
        "avoid_tags": ["trabajo físico", "atención al público"],
        "salary_range": "40.000€ – 120.000€/año",
        "demand": "Muy alta",
        "paths": ["Matemáticas/Física + Máster IA", "Ingeniería Informática + investigación", "Doctorado"],
        "work_style": "híbrido/remoto",
        "riasec": {"R": 20, "I": 95, "A": 30, "S": 15, "E": 35, "C": 55},
    },
    "videojuegos": {
        "name": "Desarrollo de Videojuegos",
        "description": "Diseño, programación y producción de videojuegos. Mezcla de arte, narrativa y tecnología para crear experiencias interactivas.",
        "interests": ["videojuegos", "programación", "arte", "narrativa", "tecnología", "animación"],
        "values": ["creatividad", "pasión", "innovación", "entretenimiento"],
        "skills": ["programación", "diseño", "trabajo en equipo", "creatividad"],
        "avoid_tags": ["sangre", "burocracia", "trabajo solitario extremo"],
        "salary_range": "22.000€ – 60.000€/año",
        "demand": "Media (sector en crecimiento)",
        "paths": ["FP Desarrollo de Videojuegos", "Grado en Ingeniería + Unity/Unreal", "Bootcamp GameDev"],
        "work_style": "presencial/híbrido",
        "riasec": {"R": 40, "I": 60, "A": 80, "S": 30, "E": 40, "C": 30},
    },
    "fp_informatica": {
        "name": "FP Informática (DAM/DAW/ASIR)",
        "description": "Formación profesional en desarrollo de apps móviles (DAM), desarrollo web (DAW) o administración de sistemas (ASIR). Salida laboral rápida.",
        "interests": ["tecnología", "programación", "web", "aplicaciones móviles", "redes"],
        "values": ["práctica", "resultados", "estabilidad", "autonomía"],
        "skills": ["programación", "resolución de problemas", "aprendizaje rápido"],
        "avoid_tags": ["burocracia", "ciencias teóricas puras"],
        "salary_range": "18.000€ – 45.000€/año",
        "demand": "Muy alta",
        "paths": ["FP Grado Medio → FP Grado Superior (2 años)", "Acceso directo desde ESO/Bachillerato"],
        "work_style": "híbrido/remoto",
        "riasec": {"R": 60, "I": 60, "A": 20, "S": 20, "E": 30, "C": 70},
    },

    # ── SALUD ────────────────────────────────────────────────────────────────
    "medicina": {
        "name": "Medicina",
        "description": "Diagnóstico, tratamiento y prevención de enfermedades. Contacto directo con pacientes, responsabilidad alta y vocación de servicio.",
        "interests": ["biología", "ayudar a personas", "ciencias", "cuerpo humano", "investigación"],
        "values": ["vocación", "responsabilidad", "impacto social", "conocimiento"],
        "skills": ["empatía", "memoria", "resistencia", "toma de decisiones"],
        "avoid_tags": ["tecnología", "oficina", "arte", "naturaleza exterior"],
        "salary_range": "35.000€ – 120.000€/año",
        "demand": "Alta",
        "paths": ["Selectividad (nota alta) + Grado en Medicina (6 años) + MIR"],
        "work_style": "presencial",
        "riasec": {"R": 50, "I": 80, "A": 20, "S": 70, "E": 30, "C": 50},
    },
    "enfermeria": {
        "name": "Enfermería",
        "description": "Cuidado directo de pacientes, administración de tratamientos y apoyo emocional. Pilar del sistema sanitario con alta demanda.",
        "interests": ["ayudar a personas", "biología", "cuidado", "salud", "contacto humano"],
        "values": ["vocación", "empatía", "impacto social", "responsabilidad"],
        "skills": ["empatía", "trabajo en equipo", "resistencia", "precisión"],
        "avoid_tags": ["tecnología pura", "arte", "naturaleza", "trabajo solitario"],
        "salary_range": "22.000€ – 45.000€/año",
        "demand": "Muy alta",
        "paths": ["Grado en Enfermería (4 años)", "Especialidad vía EIR"],
        "work_style": "presencial",
        "riasec": {"R": 40, "I": 50, "A": 15, "S": 90, "E": 20, "C": 50},
    },
    "psicologia": {
        "name": "Psicología",
        "description": "Estudio del comportamiento humano y apoyo a la salud mental. Intervención clínica, psicología educativa o de empresa.",
        "interests": ["personas", "comportamiento", "escuchar", "ayudar", "mente", "filosofía"],
        "values": ["empatía", "impacto social", "comprensión", "conocimiento"],
        "skills": ["escucha activa", "análisis", "paciencia", "comunicación"],
        "avoid_tags": ["tecnología pura", "matemáticas duras", "trabajo físico"],
        "salary_range": "20.000€ – 45.000€/año",
        "demand": "Media-alta (en auge)",
        "paths": ["Grado en Psicología (4 años) + Máster habilitante"],
        "work_style": "presencial/híbrido",
        "riasec": {"R": 15, "I": 70, "A": 30, "S": 90, "E": 35, "C": 35},
    },
    "farmacia": {
        "name": "Farmacia",
        "description": "Dispensación de medicamentos, asesoramiento farmacéutico y desarrollo de fármacos. Mezcla de ciencias y atención al público.",
        "interests": ["química", "biología", "salud", "ayudar a personas", "ciencias"],
        "values": ["responsabilidad", "conocimiento", "estabilidad", "salud"],
        "skills": ["precisión", "memoria", "comunicación", "análisis"],
        "avoid_tags": ["tecnología digital", "arte", "trabajo físico intenso"],
        "salary_range": "25.000€ – 55.000€/año",
        "demand": "Estable-alta",
        "paths": ["Grado en Farmacia (5 años)", "Doctorado para investigación"],
        "work_style": "presencial",
        "riasec": {"R": 30, "I": 75, "A": 10, "S": 60, "E": 30, "C": 65},
    },
    "fisioterapia": {
        "name": "Fisioterapia",
        "description": "Rehabilitación física de lesiones y enfermedades mediante técnicas manuales y ejercicio. Contacto directo y trabajo muy práctico.",
        "interests": ["cuerpo humano", "deporte", "salud", "anatomía", "ayudar a personas"],
        "values": ["vocación", "impacto directo", "autonomía", "salud"],
        "skills": ["empatía", "habilidad manual", "resistencia", "comunicación"],
        "avoid_tags": ["tecnología pura", "arte", "matemáticas duras", "trabajo sedentario"],
        "salary_range": "18.000€ – 40.000€/año",
        "demand": "Alta",
        "paths": ["Grado en Fisioterapia (4 años)", "Máster en especialidad"],
        "work_style": "presencial",
        "riasec": {"R": 70, "I": 45, "A": 20, "S": 80, "E": 25, "C": 35},
    },
    "veterinaria": {
        "name": "Veterinaria",
        "description": "Cuidado y tratamiento de animales, salud pública veterinaria e investigación. Para quien ama los animales tanto como las ciencias.",
        "interests": ["animales", "biología", "naturaleza", "ciencias", "cuidado"],
        "values": ["vocación", "responsabilidad", "conocimiento", "naturaleza"],
        "skills": ["empatía", "precisión", "resistencia", "toma de decisiones"],
        "avoid_tags": ["tecnología digital", "arte", "trabajo de oficina puro"],
        "salary_range": "22.000€ – 55.000€/año",
        "demand": "Media-alta",
        "paths": ["Grado en Veterinaria (5 años) + habilitación"],
        "work_style": "presencial",
        "riasec": {"R": 60, "I": 70, "A": 15, "S": 65, "E": 25, "C": 40},
    },
    "nutricion": {
        "name": "Nutrición y Dietética",
        "description": "Asesoramiento sobre alimentación saludable, planificación de dietas y educación nutricional para individuos y colectivos.",
        "interests": ["alimentación", "salud", "biología", "ayudar a personas", "deporte"],
        "values": ["salud", "impacto social", "conocimiento", "autonomía"],
        "skills": ["comunicación", "empatía", "análisis", "planificación"],
        "avoid_tags": ["tecnología pura", "trabajo físico intenso", "matemáticas duras"],
        "salary_range": "18.000€ – 38.000€/año",
        "demand": "Media-alta (en auge)",
        "paths": ["Grado en Nutrición Humana y Dietética (4 años)"],
        "work_style": "presencial/híbrido",
        "riasec": {"R": 30, "I": 60, "A": 20, "S": 80, "E": 35, "C": 45},
    },
    "fp_sanidad": {
        "name": "FP Sanidad (Técnico en Cuidados / Laboratorio)",
        "description": "Formación profesional sanitaria: técnico en cuidados auxiliares de enfermería, laboratorio clínico, imagen para el diagnóstico.",
        "interests": ["salud", "ayudar a personas", "biología", "trabajo práctico"],
        "values": ["vocación", "práctica", "estabilidad", "impacto"],
        "skills": ["empatía", "precisión", "trabajo en equipo"],
        "avoid_tags": ["tecnología digital", "arte", "trabajo solitario"],
        "salary_range": "16.000€ – 30.000€/año",
        "demand": "Alta",
        "paths": ["FP Grado Medio → FP Grado Superior (2 años)"],
        "work_style": "presencial",
        "riasec": {"R": 55, "I": 40, "A": 10, "S": 85, "E": 15, "C": 50},
    },

    # ── CIENCIAS ─────────────────────────────────────────────────────────────
    "biologia": {
        "name": "Biología / Ciencias Ambientales",
        "description": "Estudio de los seres vivos y el ecosistema. Investigación, medio ambiente, biotecnología o docencia universitaria.",
        "interests": ["naturaleza", "animales", "investigación", "ciencias", "medio ambiente", "ecología"],
        "values": ["conocimiento", "sostenibilidad", "naturaleza", "investigación"],
        "skills": ["observación", "análisis", "paciencia", "trabajo en laboratorio"],
        "avoid_tags": ["tecnología digital", "negocios", "arte"],
        "salary_range": "18.000€ – 45.000€/año",
        "demand": "Media",
        "paths": ["Grado en Biología (4 años)", "Máster + Doctorado para investigación"],
        "work_style": "presencial/laboratorio",
        "riasec": {"R": 50, "I": 90, "A": 20, "S": 40, "E": 20, "C": 50},
    },
    "quimica": {
        "name": "Química / Ingeniería Química",
        "description": "Síntesis de materiales, desarrollo de procesos industriales y control de calidad. Desde farmacéutica hasta energía.",
        "interests": ["química", "ciencias", "laboratorio", "resolver problemas", "industria"],
        "values": ["conocimiento", "precisión", "innovación", "industria"],
        "skills": ["análisis", "precisión", "concentración", "matemáticas"],
        "avoid_tags": ["arte", "ciencias sociales", "trabajo al aire libre constante"],
        "salary_range": "22.000€ – 55.000€/año",
        "demand": "Media-alta",
        "paths": ["Grado en Química o Ingeniería Química (4 años)", "Máster industrial"],
        "work_style": "presencial/laboratorio",
        "riasec": {"R": 60, "I": 90, "A": 10, "S": 20, "E": 25, "C": 65},
    },
    "fisica": {
        "name": "Física / Ingeniería Física",
        "description": "Comprensión de las leyes fundamentales del universo. Aplicaciones en energía, telecomunicaciones, astrofísica e investigación.",
        "interests": ["física", "matemáticas", "universo", "investigación", "tecnología", "energía"],
        "values": ["conocimiento", "vanguardia", "curiosidad", "rigor"],
        "skills": ["matemáticas", "abstracción", "concentración", "resolución de problemas"],
        "avoid_tags": ["arte", "ciencias sociales", "trabajo manual"],
        "salary_range": "24.000€ – 70.000€/año",
        "demand": "Media (alta en industria tech)",
        "paths": ["Grado en Física (4 años)", "Máster + Doctorado", "Sector privado: tech/finanzas"],
        "work_style": "híbrido/laboratorio",
        "riasec": {"R": 30, "I": 95, "A": 20, "S": 15, "E": 30, "C": 60},
    },
    "biotecnologia": {
        "name": "Biotecnología",
        "description": "Aplicación de técnicas biológicas a la medicina, agricultura e industria. Terapia génica, diagnóstico molecular, biopharma.",
        "interests": ["biología", "tecnología", "medicina", "investigación", "genética", "futuro"],
        "values": ["innovación", "impacto social", "conocimiento", "vanguardia"],
        "skills": ["análisis", "precisión", "investigación", "concentración"],
        "avoid_tags": ["arte", "ciencias sociales", "trabajo físico"],
        "salary_range": "25.000€ – 70.000€/año",
        "demand": "Alta y creciente",
        "paths": ["Grado en Biotecnología (4 años)", "Máster especializado", "Doctorado"],
        "work_style": "presencial/laboratorio",
        "riasec": {"R": 40, "I": 90, "A": 15, "S": 30, "E": 30, "C": 55},
    },
    "matematicas": {
        "name": "Matemáticas / Estadística",
        "description": "Resolución de problemas abstractos con aplicaciones en finanzas, seguros, investigación operativa e ingeniería.",
        "interests": ["matemáticas", "lógica", "resolver problemas", "patrones", "finanzas", "juegos"],
        "values": ["conocimiento", "precisión", "reto intelectual", "rigor"],
        "skills": ["abstracción", "análisis", "concentración", "pensamiento lógico"],
        "avoid_tags": ["arte", "contacto social intenso", "trabajo físico"],
        "salary_range": "26.000€ – 80.000€/año",
        "demand": "Alta (actuario, quant, data)",
        "paths": ["Grado en Matemáticas/Estadística (4 años)", "Máster en Finanzas/DS/Actuaría"],
        "work_style": "híbrido/remoto",
        "riasec": {"R": 20, "I": 95, "A": 15, "S": 15, "E": 35, "C": 75},
    },

    # ── DISEÑO Y ARTE ─────────────────────────────────────────────────────────
    "diseno_grafico": {
        "name": "Diseño Gráfico / UX-UI",
        "description": "Creación visual de marcas, interfaces y experiencias digitales. Mezcla de creatividad, psicología del usuario y herramientas digitales.",
        "interests": ["arte", "estética", "tecnología", "comunicación", "dibujo", "tendencias"],
        "values": ["creatividad", "expresión", "autonomía", "impacto visual"],
        "skills": ["atención al detalle", "comunicación visual", "empatía", "creatividad"],
        "avoid_tags": ["matemáticas duras", "ciencias puras", "trabajo físico"],
        "salary_range": "18.000€ – 50.000€/año",
        "demand": "Alta (UX especialmente)",
        "paths": ["Grado en Diseño", "FP Diseño Gráfico", "Autodidacta + portfolio"],
        "work_style": "híbrido",
        "riasec": {"R": 30, "I": 40, "A": 90, "S": 40, "E": 45, "C": 40},
    },
    "diseno_industrial": {
        "name": "Diseño Industrial / Ingeniería de Producto",
        "description": "Diseño de objetos físicos: muebles, dispositivos, packaging, vehículos. Combina creatividad con ingeniería y materiales.",
        "interests": ["diseño", "tecnología", "arte", "fabricación", "objetos", "innovación"],
        "values": ["creatividad", "precisión", "innovación", "impacto físico"],
        "skills": ["diseño 3D", "creatividad", "ingeniería", "atención al detalle"],
        "avoid_tags": ["ciencias sociales", "trabajo solo con personas"],
        "salary_range": "20.000€ – 50.000€/año",
        "demand": "Media",
        "paths": ["Grado en Diseño Industrial (4 años)", "Grado en Ingeniería de Diseño"],
        "work_style": "presencial/híbrido",
        "riasec": {"R": 65, "I": 55, "A": 85, "S": 20, "E": 40, "C": 35},
    },
    "cine_audiovisual": {
        "name": "Cine / Producción Audiovisual",
        "description": "Dirección, producción, edición y fotografía cinematográfica. Contar historias a través de la imagen en movimiento.",
        "interests": ["cine", "fotografía", "contar historias", "arte", "música", "creatividad"],
        "values": ["expresión", "creatividad", "pasión", "comunicación"],
        "skills": ["narrativa", "creatividad", "trabajo en equipo", "tecnología audiovisual"],
        "avoid_tags": ["matemáticas duras", "ciencias puras", "burocracia"],
        "salary_range": "16.000€ – 60.000€+ /año",
        "demand": "Competitiva",
        "paths": ["ESCAC / ECAM / Grado en Comunicación Audiovisual", "Autodidacta + proyectos"],
        "work_style": "presencial/proyecto",
        "riasec": {"R": 45, "I": 35, "A": 95, "S": 50, "E": 55, "C": 20},
    },
    "arquitectura": {
        "name": "Arquitectura",
        "description": "Diseño y planificación de edificios y espacios. Combina creatividad artística con ingeniería, normativa y gestión de proyectos.",
        "interests": ["diseño", "arte", "geometría", "construcción", "ciudad", "espacio"],
        "values": ["creatividad", "rigor", "impacto visual", "dejar huella"],
        "skills": ["diseño", "matemáticas", "planificación", "creatividad"],
        "avoid_tags": ["biología", "ciencias sociales puras", "trabajo al exterior constante"],
        "salary_range": "20.000€ – 60.000€/año",
        "demand": "Media (sector ciclíco)",
        "paths": ["Grado + Máster en Arquitectura (5+1 años)", "ETS Arquitectura"],
        "work_style": "híbrido",
        "riasec": {"R": 55, "I": 50, "A": 90, "S": 30, "E": 50, "C": 55},
    },
    "arquitectura_tecnica": {
        "name": "Arquitectura Técnica / Ingeniería de Edificación",
        "description": "Dirección de obra, mediciones, presupuestos y gestión técnica de proyectos de construcción. Más práctica que la arquitectura.",
        "interests": ["construcción", "diseño", "gestión", "obras", "matemáticas"],
        "values": ["práctica", "rigor", "estabilidad", "resultados"],
        "skills": ["organización", "matemáticas", "liderazgo", "planificación"],
        "avoid_tags": ["ciencias sociales puras", "arte puro", "trabajo sedentario total"],
        "salary_range": "22.000€ – 50.000€/año",
        "demand": "Media-alta",
        "paths": ["Grado en Arquitectura Técnica (4 años)"],
        "work_style": "presencial/obra",
        "riasec": {"R": 75, "I": 50, "A": 45, "S": 25, "E": 50, "C": 65},
    },

    # ── HUMANIDADES Y SOCIALES ────────────────────────────────────────────────
    "derecho": {
        "name": "Derecho / Abogacía",
        "description": "Asesoramiento legal, defensa y representación jurídica. Argumentación, negociación y conocimiento profundo del ordenamiento legal.",
        "interests": ["debate", "justicia", "argumentación", "sociedad", "política", "escritura"],
        "values": ["justicia", "rigor", "impacto", "poder argumentativo"],
        "skills": ["argumentación", "lectura", "memoria", "negociación"],
        "avoid_tags": ["tecnología pura", "ciencias naturales", "trabajo físico"],
        "salary_range": "22.000€ – 80.000€+ /año",
        "demand": "Media (competitivo)",
        "paths": ["Grado en Derecho (4 años) + Máster de Acceso a la Abogacía"],
        "work_style": "presencial",
        "riasec": {"R": 15, "I": 60, "A": 30, "S": 55, "E": 75, "C": 55},
    },
    "periodismo": {
        "name": "Periodismo / Comunicación",
        "description": "Investigación, redacción y difusión de información. Medios digitales, redes sociales, podcast, televisión o prensa escrita.",
        "interests": ["escritura", "actualidad", "comunicación", "redes sociales", "política", "sociedad"],
        "values": ["verdad", "impacto social", "comunicar", "curiosidad"],
        "skills": ["escritura", "comunicación", "curiosidad", "síntesis"],
        "avoid_tags": ["matemáticas duras", "ciencias naturales", "trabajo solitario extremo"],
        "salary_range": "16.000€ – 45.000€/año",
        "demand": "Competitiva (digital en auge)",
        "paths": ["Grado en Periodismo/Comunicación (4 años)", "Especialización digital"],
        "work_style": "híbrido",
        "riasec": {"R": 15, "I": 50, "A": 60, "S": 70, "E": 65, "C": 30},
    },
    "relaciones_internacionales": {
        "name": "Relaciones Internacionales / Ciencias Políticas",
        "description": "Análisis geopolítico, diplomacia, organizaciones internacionales, ONG y política exterior. Para mentes globales.",
        "interests": ["política", "idiomas", "historia", "viajes", "sociedad", "geopolítica"],
        "values": ["impacto global", "justicia", "conocimiento", "diversidad"],
        "skills": ["idiomas", "análisis", "comunicación", "negociación"],
        "avoid_tags": ["tecnología pura", "ciencias naturales", "trabajo físico"],
        "salary_range": "20.000€ – 55.000€/año",
        "demand": "Media",
        "paths": ["Grado en RRII/CCPP (4 años)", "Máster en organizaciones internacionales"],
        "work_style": "híbrido/viajes",
        "riasec": {"R": 10, "I": 65, "A": 35, "S": 70, "E": 75, "C": 45},
    },
    "traduccion": {
        "name": "Traducción e Interpretación",
        "description": "Traducción de textos y/o interpretación simultánea entre idiomas. Aplicaciones en derecho, medicina, diplomacia y literatura.",
        "interests": ["idiomas", "escritura", "cultura", "viajes", "comunicación", "literatura"],
        "values": ["precisión", "cultura", "comunicar", "autonomía"],
        "skills": ["idiomas", "escritura", "concentración", "memoria"],
        "avoid_tags": ["tecnología pura", "matemáticas duras", "trabajo físico"],
        "salary_range": "18.000€ – 40.000€/año",
        "demand": "Media",
        "paths": ["Grado en Traducción e Interpretación (4 años)", "Especialización + par de idiomas escasos"],
        "work_style": "remoto/híbrido",
        "riasec": {"R": 10, "I": 55, "A": 60, "S": 50, "E": 35, "C": 65},
    },
    "educacion": {
        "name": "Educación / Docencia",
        "description": "Enseñanza y formación en distintas etapas educativas. Impacto directo en el desarrollo de las personas.",
        "interests": ["niños", "enseñar", "comunicación", "paciencia", "conocimiento", "ayudar"],
        "values": ["vocación", "impacto social", "estabilidad", "transmitir"],
        "skills": ["paciencia", "comunicación", "organización", "empatía"],
        "avoid_tags": ["tecnología pura", "matemáticas duras", "trabajo solitario"],
        "salary_range": "24.000€ – 45.000€/año (funcionario)",
        "demand": "Estable",
        "paths": ["Magisterio Infantil/Primaria (4 años)", "Grado + Máster MAES para Secundaria"],
        "work_style": "presencial",
        "riasec": {"R": 20, "I": 55, "A": 45, "S": 90, "E": 40, "C": 50},
    },
    "trabajo_social": {
        "name": "Trabajo Social",
        "description": "Apoyo a personas en situación de vulnerabilidad: exclusión social, dependencia, familia, infancia. Agente de cambio social.",
        "interests": ["personas", "ayudar", "sociedad", "justicia social", "comunidad"],
        "values": ["vocación", "justicia social", "empatía", "impacto"],
        "skills": ["empatía", "escucha activa", "resolución de conflictos", "resiliencia"],
        "avoid_tags": ["tecnología pura", "matemáticas duras", "arte"],
        "salary_range": "18.000€ – 32.000€/año",
        "demand": "Alta",
        "paths": ["Grado en Trabajo Social (4 años)"],
        "work_style": "presencial",
        "riasec": {"R": 20, "I": 40, "A": 20, "S": 95, "E": 40, "C": 40},
    },
    "criminologia": {
        "name": "Criminología / Ciencias Forenses",
        "description": "Estudio del delito, el delincuente y el sistema penal. Perfiles psicológicos, ciencia forense y criminología aplicada.",
        "interests": ["misterio", "psicología", "justicia", "sociedad", "investigación", "crimen"],
        "values": ["justicia", "conocimiento", "reto intelectual", "impacto"],
        "skills": ["análisis", "pensamiento crítico", "observación", "memoria"],
        "avoid_tags": ["arte puro", "matemáticas duras extremas", "trabajo físico"],
        "salary_range": "18.000€ – 40.000€/año",
        "demand": "Media",
        "paths": ["Grado en Criminología (4 años)", "Doble grado Derecho + Criminología"],
        "work_style": "presencial",
        "riasec": {"R": 35, "I": 75, "A": 20, "S": 55, "E": 50, "C": 50},
    },

    # ── NEGOCIOS Y ECONOMÍA ───────────────────────────────────────────────────
    "administracion_empresas": {
        "name": "Administración de Empresas (ADE)",
        "description": "Gestión integral de empresas: finanzas, marketing, recursos humanos, estrategia. Puerta de entrada a casi cualquier sector.",
        "interests": ["negocios", "economía", "gestión", "liderazgo", "emprendimiento"],
        "values": ["resultados", "liderazgo", "estabilidad", "poder de decisión"],
        "skills": ["organización", "comunicación", "análisis", "liderazgo"],
        "avoid_tags": ["ciencias naturales puras", "arte", "trabajo físico manual"],
        "salary_range": "22.000€ – 70.000€+ /año",
        "demand": "Alta",
        "paths": ["Grado en ADE (4 años)", "MBA tras experiencia laboral"],
        "work_style": "híbrido",
        "riasec": {"R": 20, "I": 55, "A": 25, "S": 50, "E": 85, "C": 65},
    },
    "economia": {
        "name": "Economía",
        "description": "Análisis de mercados, política económica, macroeconomía y microeconomía. Orientación a investigación, banca central o consultoría.",
        "interests": ["economía", "matemáticas", "política", "sociedad", "estadística", "negocios"],
        "values": ["conocimiento", "rigor", "impacto social", "análisis"],
        "skills": ["análisis", "matemáticas", "escritura", "pensamiento crítico"],
        "avoid_tags": ["arte", "trabajo físico", "ciencias naturales"],
        "salary_range": "24.000€ – 70.000€/año",
        "demand": "Alta",
        "paths": ["Grado en Economía (4 años)", "Máster en Economía/Finanzas"],
        "work_style": "híbrido",
        "riasec": {"R": 15, "I": 80, "A": 15, "S": 40, "E": 70, "C": 75},
    },
    "finanzas": {
        "name": "Finanzas / Banca / Inversión",
        "description": "Gestión de activos, análisis bursátil, banca de inversión, fintech. Para quienes gustan de números y mercados financieros.",
        "interests": ["economía", "matemáticas", "negocios", "mercados", "inversión", "estadística"],
        "values": ["resultados", "éxito", "reto", "estabilidad económica"],
        "skills": ["análisis", "matemáticas", "toma de decisiones", "concentración"],
        "avoid_tags": ["arte", "ciencias naturales", "trabajo físico", "ciencias sociales puras"],
        "salary_range": "28.000€ – 120.000€+ /año",
        "demand": "Alta",
        "paths": ["ADE/Economía (4 años)", "CFA / Máster en Finanzas", "Fintech / banca digital"],
        "work_style": "presencial/híbrido",
        "riasec": {"R": 15, "I": 75, "A": 10, "S": 30, "E": 80, "C": 85},
    },
    "marketing_digital": {
        "name": "Marketing Digital",
        "description": "Estrategias de comunicación y ventas en entornos digitales. SEO, redes sociales, publicidad programática y growth hacking.",
        "interests": ["redes sociales", "comunicación", "tendencias", "negocios", "creatividad", "psicología"],
        "values": ["creatividad", "resultados", "dinamismo", "impacto"],
        "skills": ["comunicación", "análisis de datos", "creatividad", "adaptabilidad"],
        "avoid_tags": ["ciencias naturales", "trabajo físico", "matemáticas puras"],
        "salary_range": "20.000€ – 55.000€/año",
        "demand": "Alta",
        "paths": ["Grado en Marketing/Publicidad (4 años)", "Cursos especializados + experiencia"],
        "work_style": "híbrido/remoto",
        "riasec": {"R": 15, "I": 50, "A": 65, "S": 60, "E": 80, "C": 40},
    },
    "recursos_humanos": {
        "name": "Recursos Humanos / People & Culture",
        "description": "Selección, formación y desarrollo del talento en las organizaciones. Mediación, gestión del cambio y cultura empresarial.",
        "interests": ["personas", "psicología", "comunicación", "negocios", "gestión"],
        "values": ["empatía", "impacto", "organización", "desarrollo"],
        "skills": ["comunicación", "empatía", "organización", "negociación"],
        "avoid_tags": ["ciencias naturales", "matemáticas duras", "trabajo físico", "arte puro"],
        "salary_range": "20.000€ – 50.000€/año",
        "demand": "Media-alta",
        "paths": ["ADE/Psicología/RRHH (4 años)", "Máster en Dirección de RRHH"],
        "work_style": "híbrido",
        "riasec": {"R": 10, "I": 45, "A": 25, "S": 85, "E": 65, "C": 55},
    },

    # ── INGENIERÍA ────────────────────────────────────────────────────────────
    "ingenieria_civil": {
        "name": "Ingeniería Civil",
        "description": "Diseño y construcción de infraestructuras: puentes, carreteras, presas, obras hidráulicas. Ingeniería al servicio de la sociedad.",
        "interests": ["construcción", "matemáticas", "física", "diseño", "infraestructuras", "naturaleza"],
        "values": ["rigor", "impacto físico", "responsabilidad", "dejar huella"],
        "skills": ["matemáticas", "planificación", "liderazgo", "resolución de problemas"],
        "avoid_tags": ["arte puro", "ciencias sociales", "trabajo de oficina puro"],
        "salary_range": "26.000€ – 65.000€/año",
        "demand": "Alta (obras públicas)",
        "paths": ["Grado en Ingeniería Civil (4 años) + Máster habilitante"],
        "work_style": "presencial/obra",
        "riasec": {"R": 80, "I": 70, "A": 30, "S": 25, "E": 50, "C": 65},
    },
    "ingenieria_quimica": {
        "name": "Ingeniería Química",
        "description": "Diseño de procesos industriales basados en química: petroquímica, farmacéutica, alimentación, energía. Plantas industriales y reactores.",
        "interests": ["química", "física", "matemáticas", "industria", "resolución de problemas"],
        "values": ["innovación", "rigor", "industria", "impacto"],
        "skills": ["matemáticas", "análisis", "planificación", "resolución de problemas"],
        "avoid_tags": ["arte", "ciencias sociales", "contacto humano intenso"],
        "salary_range": "28.000€ – 65.000€/año",
        "demand": "Alta (energía e industria)",
        "paths": ["Grado en Ingeniería Química (4 años)"],
        "work_style": "presencial/industria",
        "riasec": {"R": 75, "I": 85, "A": 10, "S": 15, "E": 40, "C": 70},
    },
    "fp_electricidad": {
        "name": "FP Electricidad / Electrónica",
        "description": "Instalaciones eléctricas, mantenimiento industrial, domótica, energías renovables. Alta demanda y salida laboral muy rápida.",
        "interests": ["tecnología", "electricidad", "trabajo manual", "energía", "industria"],
        "values": ["práctica", "resultados", "estabilidad", "independencia"],
        "skills": ["habilidad manual", "resolución de problemas", "concentración"],
        "avoid_tags": ["arte", "ciencias sociales", "trabajo de oficina"],
        "salary_range": "20.000€ – 45.000€/año",
        "demand": "Muy alta",
        "paths": ["FP Grado Medio → FP Grado Superior (2 años)", "Acceso directo desde ESO"],
        "work_style": "presencial/obra",
        "riasec": {"R": 90, "I": 50, "A": 10, "S": 20, "E": 30, "C": 55},
    },

    # ── OTROS ────────────────────────────────────────────────────────────────
    "turismo": {
        "name": "Turismo / Gestión Hotelera",
        "description": "Gestión de establecimientos turísticos, eventos y experiencias. Sector muy internacional con posibilidad de trabajar en el extranjero.",
        "interests": ["viajes", "idiomas", "gente", "culturas", "gastronomía", "organización"],
        "values": ["dinamismo", "diversidad", "experiencias", "contacto humano"],
        "skills": ["idiomas", "comunicación", "organización", "atención al cliente"],
        "avoid_tags": ["matemáticas duras", "ciencias naturales", "trabajo solitario"],
        "salary_range": "16.000€ – 40.000€/año",
        "demand": "Alta (sector recuperado)",
        "paths": ["Grado en Turismo (4 años)", "FP Hostelería", "Especialización en eventos"],
        "work_style": "presencial/viajes",
        "riasec": {"R": 25, "I": 25, "A": 45, "S": 85, "E": 70, "C": 40},
    },
    "gastronomia": {
        "name": "Gastronomía / Chef",
        "description": "Arte culinario y gestión de cocina. Creación de platos, dirección de restaurantes, pastelería o consultoría gastronómica.",
        "interests": ["cocina", "arte", "creatividad", "culturas", "gastronomía", "comida"],
        "values": ["creatividad", "excelencia", "pasión", "expresión"],
        "skills": ["creatividad", "habilidad manual", "resistencia", "trabajo en equipo"],
        "avoid_tags": ["tecnología pura", "matemáticas duras", "trabajo sedentario"],
        "salary_range": "14.000€ – 60.000€+ /año",
        "demand": "Alta",
        "paths": ["FP Hostelería y Turismo", "Escuelas de hostelería privadas (Le Cordon Bleu, Basque Culinary)"],
        "work_style": "presencial",
        "riasec": {"R": 65, "I": 30, "A": 85, "S": 50, "E": 55, "C": 35},
    },
    "relaciones_publicas": {
        "name": "Relaciones Públicas / Comunicación Corporativa",
        "description": "Gestión de la imagen y reputación de organizaciones. Eventos, comunicación de crisis, branding y relaciones con medios.",
        "interests": ["comunicación", "redes sociales", "negocios", "eventos", "personas"],
        "values": ["imagen", "comunicar", "dinamismo", "influencia"],
        "skills": ["comunicación", "creatividad", "negociación", "redes"],
        "avoid_tags": ["ciencias naturales", "matemáticas duras", "trabajo físico", "trabajo solitario"],
        "salary_range": "18.000€ – 50.000€/año",
        "demand": "Media",
        "paths": ["Grado en Publicidad y RRPP (4 años)", "Marketing + especialización"],
        "work_style": "híbrido",
        "riasec": {"R": 10, "I": 30, "A": 65, "S": 75, "E": 85, "C": 35},
    },
    "logopedia": {
        "name": "Logopedia",
        "description": "Evaluación y tratamiento de trastornos del habla, lenguaje, voz y deglución. Trabajo con niños, adultos y personas con diversidad funcional.",
        "interests": ["personas", "lenguaje", "ayudar", "comunicación", "niños", "neurología"],
        "values": ["vocación", "empatía", "impacto", "conocimiento"],
        "skills": ["empatía", "paciencia", "observación", "comunicación"],
        "avoid_tags": ["tecnología pura", "matemáticas duras", "trabajo físico"],
        "salary_range": "18.000€ – 35.000€/año",
        "demand": "Alta y creciente",
        "paths": ["Grado en Logopedia (4 años)"],
        "work_style": "presencial",
        "riasec": {"R": 20, "I": 60, "A": 30, "S": 90, "E": 25, "C": 45},
    },
}


def get_all_careers():
    return CAREERS


def get_career(career_id: str):
    return CAREERS.get(career_id)


def match_careers(profile: dict, top_n: int = 5) -> list:
    """
    Matching semántico con sentence-transformers + penalización por avoid[].
    Si los embeddings no están disponibles, fallback a keyword matching.
    """
    try:
        return _semantic_match(profile, top_n)
    except Exception:
        return _keyword_match(profile, top_n)


def _build_profile_text(profile: dict) -> str:
    parts = []
    if profile.get("interests"):
        parts.append("Intereses: " + ", ".join(profile["interests"]))
    if profile.get("values"):
        parts.append("Valores: " + ", ".join(profile["values"]))
    if profile.get("skills"):
        parts.append("Habilidades: " + ", ".join(profile["skills"]))
    if profile.get("work_style") and profile["work_style"] != "no importa":
        parts.append("Estilo de trabajo preferido: " + profile["work_style"])
    return ". ".join(parts)


def _semantic_match(profile: dict, top_n: int) -> list:
    from sentence_transformers import SentenceTransformer
    import numpy as np

    model = _get_model()
    profile_text = _build_profile_text(profile)
    profile_emb = model.encode([profile_text], normalize_embeddings=True)[0]

    avoid_keywords = [a.lower() for a in profile.get("avoid", [])]

    scores = []
    for career_id, career in CAREERS.items():
        career_text = career["description"] + " " + ", ".join(career["interests"] + career["values"])
        career_emb = _get_career_embeddings()[career_id]
        cosine = float(np.dot(profile_emb, career_emb))

        # Penalización por avoid[]
        avoid_penalty = 0
        career_text_lower = (career["description"] + " " + " ".join(career.get("avoid_tags", []))).lower()
        for avoid_kw in avoid_keywords:
            for word in avoid_kw.split():
                if len(word) > 3 and word in career_text_lower:
                    avoid_penalty += 0.05
                    break

        final_score = max(0, cosine - avoid_penalty)
        scores.append((career_id, final_score, career))

    scores.sort(key=lambda x: x[1], reverse=True)
    return [
        {"id": cid, "score": round(s * 100, 1), **c}
        for cid, s, c in scores[:top_n]
    ]


_model_cache = None
_career_emb_cache = None


def _get_model():
    global _model_cache
    if _model_cache is None:
        from sentence_transformers import SentenceTransformer
        _model_cache = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    return _model_cache


def _get_career_embeddings():
    global _career_emb_cache
    if _career_emb_cache is None:
        model = _get_model()
        _career_emb_cache = {}
        for career_id, career in CAREERS.items():
            text = career["description"] + " " + ", ".join(career["interests"] + career["values"])
            emb = model.encode([text], normalize_embeddings=True)[0]
            _career_emb_cache[career_id] = emb
    return _career_emb_cache


def _keyword_match(profile: dict, top_n: int) -> list:
    """Fallback: keyword substring matching."""
    interests = [i.lower() for i in profile.get("interests", [])]
    values = [v.lower() for v in profile.get("values", [])]
    skills = [s.lower() for s in profile.get("skills", [])]
    avoid_keywords = [a.lower() for a in profile.get("avoid", [])]

    scores = []
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
        # Penalización avoid
        career_desc_lower = career["description"].lower()
        for avoid_kw in avoid_keywords:
            for word in avoid_kw.split():
                if len(word) > 3 and word in career_desc_lower:
                    score -= 2
                    break
        scores.append((career_id, score, career))

    scores.sort(key=lambda x: x[1], reverse=True)
    return [
        {"id": cid, "score": s, **c}
        for cid, s, c in scores[:top_n]
    ]
