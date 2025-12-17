import streamlit as st
import streamlit.components.v1 as components
import base64

# ==============================
# CONFIGURACIÓN GENERAL
# ==============================
st.set_page_config(
    page_title="Interinspect",
    page_icon="🛠️",
    layout="wide"
)

# Inyectar CSS para forzar el fondo negro en toda la aplicación
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================
# CONTENEDOR DE PARTÍCULAS
# ==============================
particles_html = """
<div id="particles-js"></div>
<style>
#particles-js {
    position: relative;
    width: 100%;
    height: 200px; 
    background: #000000;
    margin-bottom: 0px;
    z-index: 1;
}
body {
    margin: 0;
}
</style>
<script src="https://cdn.jsdelivr.net/npm/particles.js"></script>
<script>
particlesJS("particles-js", {
    "particles": {
        "number": { "value": 80, "density": { "enable": true, "value_area": 800 } },
        "color": { "value": "#ffffff" },
        "shape": { "type": "circle" },
        "opacity": { "value": 0.5 },
        "size": { "value": 3 },
        "line_linked": { "enable": true, "distance": 150, "color": "#ffffff", "opacity": 0.4, "width": 1 },
        "move": { "enable": true, "speed": 2 }
    },
    "interactivity": {
        "detect_on": "canvas",
        "events": { "onhover": { "enable": true, "mode": "grab" } }
    },
    "retina_detect": true
});
</script>
"""

components.html(particles_html, height=200)

# ==============================
# TÍTULO Y TEXTO PERSONALIZADO
# ==============================

# Definimos el color azul solicitado
color_azul = "#6194C1"

st.markdown(f"""
    <div style="text-align: center; padding: 20px;">
        
    </div>
    """, unsafe_allow_html=True)

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
img_cx = get_base64("industry cx core.png")
img_et = get_base64("etapas.png")
img_min = get_base64("min.png")
img_ene = get_base64("ene.png")
img_gas = get_base64("gas.png")
img_man = get_base64("man.png")
img_agro = get_base64("agro.png")
img_met = get_base64("met.png")
img_fish = get_base64("fish.png")

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
    <h4 style="color: {color_azul}; font-size: 1.4rem; margin-bottom: 2px;">
        Transformación Digital Industrial
    </h4>
    <h1 style="color: white; font-weight: 400; margin-bottom: 5px;">
        Ecosistema Cognitivo para la Evolución Industrial Inteligente
    </h1>
    <p style="font-size: 1.2rem; line-height: 1.6; max-width: 900px; margin: 0 auto; color: #E0E0E0;">
        La transformación digital industrial ya no es un proyecto finito. Es una 
        <span style="color: {color_azul}; font-weight: bold;">mutación evolutiva del ADN organizacional</span>: 
        un proceso continuo donde la sensorización crítica, el análisis cognitivo, la prescripción operativa, 
        la monetización del riesgo y la maximización de rentabilidad operacional convergen en un organismo 
        inteligente que aprende de manera evolutiva.
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
# SECCIÓN: IDENTIDAD CORPORATIVA
# ==============================
st.markdown('<div id="identidad"></div>', unsafe_allow_html=True)

# Título de la sección CENTRADO
st.markdown(f"""
    <div style="text-align: center; margin-top: 50px; margin-bottom: 40px;">
        <h2 style="color: {color_azul}; font-size: 2.8rem; font-weight: 400; letter-spacing: 2px;">
            IDENTIDAD CORPORATIVA
        </h2>
    </div>
""", unsafe_allow_html=True)

# Creamos tres columnas para las tarjetas
col1, col2, col3 = st.columns(3)

# Estilo común para las tarjetas (se mantiene igual)
card_style = """
    background-color: #1E1E1E; /* Un gris un poco más profundo para resaltar el texto */
    padding: 35px;
    border-radius: 15px;
    height: 300px;
    border: 1px solid #333;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
"""

