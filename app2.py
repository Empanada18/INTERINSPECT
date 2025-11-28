import streamlit as st
import base64
import streamlit.components.v1 as components

# ==============================
# CONFIGURACIÓN GENERAL
# ==============================
st.set_page_config(
    page_title="Interinspect",
    page_icon="🛠️",
    layout="wide"
)

# ==============================
# CONTENEDOR DE PARTÍCULAS (200px alto, fondo negro)
# ==============================
particles_html = """
<div id="particles-js"></div>

<style>
#particles-js {
    position: relative;
    width: 100%;
    height: 200px; 
    background: #000000; /* Fondo negro sólido */
    margin-bottom: 20px;  /* Espacio debajo del bloque */
    z-index: 1;
}
</style>

<!-- Script de partículas -->
<script src="https://cdn.jsdelivr.net/npm/particles.js"></script>
<script>
particlesJS("particles-js", {
    "particles": {
        "number": { "value": 50 },
        "size": { "value": 3 },
        "color": { "value": "#ffffff" },
        "line_linked": { "color": "#ffffff" }
    }
});
</script>
"""

components.html(particles_html, height=220)

# ==============================
# FUNCIÓN PARA IMAGEN BASE64
# ==============================
def get_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ==============================
# CARGAR IMÁGENES
# ==============================
img_logo = get_base64("Logo_blanco.png")
img_api = get_base64("API.png")
img_asnt = get_base64("ASNT.png")
img_aws = get_base64("aws.png")
img_tech = get_base64("TECHBRIDGE.png")
img_evo = get_base64("evo.png")
img_pt = get_base64("photo.png")
img_ng = get_base64("negro.jpg")

# ==============================
# FONDO CON IMAGEN img_ng
# ==============================
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpeg;base64,{img_ng}");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}}

[data-testid="stHeader"] {{ 
    background: transparent !important; 
}}

.block-container {{
    padding-top: 20px !important;
    background: transparent !important;
}}

</style>
""", unsafe_allow_html=True)

# ==============================
# SECCIÓN: INICIO
# ==============================
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="hero-text-container" style="
    text-align:center;
    padding-top:2vh;
    color:white;
    animation: fadeSlide 1.8s ease-out forwards;
    opacity:0;
    transform:translateY(25px);
">
     <img src="data:image/jpeg;base64,{img_pt}" style="width:500px; height:290px; border-radius:20px; object-fit:cover; margin-bottom:50px;" />
    <h1 style="font-size:52px; font-weight:bold;">Bienvenido</h1>
    <h3 style="font-size:30px; font-weight:bold; margin-top:-10px; color: #A295C1;">
        "Ecosistema Cognitivo para la Evolución Industrial Inteligente"
    </h3>
    <p style="font-size:22px; margin-top:8px;">
        La transformación digital industrial ya no es un proyecto finito. Es una mutación evolutiva del ADN <br>
        organizacional: un proceso continuo donde la sensorización crítica, el análisis cognitivo, la prescripción <br>
        operativa, la monetización del riesgo y la maximizacion de rentabilidad operacional convergen en un <br>
        organismo inteligente que aprende de manera evolutiva.
    </p>

</div>

<style>
@keyframes fadeSlide {{
    0% {{opacity:0; transform:translateY(25px);}}
    100% {{opacity:1; transform:translateY(0);}}
}}
.hero-text-container a:hover {{
    background: #A295C1;
}}
</style>
""", unsafe_allow_html=True)

# ==============================
# SECCIÓN: SOBRE NOSOTROS
# ==============================
st.markdown('<div id="sobre" style="margin-top:150px;"></div>', unsafe_allow_html=True)
st.markdown(f"""
<style>
.about-us-card {{
    display: flex;
    flex-direction: row;
    gap: 24px;
    background: linear-gradient(135deg, #2e2e2e 0%, #4d4d4d 100%);
    border-radius: 20px;
    padding: 28px;
    box-shadow: 0 6px 26px rgba(20,30,55,0.18), 0 2px 14px rgba(44,62,80,0.08);
    margin-bottom: 32px;
    transition: transform .33s cubic-bezier(.37,1.7,.7,1), box-shadow .33s;
}}
.about-us-card:hover {{
    transform: translateY(-7px) scale(1.02);
    box-shadow: 0 14px 38px 0 #A295C130, 0 2px 18px rgba(44,62,80,0.12);
}}
.about-us-left {{
    flex: 1;
    min-width: 200px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 16px; /* espacio entre logos */
}}
.about-us-left img {{
    width: 400px;
    height: 120px;
    border-radius: 24px;
    object-fit: cover;
}}
.additional-logos {{
    display: flex;
    gap: 16px;
    justify-content: center;
    flex-wrap: wrap; /* que se acomoden en móviles */
}}
.additional-logos img {{
    width: 120px;
    height: 120px;
    border-radius: 16px;
    object-fit: contain;
}}
.about-us-right {{
    flex: 2;
    color: #fff;
    font-size: 1.05rem;
    line-height: 1.6;
}}
.about-us-title {{
    font-size: 1.3rem;
    font-weight: 700;
    margin-bottom: 12px;
    color: #A295C1;
}}
@media (max-width: 900px) {{
    .about-us-card {{
        flex-direction: column;
        align-items: center;
    }}
    .about-us-right {{
        text-align: center;
    }}
}}
</style>

<div class="about-us-card">
    <div class="about-us-left">
        <div class="additional-logos">
            <img src="data:image/png;base64,{img_evo}" />
            <img src="data:image/png;base64,{img_tech}" />
        </div>
        <img src="data:image/png;base64,{img_logo}" />
    </div>
    <div class="about-us-right">
        <div class="about-us-title">IDENTIDAD CORPORATIVA</div>
        <p><strong>Quiénes Somos</strong><br> Somos arquitectos de inteligencias industriales avanzadas. Diseñamos ecosistemas cognitivos capaces de percibir, interpretar, adelantar escenarios, tomar decisiones y evolucionar junto a tu operación.</p>
        <p><strong>Nuestra Visión</strong><br>Construir organizaciones industriales autónomas, resilientes y adaptativas, donde la cognición técnica se convierte en ventaja competitiva.</p>
        <p><strong>Nuestro Propósito</strong><br>Transformar industrias desde su estructura operativa y cultura organizacional, activando una evolución continua basada en ciencia, ingeniería y aprendizaje automatizado.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ==============================
# SECCIÓN: INDUSTRY-CX CORE
# ==============================
st.markdown('<div id="core" style="margin-top:20px;"></div>', unsafe_allow_html=True)
st.markdown(f"""
<style>

.industry-section {{
    background: linear-gradient(135deg, #2e2e2e 0%, #4d4d4d 100%);
    border-radius: 20px;
    padding: 28px;
    margin-bottom: 32px;
    color: white;
}}

.industry-title {{
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 16px;
    color: #A295C1;
    text-align: center;
}}
.industry-intro {{
    font-size: 1.05rem;
    margin-bottom: 24px;
    text-align: center;
}}
.industry-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
}}