with col1:
    st.markdown(f"""
        <div style="{card_style}">
            <h2 style="color: white; font-weight: 400; margin-bottom: 25px; font-size: 1.8rem;">Quiénes Somos</h2>
            <p style="color: #CCCCCC; font-size: 1.1rem; line-height: 1.6; font-weight: 300;">
                Somos arquitectos de inteligencias industriales avanzadas. Diseñamos ecosistemas cognitivos 
                capaces de percibir, interpretar, adelantar escenarios, tomar decisiones y evolucionar junto a tu operación.
            </p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div style="{card_style}">
            <h2 style="color: white; font-weight: 400; margin-bottom: 25px; font-size: 1.8rem;">Nuestra Visión</h2>
            <p style="color: #CCCCCC; font-size: 1.1rem; line-height: 1.6; font-weight: 300;">
                Construir organizaciones industriales autónomas, resilientes y adaptativas, donde la cognición 
                técnica se convierte en ventaja competitiva.
            </p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div style="{card_style}">
            <h2 style="color: white; font-weight: 400; margin-bottom: 25px; font-size: 1.8rem;">Nuestro Propósito</h2>
            <p style="color: #CCCCCC; font-size: 1.1rem; line-height: 1.6; font-weight: 300;">
                Transformar industrias desde su estructura operativa y cultura organizacional, activando una 
                evolución continua basada en ciencia, ingeniería y aprendizaje automatizado.
            </p>
        </div>
    """, unsafe_allow_html=True)

# ==============================
# SECCIÓN: INDUSTRY-CX CORE
# ==============================
st.markdown('<div id="nucleo"></div>', unsafe_allow_html=True)

# Creamos dos columnas: izquierda para texto, derecha para imagen
col_text, col_img = st.columns(2, gap="large")

with col_text:
    st.markdown(f"""
        <div style="padding-top: 50px;">
            <h2 style="color: {color_azul}; font-size: 2.2rem; font-weight: 400; margin-bottom: 5px; letter-spacing: 1px;">
                INDUSTRY-CX CORE
            </h2>
            <h1 style="color: white; font-size: 3.2rem; font-weight: 600; margin-bottom: 30px; line-height: 1.1;">
               EL NÚCLEO COGNITIVO
            </h1>
            <p style="color: #CCCCCC; font-size: 1.15rem; line-height: 1.6; margin-bottom: 25px;">
                INDUSTRY-CX CORE es ese organismo cognitivo que evoluciona contigo, con tus procesos, con tus mercados y con tu cultura técnica-organizacional.
            </p>
            <p style="color: white; font-weight: bold; margin-bottom: 20px;">Un organismo inteligente capaz de:</p>
            <ul style="list-style-type: none; padding-left: 0;">
                <li style="margin-bottom: 12px; color: #CCCCCC;">
                    <span style="color: {color_azul}; font-weight: bold;">• Percibir</span> → Sensorización, telemetría, datos operativos IIoT, 3D, imágenes, NDT
                </li>
                <li style="margin-bottom: 12px; color: #CCCCCC;">
                    <span style="color: {color_azul}; font-weight: bold;">• Integrar</span> → Fusión multimodal (modelos físicos + ML)
                </li>
                <li style="margin-bottom: 12px; color: #CCCCCC;">
                    <span style="color: {color_azul}; font-weight: bold;">• Analizar</span> → Diagnóstico + simulación + predicción + prescripción
                </li>
                <li style="margin-bottom: 12px; color: #CCCCCC;">
                    <span style="color: {color_azul}; font-weight: bold;">• Actuar</span> → Automatización de workflows y toma de decisiones
                </li>
                <li style="margin-bottom: 12px; color: #CCCCCC;">
                    <span style="color: {color_azul}; font-weight: bold;">• Aprender</span> → Ajuste continuo del sistema
                </li>
                <li style="margin-bottom: 30px; color: #CCCCCC;">
                    <span style="color: {color_azul}; font-weight: bold;">• Monetizar</span> → VaRO (Value at Risk Operational), CEIP (Costo Esperado de Interrupción de Producción), OPEX (Operational Expenditure)
                </li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Botón blanco estilo la imagen
    st.markdown(f"""
        <a href="#" style="
            background-color: white; 
            color: black; 
            padding: 12px 30px; 
            border-radius: 5px; 
            text-decoration: none; 
            font-weight: bold;
            display: inline-block;
            transition: 0.3s;
        ">Conocer el Núcleo Cognitivo</a>
    """, unsafe_allow_html=True)

with col_img:
    # Mostramos la imagen cargada (img_cx)
    # Asumiendo que img_cx es el base64 de la imagen que mencionaste
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 90%;">
            <img src="data:image/png;base64,{img_cx}" style="width: 100%; border-radius: 10px; box-shadow: 0px 0px 30px rgba(97, 148, 193, 0.2);">
        </div>
    """, unsafe_allow_html=True)
    
# ==============================
# SECCIÓN: ARQUITECTURA COGNITIVA
# ==============================
st.markdown('<div id="arquitectura"></div>', unsafe_allow_html=True)

# Título de la sección centrado
st.markdown(f"""
    <div style="text-align: center; margin-top: 40px; margin-bottom: 20px;">
        <h2 style="color: {color_azul}; font-size: 2.5rem; font-weight: 400; letter-spacing: 1px;">
            INDUSTRY-CX CORE: Arquitectura Cognitiva de Seis Etapas
        </h2>
    </div>
""", unsafe_allow_html=True)

# Contenedor para la imagen img_et
st.markdown(f"""
    <div style="display: flex; justify-content: center; padding: 0 10% 10px 10%;">
        <img src="data:image/png;base64,{img_et}" style="width: 100%; max-width: 1200px; border-radius: 15px; box-shadow: 0px 10px 30px rgba(0,0,0,0.5);">
    </div>
""", unsafe_allow_html=True)

# ==============================
# SECCIÓN: ARQUITECTURA DEL SISTEMA - INSTRUMENTACIÓN
# ==============================
st.markdown('<div id="instrumentacion"></div>', unsafe_allow_html=True)

# Encabezado alineado a la izquierda como en la imagen
st.markdown(f"""
    <div style="padding-left: 10px; margin-top:10px; margin-bottom: 10px;">
        <h4 style="color: {color_azul}; font-size: 1.5rem; font-weight: 300; margin-bottom: 5px;">
            Arquitectura del Sistema
        </h4>
        <h1 style="color: white; font-size: 3.2rem; font-weight: 600;">
            Instrumentación
        </h1>
    </div>
""", unsafe_allow_html=True)

# Tres columnas para las capas
col_sensores, col_procesamiento, col_inteligencia = st.columns(3)

# Estilo para los items de la lista
li_style = f"margin-bottom: 8px; color: #CCCCCC; font-size: 1.05rem; list-style-type: none;"
bullet = f"<span style='color: {color_azul}; font-weight: bold; margin-right: 10px;'>•</span>"