.industry-card {{
    background: linear-gradient(135deg, #C9BFE7 0%, #E0D9F0 100%);
    color: #253451;
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
    transition: transform .33s, box-shadow .33s;
}}

.industry-card:hover {{
    transform: translateY(-5px) scale(1.03);
    box-shadow: 0 12px 26px rgba(0,0,0,0.2);
}}


.industry-name {{
    text-align: center;
    font-weight: 700;
    margin-bottom: 8px;
}}
.industry-description {{
    font-size: 0.95rem;
}}
.industry-footer {{
    text-align: center;
    margin-top: 24px;
    font-style: italic;
    font-size: 1rem;
}}
</style>

<div class="industry-section">
    <div class="industry-title">INDUSTRY-CX CORE — EL NÚCLEO COGNITIVO</div>
    <div class="industry-intro">
        INDUSTRY-CX CORE es ese organismo cognitivo que evoluciona contigo, con tus procesos, con tus mercados y con tu cultura técnica-organizacional.
    </div>
    <div class="industry-title">Un organismo inteligente capaz de:</div>
    <div class="industry-grid">
        <div class="industry-card">
            <div class="industry-name">Percibir</div>
            <div class="industry-description">Sensorización, telemetría, datos operativos IIoT, 3D, imágenes, NDT.</div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Actuar</div>
            <div class="industry-description">Automatización de workflows y toma de decisiones.</div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Integrar</div>
            <div class="industry-description">Fusión multimodal (modelos físicos + ML).</div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Aprender</div>
            <div class="industry-description"> Ajuste continuo del sistema.</div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Analizar</div>
            <div class="industry-description">Diagnóstico + simulación + predicción + prescripción.</div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Monetizar</div>
            <div class="industry-description">VaRO (Value at Risk Operational), CEIP (Costo Esperado de Interrupción de Producción), OPEX (Operational Expenditure).</div>
        </div>        
    </div>
    <div class="industry-title" style="margin-top: 20px;">🛠️ Instrumentación - 2da Capa (Ecosistema)</div>
    <div class="industry-grid">
        <div class="industry-card">
            <div class="industry-name">Capa Sensorial & IIoT</div>
            <div class="industry-description">
            * IIoT multisensor (vibración, presión, caudal, energía)
            * NDT avanzado (UT/PAUT, EMAT, AE, MFL, LRUT) <br>
            * Termografía IR (dron + fija + portátil) <br>
            * Geotecnia cognitiva (piezómetros, fibra óptica) <br>
            * Visión computacional industrial <br>
            * LIDAR 3D <br>
            * Integración OT/IT (SCADA, DCS, PLC) <br>
            * Edge AI + Cloud ML
            </div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Capa de Inteligencia</div>
            <div class="industry-description">
            * Gateways de datos OT/IT <br>
            * GPU/TPU para entrenamiento ML <br>
            * Motor prescriptivo con reglas sectoriales <br>
            * Gemelos cognitivos (físico + estadístico + ML) <br>
            * Dashboards 3D interactivos <br>
            * Integración con IA agéntica
            </div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Arquitectura & Core</div>
            <div class="industry-description">
            * Arquitectura híbrida Cloud-Edge <br>
            * Algoritmos ML + modelos físicos <br>
            * Pipelines n8n industriales <br>
            * Integración multiprotocolo (OPC-UA, MQTT, REST) <br>
            * Repositorios sectoriales de inteligencia <br>
            * Núcleo cognitivo INDUSTRY-CX CORE
            </div>
        </div>      
    </div>
</div>
""", unsafe_allow_html=True)


# ==============================
# SECCIÓN: EXPLORA POR INDUSTRIA (ESTILO MEJORADO)
# ==============================
st.markdown('<div id="industria" style="margin-top:20px;"></div>', unsafe_allow_html=True)
st.markdown(f"""
<style>

.industry-section {{
    background: linear-gradient(135deg, #2e2e2e 0%, #4d4d4d 100%);
    border-radius: 20px;
    padding: 28px;
    margin-bottom: 32px;
    color: white;
}}

.industry-title {{
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 16px;
    color: #A295C1;
    text-align: center;
}}
.industry-intro {{
    font-size: 1.05rem;
    margin-bottom: 24px;
    text-align: center;
}}
.industry-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
}}