with col_sensores:
    st.markdown(f"""
        <div style="padding: 0 40px;">
            <h3 style="color: {color_azul}; font-size: 1.4rem; font-weight: 400; margin-bottom: 25px;">Capa de Sensores</h3>
            <ul style="padding-left: 0;">
                <li style="{li_style}">{bullet} IIoT multisensor (vibración, presión, caudal, energía)</li>
                <li style="{li_style}">{bullet} NDT avanzado (UT/PAUT, EMAT, AE, MFL, LRUT)</li>
                <li style="{li_style}">{bullet} Termografía IR (dron + fija + portátil)</li>
                <li style="{li_style}">{bullet} Geotecnia cognitiva (piezómetros, fibra óptica)</li>
                <li style="{li_style}">{bullet} Visión computacional industrial</li>
                <li style="{li_style}">{bullet} LIDAR 3D</li>
                <li style="{li_style}">{bullet} Integración OT/IT (SCADA, DCS, PLC)</li>
                <li style="{li_style}">{bullet} Edge AI + Cloud ML</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col_procesamiento:
    st.markdown(f"""
        <div style="padding: 0 40px;">
            <h3 style="color: {color_azul}; font-size: 1.4rem; font-weight: 400; margin-bottom: 25px;">Capa de Procesamiento</h3>
            <ul style="padding-left: 0;">
                <li style="{li_style}">{bullet} Gateways de datos OT/IT</li>
                <li style="{li_style}">{bullet} GPU/TPU para entrenamiento ML</li>
                <li style="{li_style}">{bullet} Motor prescriptivo con reglas sectoriales</li>
                <li style="{li_style}">{bullet} Gemelos cognitivos (físico + estadístico + ML)</li>
                <li style="{li_style}">{bullet} Dashboards 3D interactivos</li>
                <li style="{li_style}">{bullet} Integración con IA agéntica</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col_inteligencia:
    st.markdown(f"""
        <div style="padding: 0 40px;">
            <h3 style="color: {color_azul}; font-size: 1.4rem; font-weight: 400; margin-bottom: 25px;">Capa de Inteligencia</h3>
            <ul style="padding-left: 0;">
                <li style="{li_style}">{bullet} Arquitectura híbrida Cloud–Edge</li>
                <li style="{li_style}">{bullet} Algoritmos ML + modelos físicos</li>
                <li style="{li_style}">{bullet} Pipelines n8n industriales</li>
                <li style="{li_style}">{bullet} Integración multiprotocolo (OPC-UA, MQTT, REST)</li>
                <li style="{li_style}">{bullet} Repositorios sectoriales de inteligencia</li>
                <li style="{li_style}">{bullet} Núcleo cognitivo INDUSTRY-CX CORE</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
# ==============================
# SECCIÓN: EXPLORAR POR INDUSTRIA
# ==============================
st.markdown('<div id="industria"></div>', unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align: center; margin-top: 60px; margin-bottom: 60px; padding: 0 20px;">
    <h4 style="color: {color_azul}; font-size: 1.3rem; font-weight: 300; margin-bottom: 10px; letter-spacing: 1px;">
        Soluciones Especializadas
    </h4>
    <h1 style="color: white; font-size: 4.5rem; font-weight: 600; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 3px; line-height: 1.1;">
        EXPLORAR POR INDUSTRIA
    </h1>
    <h3 style="color: white; font-size: 2rem; font-weight: 400; margin-bottom: 20px;">
        Motores Cognitivos Sectoriales (Industrial Cognitive Engines)
    </h3>
    <p style="color: #CCCCCC; font-size: 1.2rem; max-width: 850px; margin: 0 auto; line-height: 1.5; font-weight: 300;">
        Cada industria posee un ADN operativo distinto. Nuestros motores cognitivos se adaptan a esa estructura.
    </p>
</div>
""", unsafe_allow_html=True)

# ==============================
# SECCIÓN: MINERÍA (MINEX-IN CORE)
# ==============================
st.markdown('<div id="mineria"></div>', unsafe_allow_html=True)

# Usamos columnas 1:1 para un equilibrio visual perfecto
col_img_min, col_text_min = st.columns(2, gap="large")

with col_img_min:
    # Mostramos la imagen img_min
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="data:image/png;base64,{img_min}" style="width: 100%; border-radius: 15px; box-shadow: 0px 5px 25px rgba(0,0,0,0.5);">
        </div>
    """, unsafe_allow_html=True)

with col_text_min:
    st.markdown(f"""
        <div style="padding-top: 60px;">
            <h1 style="font-size: 2.8rem; font-weight: 600; line-height: 1.2; margin-bottom: 25px;">
                <span style="color: {color_azul};">MINEX-IN CORE</span> <span style="color: white;">— Minería</span>
            </h1>
            <p style="color: #CCCCCC; font-size: 1.2rem; line-height: 1.6; margin-bottom: 35px;">
                Integridad predictiva, metalurgia inteligente, geotecnia cognitiva y optimización de plantas concentradoras.
            </p>
            <a href="#" style="
                background-color: white; 
                color: black; 
                padding: 12px 30px; 
                border-radius: 5px; 
                text-decoration: none; 
                font-weight: bold;
                display: inline-block;
                transition: 0.3s;
            ">Conocer el MINEX-IN COR</a>
        </div>
    """, unsafe_allow_html=True)
    
    
# ==============================
# SECCIÓN: ENERGÍA (ENERG-IN CORE)
# ==============================
st.markdown('<div id="energia"></div>', unsafe_allow_html=True)

# INVERTIMOS EL ORDEN: Primero el texto (izquierda) y luego la imagen (derecha)
col_text_ene, col_img_ene = st.columns(2, gap="large")

with col_text_ene:
    st.markdown(f"""
        <div style="
            display: flex; 
            flex-direction: column; 
            justify-content: center; 
            height: 100%;
            min-height: 400px;
            padding-left: 50px; /* Un poco de margen desde el borde izquierdo */
        ">
            <h1 style="font-size: 2.8rem; font-weight: 600; line-height: 1.2; margin-bottom: 25px;">
                <span style="color: {color_azul};">ENERG-IN CORE</span> <span style="color: white;">— Energía</span>
            </h1>
            <p style="color: #CCCCCC; font-size: 1.2rem; line-height: 1.6; margin-bottom: 35px;">
                Eficiencia energética, integridad térmica, redes inteligentes y detección temprana de fallas eléctricas.
            </p>
            <div>
                <a href="#" style="
                    background-color: white; 
                    color: black; 
                    padding: 12px 30px; 
                    border-radius: 5px; 
                    text-decoration: none; 
                    font-weight: bold;
                    display: inline-block;
                    transition: 0.3s;
                ">Conocer el ENERG-IN COR</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_img_ene:
    # La imagen img_ene ahora queda en la columna de la derecha
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="data:image/png;base64,{img_ene}" style="width: 100%; border-radius: 15px; box-shadow: 0px 5px 25px rgba(0,0,0,0.5);">
        </div>
    """, unsafe_allow_html=True)
    
# ==============================
# SECCIÓN: OIL & GAS (OIL-IN CORE)
# ==============================
st.markdown('<div id="oilgas"></div>', unsafe_allow_html=True)

# Usamos columnas 1:1 para un equilibrio visual perfecto
col_img_gas, col_text_gas = st.columns(2, gap="large")

with col_img_gas:
    # Mostramos la imagen img_min
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="data:image/png;base64,{img_gas}" style="width: 100%; border-radius: 15px; box-shadow: 0px 5px 25px rgba(0,0,0,0.5);">
        </div>
    """, unsafe_allow_html=True)

with col_text_gas:
    st.markdown(f"""
        <div style="padding-top: 60px;">
            <h1 style="font-size: 2.8rem; font-weight: 600; line-height: 1.2; margin-bottom: 25px;">
                <span style="color: {color_azul};">OIL & GAS-IN CORE</span> <span style="color: white;">— Oil & Gas</span>
            </h1>
            <p style="color: #CCCCCC; font-size: 1.2rem; line-height: 1.6; margin-bottom: 35px;">
                Integridad Estructural API, gestion de la corrosión, RBI 580/581 Inspeccion basada en Riesgo, detección temprana y prediccón de fallas críticas en tuberías, tanques y sistemas presurizados.
            </p>
            <a href="#" style="
                background-color: white; 
                color: black; 
                padding: 12px 30px; 
                border-radius: 5px; 
                text-decoration: none; 
                font-weight: bold;
                display: inline-block;
                transition: 0.3s;
            ">Conocer el OIL & GAS-IN COR</a>
        </div>
    """, unsafe_allow_html=True)

# ==============================
# SECCIÓN: MANUFACTURA (MANUF-IN CORE)
# ==============================
st.markdown('<div id="manufactura"></div>', unsafe_allow_html=True)

# Mantenemos el orden: Texto a la izquierda, Imagen a la derecha
col_text_man, col_img_man = st.columns(2, gap="large")

with col_text_man:
    st.markdown(f"""
        <div style="
            display: flex; 
            flex-direction: column; 
            justify-content: center; 
            height: 100%;
            padding-left: 50px;
        ">
            <h1 style="font-size: 2.8rem; font-weight: 600; line-height: 1.2; margin-bottom: 20px;">
                <span style="color: {color_azul};">MANUF-IN CORE</span> <span style="color: white;">— Manufactura</span>
            </h1>
            <p style="color: #CCCCCC; font-size: 1.2rem; line-height: 1.6; margin-bottom: 20px;">
                OEE cognitivo, scrap cero, computer vision para calidad y líneas autónomas.
            </p>
            <ul style="list-style-type: none; padding-left: 0; margin-bottom: 35px;">
                <li style="color: #CCCCCC; margin-bottom: 10px;">
                    <span style="color: {color_azul}; margin-right: 10px;">•</span> cámaras industriales 4K
                </li>
                <li style="color: #CCCCCC; margin-bottom: 10px;">
                    <span style="color: {color_azul}; margin-right: 10px;">•</span> sensores de vibración/acústica
                </li>
                <li style="color: #CCCCCC; margin-bottom: 10px;">
                    <span style="color: {color_azul}; margin-right: 10px;">•</span> sistemas robotizados
                </li>
                <li style="color: #CCCCCC; margin-bottom: 10px;">
                    <span style="color: {color_azul}; margin-right: 10px;">•</span> espectroscopía de inspección
                </li>
                <li style="color: #CCCCCC; margin-bottom: 10px;">
                    <span style="color: {color_azul}; margin-right: 10px;">•</span> PLC + IIoT assembly line
                </li>
            </ul>      
            <div>
                <a href="#" style="
                    background-color: white; 
                    color: black; 
                    padding: 12px 30px; 
                    border-radius: 5px; 
                    text-decoration: none; 
                    font-weight: bold;
                    display: inline-block;
                ">Conocer MAFUF-IN COR</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_img_man:
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="data:image/png;base64,{img_man}" style="width: 100%; border-radius: 15px; box-shadow: 0px 5px 25px rgba(0,0,0,0.5);">
        </div>
    """, unsafe_allow_html=True)
    