.industry-card {{
    background: linear-gradient(135deg, #C9BFE7 0%, #E0D9F0 100%);
    color: #253451;
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
    transition: transform .33s, box-shadow .33s;
}}

.industry-card:hover {{
    transform: translateY(-5px) scale(1.03);
    box-shadow: 0 12px 26px rgba(0,0,0,0.2);
}}

/* -- CAMBIOS DE ESTILO AQUÍ -- */

.industry-name {{
    text-align: center;
    font-weight: 800; /* Mayor negrita */
    font-size: 1.1rem; /* Un poco más grande */
    margin-bottom: 8px;
    color: #253451; /* Color principal */
    text-transform: uppercase; /* Todo en mayúsculas */
    padding-bottom: 5px; /* Pequeño espacio debajo del título */
    border-bottom: 2px solid #A295C1; /* Separador morado */
}}

.industry-link {{
    text-align: center;
    font-weight: 700;
    font-size: 0.95rem;
    margin-top: 15px; /* Espacio antes del enlace/CTA */
    margin-bottom: 8px;
    color: #A295C1; /* Color morado para destacar */
    cursor: pointer; /* Indica que es clickable */
    transition: text-decoration 0.3s;
}}

.industry-link:hover {{
    text-decoration: underline; /* Subrayado al pasar el ratón */
}}

.industry-description {{
    font-size: 0.95rem;
    line-height: 1.4; /* Mejora la legibilidad de las listas */
    color: #3d4e6d; /* Un gris-azulado más suave para el cuerpo de texto */
}}

.industry-footer {{
    text-align: center;
    margin-top: 24px;
    font-style: italic;
    font-size: 1rem;
}}
</style>

<div class="industry-section">
    <div class="industry-title">Explora por Industria</div>
    <div class="industry-intro"><strong>Motores Cognitivos Sectoriales (Industrial Cognitive Engines)</strong></div>
    <div class="industry-intro">
        Cada industria posee un ADN operativo distinto. Nuestros motores cognitivos se adaptan a esa estructura.
    </div>
    <div class="industry-grid">
        <div class="industry-card">
            <div class="industry-name">MINEX-IN CORE - Minería</div>
            <div class="industry-description">Integridad predictiva, metalurgia inteligente, geotecnia cognitiva y optimización de plantas concentradoras.</div>
            <div class="industry-link">Conocer el MINEX-IN CORE</div>           <div class="industry-description">
            <strong>Instrumentación:</strong><br>
            •   drones IR <br>
            •   espesadores & slurry pipelines <br>
            •   sensores de densidad, torque, carga <br>
            •   UT/PAUT para piping minero <br>
            •   piezómetros/fibra óptica <br>
            •   ML para recuperación y granulometría
        </div>
        </div>
        <div class="industry-card">
            <div class="industry-name">ENERG-IN CORE - Energía</div>
            <div class="industry-description">Eficiencia energética, integridad térmica, redes inteligentes, fallas eléctricas.</div>
            <div class="industry-link">Conocer el ENERG-IN CORE</div>           <div class="industry-description">
            <strong>Instrumentación:</strong><br>
            •   termografía de subestaciones <br>
            •   descargas parciales <br>
            •   sensores de potencia & armónicos <br>
            •   vibración en turbinas <br>
            •   edge AI para anomalías eléctricas
            </div>
        </div>
        <div class="industry-card">
            <div class="industry-name">OILGAS-IN CORE - Oil & Gas</div>
            <div class="industry-description">Integridad Estructural API, gestion de la corrosión, RBI 580/581 Inspeccion basada en Riesgo, detección temprana y prediccón de fallas críticas en tuberías, tanques y sistemas presurizados.</div>
            <div class="industry-link">Conocer OILGAS-IN CORE</div>             <div class="industry-description">
            <strong>Instrumentación:</strong><br>
            •   MFL <br>
            •   pigging inteligente <br>
            •   corrosímetros electroquímicos <br>
            •   UT/PAUT de alta velocidad <br>
            •   visión ATEX <br>
            •   monitoreo continuo de H2S
            </div>
        </div>
        <div class="industry-card">
            <div class="industry-name">MANUF-IN CORE - Manufactura</div>
            <div class="industry-description">OEE cognitivo, scrap cero, computer vision para calidad y líneas autónomas.</div>
            <div class="industry-link">Conocer MAFUF-IN CORE</div>          <div class="industry-description">
            <strong>Instrumentación:</strong><br>
            •   cámaras industriales 4K <br>
            •   sensores de vibración/acústica <br>
            •   sistemas robotizados <br>
            •   espectroscopía de inspección <br>
            •   PLC + IIoT assembly line
            </div>
        </div>
        <div class="industry-card">
            <div class="industry-name">AGRO-IN CORE - Agroindustria</div>
            <div class="industry-description">IA climática, eficiencia hídrica, trazabilidad blockchain, control de plagas.</div>
            <div class="industry-link">Conocer AGRO-IN CORE</div>           <div class="industry-description">
            <strong>Instrumentación:</strong><br>
            •   NDVI + drones multiespectrales <br>
            •   sensores de humedad & CO₂ <br>
            •   estaciones meteorológicas <br>
            •   RFID, blockchain IoT <br>
            •   visión para madurez & plagas
            </div>
        </div>
        <div class="industry-card">
            <div class="industry-name">METAL-IN CORE - Metalurgia (extractiva + física)</div>
            <div class="industry-description">Hornos inteligentes, fundición optimizada, refinación predictiva, laminación controlada.</div>
            <div class="industry-link">Conocer METAL-IN CORE</div>          <div class="industry-description">
            <strong>Instrumentación:</strong><br>
            •   pirómetros ópticos <br>
            •   termopares de alta temperatura <br>
            •   sensores de deformación <br>
            •   visión térmica industrial <br>
            •   ML para curvas térmicas
            </div>
        </div>
</div>
""", unsafe_allow_html=True)

# ==============================
# SECCIÓN: EXPLORAR POR CAPACIDADES COGNITIVAS
# ==============================
st.markdown('<div id="capacidades" style="margin-top:20px;"></div>', unsafe_allow_html=True)
st.markdown(f"""

<style>
/* Estilo del contenedor principal (sin cambios) */
.industry-section {{
    background: linear-gradient(135deg, #2e2e2e 0%, #4d4d4d 100%);
    border-radius: 20px;
    padding: 28px;
    margin-bottom: 32px;
    color: white;
}}
.industry-title {{
    font-size: 1.8rem;
    font-weight: 800; /* Mayor negrita */
    margin-bottom: 16px;
    color: #A295C1;
    text-align: center;
}}
.industry-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); /* Aumento el tamaño mínimo para mejor lectura */
    gap: 20px;
}}
.industry-card {{
    background: linear-gradient(135deg, #E0D9F0 0%, #C9BFE7 100%); /* Cambio el orden del gradiente */
    color: #253451;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
    transition: transform .33s, box-shadow .33s;
    display: flex; /* Añadido para igualar altura */
    flex-direction: column; /* Añadido para igualar altura */
}}
.industry-card:hover {{
    transform: translateY(-5px) scale(1.02);
    box-shadow: 0 12px 26px rgba(0,0,0,0.2);
}}

/* --- ESTILOS MEJORADOS PARA LA VISUALIZACIÓN --- */

.industry-name {{
    text-align: center;
    font-weight: 800; 
    font-size: 1.2rem; /* Más grande */
    margin-bottom: 12px;
    color: #253451; 
    text-transform: uppercase; /* MAYÚSCULAS */
    padding-bottom: 5px; 
    border-bottom: 3px solid #A295C1; /* Separador más grueso y visible */
    flex-shrink: 0; 
}}
.instrumentation-list {{ /* Nueva clase para la lista de instrumentación */
    font-size: 0.9rem;
    line-height: 1.4;
    color: #4b4b4b; /* Un gris más oscuro */
    flex-grow: 1; /* Esto ayuda a que todas las tarjetas tengan la misma altura */
    margin-top: 2px;
}}
.instrumentation-list strong {{
    color: #253451; /* Destaca el título "Instrumentación" */
    display: block;
    margin-bottom: 2px;
}}
</style>

<div class="industry-section">
    <div class="industry-title" style="margin-top: 20px;">EXPLORAR POR CAPACIDADES COGNITIVAS</div>
    <div class="industry-grid">
        <div class="industry-card">
            <div class="industry-name">Integridad Predictiva</div>
            <div class="industry-description">
            Identifica, mide y anticipa mecanismos de daño antes de que se vuelvan críticos, combinando datos de inspección avanzada con análisis cognitivo para estimar vida remanente y riesgo estructural. Permite priorizar reparaciones, reducir fallas y extender la fiabilidad de activos.<br><br> 
            </div>
            <div class="instrumentation-list">
            <strong>Instrumentación (segunda capa):</strong> <br>
            UT/PAUT, EMAT, MFL, Acoustic Emission (AE), termografía IR, drones, LRUT, corrosímetros, análisis de vida remanente, digital twins de integridad.
            </div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Mantenimiento Cognitivo</div>
            <div class="industry-description">
            Detecta patrones de deterioro, anomalías y fallas incipientes mediante análisis vibracional, termografía y datos IIoT, generando recomendaciones automáticas basadas en modelos ML y reglas operativas. Reduce tiempos muertos, optimiza repuestos y habilita mantenimiento prescriptivo.<br><br> 
            </div>
            <div class="instrumentation-list">
            <strong>Instrumentación (segunda capa):</strong> <br>
            Sensores de vibración (acc/vel), termografía térmica, IoT industrial, streaming de datos, edge AI para detección de anomalías, prescripción automática.
            </div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Optimización de Procesos</div>
            <div class="industry-description">
            Integra modelos ML, modelos físicos y variables críticas de operación para identificar cuellos de botella, optimizar parámetros metalúrgicos o productivos y maximizar eficiencia energética, química o mecánica. Permite operar en el punto óptimo, con ajustes dinámicos basados en resultados reales.<br><br> 
            </div>
            <div class="instrumentation-list">
            <strong>Instrumentación (segunda capa):</strong> <br>
            Torque, densidad, caudal, granulometría, temperatura, reactivos, sensores de energía, modelos híbridos (físico + ML), simulación cognitiva.
            </div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Seguridad Prescriptiva (SPIR-HSE)</div>
            <div class="industry-description">
            Detecta condiciones inseguras, comportamientos de riesgo y patrones que preceden incidentes mediante visión computacional e IA cognitiva, emitiendo alertas prescriptivas y acciones recomendadas. Integra monitoreo ambiental, humano y operacional en un sistema HSE inteligente.<br><br> 
            </div>
            <div class="instrumentation-list">
            <strong>Instrumentación (segunda capa):</strong> <br>
            Visión para comportamiento seguro, detección automatizada de EPP, sensores ambientales, predicción HSE basada en ML, alarmas cognitivas, análisis de proximidad y zonas críticas.
            </div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Formación y Entrenamiento Inteligente (AR/AI)</div>
            <div class="industry-description">
            Guía procedimientos operativos mediante realidad aumentada e inteligencia cognitiva, reduciendo errores humanos, acelerando el aprendizaje técnico y estandarizando tareas críticas. El sistema actúa como un “copiloto industrial” que asiste al operador en tiempo real.<br><br> 
            </div>
            <div class="instrumentation-list">
            <strong>Instrumentación (segunda capa):</strong> <br>
            HMS (Hybrid Mentorship System), RA operativa, visores AR/VR, workflows guiados, reconocimiento de pasos, checklists inteligentes, instructivos cognitivos.
            </div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Monetización del Riesgo y Maximización de Rentabilidad</div>
            <div class="industry-description">
            Convierte datos técnicos en impacto financiero real monetizado, cuantificando cómo cada falla o su potencial de ocurrencia, una desviación o anomalía afecta costos, OPEX, disponibilidad y producción. Permite priorizar decisiones operacionales prescriptivas según retorno económico, reduciendo pérdidas y maximizando rentabilidad operacional.<br><br> 
            </div>
            <div class="instrumentation-list">
            <strong>Instrumentación (segunda capa):</strong> <br>
            Modelo VaRO (Value at Risk Operational), simulaciones de degradación, OPEX (Operational Expenditure), optimización energética, ML financiero, gemelos económicos.
            </div>
        </div>
</div>
""", unsafe_allow_html=True)


# ==============================
# SECCIÓN: PROCESO DE VALOR
# ==============================
st.markdown('<div id="proceso" style="margin-top: 20px;"></div>', unsafe_allow_html=True)
st.markdown(f"""
<style>
.timeline-section {{
    background: linear-gradient(135deg, #2e2e2e 0%, #4d4d4d 100%);
    border-radius: 20px;
    padding: 40px 28px;
    margin-bottom: 32px;
    color: white;
    text-align: center;
}}
.timeline-title {{
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 16px;
    color: #A295C1;
}}
.timeline-intro {{
    font-size: 1.05rem;
    margin-bottom: 40px;
}}
.timeline-container {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    margin: 0 20px;
}}
.timeline-line {{
    position: absolute;
    top: 50%;
    left: 5%;
    width: 90%;
    height: 10px;
    background: linear-gradient(135deg, #C9BFE7 0%, #E0D9F0 100%);
    border-radius: 5px;
    z-index: 0;
}}
.phase-card {{
    background: linear-gradient(135deg, #C9BFE7 0%, #E0D9F0 100%);
    color: #253451;
    border-radius: 16px;
    padding: 20px;
    width: 180px;
    z-index: 1;
    transition: transform .3s, box-shadow .3s;
    position: relative;
}}
.phase-card:hover {{
    transform: translateY(-10px) scale(1.05);
    box-shadow: 0 12px 26px rgba(0,0,0,0.3);
}}
.phase-name {{
    font-weight: 700;
    margin-bottom: 8px;
}}
.phase-description {{
    font-size: 0.95rem;
}}
@media (max-width: 900px) {{
    .timeline-container {{
        flex-direction: column;
        align-items: center;
    }}
    .timeline-line {{
        width: 4px;
        height: 80%;
        left: 50%;
        top: 10%;
    }}
    .phase-card {{
        width: 80%;
        margin-bottom: 30px;
    }}
}}
</style>

<div class="timeline-section">
    <div class="timeline-title">PROCESO DE VALOR - EL VIAJE EVOLUTIVO</div>
    <div class="timeline-intro">
        Tu operación sigue una trayectoria diseñada hacia autonomía cognitiva.
    </div>
    <div class="timeline-container">
        <div class="timeline-line"></div>
        <div class="phase-card">
            <div class="phase-name">Fase 1 - Diagnóstico Cognitivo</div>
            <div class="phase-description">Evaluación técnica + digital + NDT + sensorización.</div>
        </div>
        <div class="phase-card">
            <div class="phase-name">Fase 2 - Pilotaje Dirigido</div>
            <div class="phase-description">Edge AI + sensores + workflows Automatizados.</div>
        </div>
        <div class="phase-card">
            <div class="phase-name">Fase 3 - Integración Escalable</div>
            <div class="phase-description">Despliegue de las capacidades cognitivas requeridas.</div>
        </div>
        <div class="phase-card">
            <div class="phase-name">Fase 4 - Gemelos Cognitivos</div>
            <div class="phase-description">Modelos 3D + simulación + prescripción.</div>
        </div>
        <div class="phase-card">
            <div class="phase-name">Fase 5 - Autonomía Operativa</div>
            <div class="phase-description">Proceso autoajustable con aprendizaje continuo.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==============================
# SECCIÓN: GESTIÓN TECNOLÓGICA & CO-INNOVACIÓN (I+D+I)
# ==============================
st.markdown('<div id="idi"></div>', unsafe_allow_html=True)
st.markdown(f"""
<style>

.industry-section {{
    background: linear-gradient(135deg, #2e2e2e 0%, #4d4d4d 100%);
    border-radius: 20px;
    padding: 28px;
    margin-bottom: 32px;
    color: white;
}}

.industry-title {{
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 16px;
    color: #A295C1;
    text-align: center;
}}
.industry-intro {{
    font-size: 1.05rem;
    margin-bottom: 24px;
    text-align: center;
}}
.industry-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
}}

.industry-card {{
    background: linear-gradient(135deg, #C9BFE7 0%, #E0D9F0 100%);
    color: #253451;
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
    transition: transform .33s, box-shadow .33s;
}}

.industry-card:hover {{
    transform: translateY(-5px) scale(1.03);
    box-shadow: 0 12px 26px rgba(0,0,0,0.2);
}}


.industry-name {{
    text-align: center;
    font-weight: 700;
    margin-bottom: 8px;
}}
.industry-description {{
    font-size: 0.95rem;
}}
.industry-footer {{
    text-align: center;
    margin-top: 24px;
    font-style: italic;
    font-size: 1rem;
}}
</style>

<div class="industry-section">
    <div class="industry-title">GESTIÓN TECNOLÓGICA & CO-INNOVACIÓN (I+D+I)</div>
    <div class="industry-intro">
        Co-evolucionamos contigo.
    </div>
    <div class="industry-grid">
        <div class="industry-card">
            <div class="industry-name">Acompañamos desde:</div>
            <div class="industry-description">vigilancia tecnológica, exploración de soluciones, prototipado, pruebas de campo, industrialización, escalamiento.</div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Instrumentación:</div>
            <div class="industry-description">Bancos de prueba, sensores prototipo, simuladores, experimentación ML, documentación técnica, integración API.</div>
        </div>        
    </div>
</div>
""", unsafe_allow_html=True)

# ==============================
# SECCIÓN: MADUREZ DIGITAL & EVOLUCIÓN COGNITIVA
# ==============================
st.markdown('<div id="madurez" style="margin-top:20px;"></div>', unsafe_allow_html=True)
st.markdown(f"""
<style>
.services-section {{
    background: linear-gradient(135deg, #2e2e2e 0%, #4d4d4d 100%);
    border-radius: 20px;
    padding: 28px;
    margin-bottom: 32px;
    color: white;
}}
.services-title {{
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 16px;
    color: #A295C1;
    text-align: center;
}}
.services-intro {{
    font-size: 1.05rem;
    margin-bottom: 24px;
    text-align: center;
}}
.services-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
}}

.services-card {{
    background: linear-gradient(135deg, #C9BFE7 0%, #E0D9F0 100%);
    color: #253451;
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
    transition: transform .33s, box-shadow .33s;
    text-align: center;
}}

.services-card:hover {{
    transform: translateY(-5px) scale(1.03);
    box-shadow: 0 12px 26px rgba(0,0,0,0.2);
}}

.services-name {{
    font-weight: 700;
    margin-bottom: 8px;
}}
.services-description {{
    font-size: 0.95rem;
}}
.services-footer {{
    text-align: center;
    margin-top: 24px;
    font-style: italic;
    font-size: 1rem;
}}
</style>

<div class="services-section">
    <div class="services-title">MADUREZ DIGITAL & EVOLUCIÓN COGNITIVA</div>
    <div class="services-intro">
        ¿Dónde estás hoy? ¿Hacia dónde puedes evolucionar?<br>
        Niveles:
    </div>
    <div class="services-grid">
        <div class="services-card">
            <div class="services-name">0<br>Operación intuitiva</div>
        </div>
        <div class="services-card">
            <div class="services-name">1<br>igitalización inicial</div>
        </div>
        <div class="services-card">
            <div class="services-name">2<br>Integración OT/IT</div>
        </div>
        <div class="services-card">
            <div class="services-name">3<br>Predicción</div>
        </div>
        <div class="services-card">
            <div class="services-name">4<br>Prescripción</div>
        </div>
        <div class="services-card">
            <div class="services-name">5<br>Autonomía cognitiva</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==============================
# SECCIÓN: LABORATORIO COGNITIVO & SIMULADOR DE EVOLUCIÓN
# ==============================
st.markdown('<div id="lab"></div>', unsafe_allow_html=True)
st.markdown(f"""
<style>

.industry-section {{
    background: linear-gradient(135deg, #2e2e2e 0%, #4d4d4d 100%);
    border-radius: 20px;
    padding: 28px;
    margin-bottom: 32px;
    color: white;
}}

.industry-title {{
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 16px;
    color: #A295C1;
    text-align: center;
}}
.industry-intro {{
    font-size: 1.05rem;
    margin-bottom: 24px;
    text-align: center;
}}
.industry-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
}}

.industry-card {{
    background: linear-gradient(135deg, #C9BFE7 0%, #E0D9F0 100%);
    color: #253451;
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
    transition: transform .33s, box-shadow .33s;
}}

.industry-card:hover {{
    transform: translateY(-5px) scale(1.03);
    box-shadow: 0 12px 26px rgba(0,0,0,0.2);
}}


.industry-name {{
    text-align: center;
    font-weight: 700;
    margin-bottom: 8px;
}}
.industry-description {{
    font-size: 0.95rem;
}}
.industry-footer {{
    text-align: center;
    margin-top: 24px;
    font-style: italic;
    font-size: 1rem;
}}
</style>

<div class="industry-section">
    <div class="industry-title">LABORATORIO COGNITIVO & SIMULADOR DE EVOLUCIÓN</div>
    <div class="industry-intro">
        Explora, mide y proyecta el futuro de tu operación.<br>
        Un espacio integral donde puedes:
    </div>
    <div class="industry-grid">
        <div class="industry-card">
            <div class="industry-name">Experimentar (capa técnica):</div>
            <div class="industry-description">
            •	gemelos cognitivos<br>
            •	modelos predictivos<br>
            •	simuladores de falla<br>
            •	dashboards 3D<br>
            •	KPIs cognitivos<br>
            •	análisis técnico y operativo
            </div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Proyectar (capa estratégica):</div>
            <div class="industry-description">
            •	disponibilidad futura<br>
            •	reducción de riesgo<br>
            •	ahorro energético<br>
            •	impacto financiero<br>
            •	escenarios por industria<br>
            •	simulaciones 6m / 1 año / 3 años
            </div>
        </div>        
    </div>
</div>
""", unsafe_allow_html=True)

# ==============================
# SECCIÓN: CONTACTO INTELIGENTE
# ==============================
st.markdown('<div id="ctoit"></div>', unsafe_allow_html=True)
st.markdown(f"""
<style>

.industry-section {{
    background: linear-gradient(135deg, #2e2e2e 0%, #4d4d4d 100%);
    border-radius: 20px;
    padding: 28px;
    margin-bottom: 32px;
    color: white;
}}

.industry-title {{
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 16px;
    color: #A295C1;
    text-align: center;
}}
.industry-intro {{
    font-size: 1.05rem;
    margin-bottom: 24px;
    text-align: center;
}}
.industry-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
}}

.industry-card {{
    background: linear-gradient(135deg, #C9BFE7 0%, #E0D9F0 100%);
    color: #253451;
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
    transition: transform .33s, box-shadow .33s;
}}

.industry-card:hover {{
    transform: translateY(-5px) scale(1.03);
    box-shadow: 0 12px 26px rgba(0,0,0,0.2);
}}


.industry-name {{
    text-align: center;
    font-weight: 700;
    margin-bottom: 8px;
}}
.industry-description {{
    font-size: 0.95rem;
}}
.industry-footer {{
    text-align: center;
    margin-top: 24px;
    font-style: italic;
    font-size: 1rem;
}}
</style>

<div class="industry-section">
    <div class="industry-title">CONTACTO INTELIGENTE</div>
    <div class="industry-grid">
        <div class="industry-card">
            <div class="industry-name">Onboarding guiado por IA:</div>
            <div class="industry-description">
            •	prediagnóstico<br>
            •	recomendación de capacidades<br>
            •	match por industria<br>
            •	agendamiento inteligente
            </div>
        </div>        
    </div>
</div>
""", unsafe_allow_html=True)

# ==============================
# SECCIÓN: LABORATORIO DIGITAL Y FEEDBACK
# ==============================
st.markdown('<div id="laboratorio" style="margin-top:40px;"></div>', unsafe_allow_html=True)
st.markdown(f"""
<style>
.lab-section {{
    background: linear-gradient(135deg, #2e2e2e 0%, #4d4d4d 100%);
    color: white;
    border-radius: 20px;
    padding: 40px 28px;
    margin-bottom: 32px;
}}
.lab-title {{
    font-size: 2rem;
    font-weight: 700;
    text-align: center;
    color: #A295C1;
    margin-bottom: 16px;
}}
.lab-intro {{
    font-size: 1.05rem;
    text-align: center;
    margin-bottom: 32px;
}}
.lab-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
}}
.lab-card {{
    background: linear-gradient(135deg, #C9BFE7 0%, #E0D9F0 100%);
    color: #253451;
    border-radius: 16px;
    padding: 18px;
    text-align: center;
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
    transition: transform .33s, box-shadow .33s;
}}

.lab-card:hover {{
    transform: translateY(-5px) scale(1.03);
    box-shadow: 0 12px 26px rgba(0,0,0,0.2);
}}

.lab-card-icon {{
    font-size: 36px; /* Aquí puedes poner un emoji o imagen pequeña */
    margin-bottom: 12px;
}}
.lab-footer {{
    text-align: center;
    margin-top: 24px;
    font-style: italic;
    font-size: 1rem;
}}
</style>

<div class="lab-section">
    <div class="lab-title">Laboratorio Digital y Feedback</div>
    <div class="lab-intro">
        Participa en nuestro laboratorio digital: prueba, mide y colabora en el desarrollo de las soluciones que transformarán tu industria.
    </div>
    <div class="lab-grid">
        <div class="lab-card">
            <div class="lab-card-icon">📊</div>
            <div class="lab-card-name">Tableros de KPI personalizables</div>
        </div>
        <a href="https://simefcalculator.streamlit.app/" target="_blank" style="text-decoration:none;">
            <div class="lab-card">
                <div class="lab-card-icon">🖥️</div>
                <div class="lab-card-name">Sistema Inteligente de Evaluación de Mecanismos de Falla</div>
            </div>
        </a>
        <div class="lab-card">
            <div class="lab-card-icon">💬</div>
            <div class="lab-card-name">Feedback en tiempo real y foros de usuarios</div>
        </div>
    </div>
    <div class="lab-footer">
        Tu opinión guía nuestra innovación.
    </div>
</div>
""", unsafe_allow_html=True)


# ==============================
# SECCIÓN: CONTACTO PLEGABLE (con st.expander)
# ==============================
st.markdown('<div id="contacto" style="margin-top:40px;"></div>', unsafe_allow_html=True)

# ----------------------------------------------------
# 1. ENCABEZADO DE LA SECCIÓN (Markdown sin el contenido)
# ----------------------------------------------------
st.markdown("""
<div class="contact-section-header" style="
    background: linear-gradient(135deg, #2e2e2e 0%, #4d4d4d 100%);
    border-radius: 20px 20px 0 0; /* Bordes solo arriba */
    padding: 28px;
    color: white;
">
    <div style="font-size: 1.8rem; font-weight: 700; color: #A295C1; text-align: center; margin-bottom: 5px;">Hablemos de tu Evolución</div>
    <div style="font-size: 1.05rem; text-align: center;">Haz clic para desplegar el formulario de contacto.</div>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 2. CONTENIDO PLEGABLE (st.expander)
# ----------------------------------------------------
with st.expander("Abrir Formulario y Opciones de Contacto", expanded=False):
    
    # ----------------------------------------------------
    # 2.1. FORMULARIO DE GOOGLE (Incrustado)
    # ----------------------------------------------------
    
    # Reemplaza esta URL con la tuya
    GOOGLE_FORM_URL = "https://forms.gle/nfN3effJfcoqDSQ29" 

    st.markdown("### 📧 Formulario de Contacto")
    
    # Usamos st.container para darle un borde visual al iframe
    with st.container(border=True):
        components.iframe(
            GOOGLE_FORM_URL,
            height=600, # Ajusta la altura según lo necesites
            scrolling=True
        )
    
    # ----------------------------------------------------
    # 2.2. BOTÓN DE WHATSAPP (Añadido para contacto directo)
    # ----------------------------------------------------
    numero_wps = "51923739372" # Tu número con código de país + número
    mensaje_wps = "Hola, he visitado su página de Streamlit y me gustaría tener más información sobre sus soluciones digitales."
    import urllib.parse
    mensaje_codificado = urllib.parse.quote(mensaje_wps)
    url_wps = f"https://wa.me/{numero_wps}?text={mensaje_codificado}"

    st.markdown(f"""
    <div style="text-align: center; margin-top: 20px; margin-bottom: 5px;">
        <a href="{url_wps}" target="_blank" style="text-decoration: none;">
            <div style="
                display: inline-block;
                padding: 12px 25px;
                border-radius: 8px;
                background-color: #25D366; 
                color: white;
                font-weight: bold;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: background-color 0.3s ease;
            ">
                🟢 Contáctanos por WhatsApp
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------
# 3. Cierre visual de la sección (opcional)
# ----------------------------------------------------
st.markdown('<div style="background: linear-gradient(135deg, #2e2e2e 0%, #4d4d4d 100%); height: 20px; border-radius: 0 0 20px 20px; margin-bottom: 32px;"></div>', unsafe_allow_html=True)

# ==============================
# SECCIÓN: CIERRE INSTITUCIONAL
# ==============================
st.markdown('<div id="ctoit"></div>', unsafe_allow_html=True)
st.markdown(f"""
<style>

.industry-section {{
    background: linear-gradient(135deg, #2e2e2e 0%, #4d4d4d 100%);
    border-radius: 20px;
    padding: 28px;
    margin-bottom: 32px;
    color: white;
}}
.industry-intro {{
    font-size: 1.05rem;
    margin-bottom: 24px;
    text-align: center;
}}
</style>

<div class="industry-section">
    <div class="industry-intro">
        "INDUSTRY-CX CORE no es una plataforma tecnológica. Es un organismo industrial cognitivo que evoluciona con tu empresa transformando procesos, activos y personas."
    </div>
</div>
""", unsafe_allow_html=True)