# ==============================
# SECCIÓN: AGRO (AGRO-IN CORE)
# ==============================
st.markdown('<div id="agro"></div>', unsafe_allow_html=True)

# Usamos columnas 1:1 para un equilibrio visual perfecto
col_img_agro, col_text_agro = st.columns(2, gap="large")

with col_img_agro:
    # Mostramos la imagen img_min
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="data:image/png;base64,{img_agro}" style="width: 100%; border-radius: 15px; box-shadow: 0px 5px 25px rgba(0,0,0,0.5);">
        </div>
    """, unsafe_allow_html=True)

with col_text_agro:
    st.markdown(f"""
        <div style="padding-top: 60px;">
            <h1 style="font-size: 2.8rem; font-weight: 600; line-height: 1.2; margin-bottom: 25px;">
                <span style="color: {color_azul};">AGRO-IN CORE</span> <span style="color: white;">— Agroindustria</span>
            </h1>
            <p style="color: #CCCCCC; font-size: 1.2rem; line-height: 1.6; margin-bottom: 35px;">
                IA climática, eficiencia hídrica, trazabilidad blockchain, control de plagas.
            </p>
            <a href="#" style="
                background-color: white; 
                color: black; 
                padding: 12px 30px; 
                border-radius: 5px; 
                text-decoration: none; 
                font-weight: bold;
                display: inline-block;
                transition: 0.3s;
            ">Conocer el AGRO-IN COR</a>
        </div>
    """, unsafe_allow_html=True)

# ==============================
# SECCIÓN: MMETALURGIA (MET-IN CORE)
# ==============================
st.markdown('<div id="metalurgia"></div>', unsafe_allow_html=True)

# Mantenemos el orden: Texto a la izquierda, Imagen a la derecha
col_text_met, col_img_met = st.columns(2, gap="large")

with col_text_met:
    st.markdown(f"""
        <div style="padding-top: 60px;">
            <h1 style="font-size: 2.8rem; font-weight: 600; line-height: 1.2; margin-bottom: 25px;">
                <span style="color: {color_azul};">METAL-IN CORE</span> <span style="color: white;">— Metalurgía (extractiva + física)</span>
            </h1>
            <p style="color: #CCCCCC; font-size: 1.2rem; line-height: 1.6; margin-bottom: 35px;">
                Hornos inteligentes, fundición optimizada, refinación predictiva, laminación controlada.
            </p>
            <a href="#" style="
                background-color: white; 
                color: black; 
                padding: 12px 30px; 
                border-radius: 5px; 
                text-decoration: none; 
                font-weight: bold;
                display: inline-block;
                transition: 0.3s;
            ">Conocer el METAL-IN COR</a>
        </div>
    """, unsafe_allow_html=True)

with col_img_met:
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="data:image/png;base64,{img_met}" style="width: 100%; border-radius: 15px; box-shadow: 0px 5px 25px rgba(0,0,0,0.5);">
        </div>
    """, unsafe_allow_html=True)
    
# ==============================
# SECCIÓN: PESCA (FISH-IN CORE)
# ==============================
st.markdown('<div id="agro"></div>', unsafe_allow_html=True)

# Usamos columnas 1:1 para un equilibrio visual perfecto
col_img_agro, col_text_agro = st.columns(2, gap="large")

with col_img_agro:
    # Mostramos la imagen img_min
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="data:image/png;base64,{img_fish}" style="width: 100%; border-radius: 15px; box-shadow: 0px 5px 25px rgba(0,0,0,0.5);">
        </div>
    """, unsafe_allow_html=True)

with col_text_agro:
    st.markdown(f"""
        <div style="padding-top: 60px;">
            <h1 style="font-size: 2.8rem; font-weight: 600; line-height: 1.2; margin-bottom: 25px;">
                <span style="color: {color_azul};">ARQUITECTURA COGNITIVA FISH-IN CORE</span>
            </h1>
            <p style="color: #CCCCCC; font-size: 1.2rem; line-height: 1.6; margin-bottom: 35px;">
                Sistema INTELIGENTE para pesca industrial, predicción de biomasa, control de flota y calidad pesquera
            </p>
            <a href="#" style="
                background-color: white; 
                color: black; 
                padding: 12px 30px; 
                border-radius: 5px; 
                text-decoration: none; 
                font-weight: bold;
                display: inline-block;
                transition: 0.3s;
            ">Conocer el FISH-IN COR</a>
        </div>
    """, unsafe_allow_html=True)
