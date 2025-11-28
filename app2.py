import streamlit as st
import base64
import streamlit.components.v1 as components

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
# CONFIGURACIÓN GENERAL
# ==============================
st.set_page_config(
    page_title="Interinspect",
    page_icon="🛠️",
    layout="wide"
)

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
     <img src="data:image/jpeg;base64,{img_pt}" style="width:500px; height:290px; border-radius:20px; object-fit:cover; margin-bottom:20px;" />
    <h1 style="font-size:52px; font-weight:bold;">Bienvenido</h1>
    <p style="font-size:22px; margin-top:8px;">
        La evolución de tu industria comienza aquí.<br>
        Desde los retos actuales de optimización hacia un futuro digital <br>
        inteligente y el control completo del negocio.
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
        <div class="about-us-title">Sobre Nosotros</div>
        <p>Somos un ecosistema innovador que une tecnología avanzada y pasión por transformar procesos industriales y PYMES, construyendo un futuro sustentable e inteligente.</p>
        <p>Creemos que la digitalización es una evolución necesaria, accesible y poderosa para quienes buscan eficiencia, seguridad y sostenibilidad.</p>
        <p>Queremos ser tu socio estratégico en cada paso de la transformación, entregando soluciones escalables, personalizadas y basadas en inteligencia real.<p>
    </div>
</div>
""", unsafe_allow_html=True)

# ==============================
# SECCIÓN: EXPLORA POR INDUSTRIA
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
    <div class="industry-title">Explora por Industria</div>
    <div class="industry-intro">
        Cada industria tiene sus particularidades. Aquí te mostramos las soluciones que transforman tu sector.
    </div>
    <div class="industry-grid">
        <div class="industry-card">
            <div class="industry-name">Minería y Metalurgia Extractiva</div>
            <div class="industry-description">Monitoreo avanzado, trazabilidad, análisis predictivo y seguridad operacional.</div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Metalurgia Física</div>
            <div class="industry-description">Ensayos, caracterización, control de calidad y optimización de procesos metalúrgicos.</div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Energía</div>
            <div class="industry-description">Redes inteligentes, eficiencia energética y soluciones integradas de gestión.</div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Hidrocarburos</div>
            <div class="industry-description"> Integridad de activos, operación segura y monitoreo en tiempo real.</div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Agroindustria</div>
            <div class="industry-description">Trazabilidad, control ambiental, manejo hídrico y gestión de calidad.</div>
        </div>
        <div class="industry-card">
            <div class="industry-name">Manufactura</div>
            <div class="industry-description">Automatización modular, control de procesos y eficiencia operativa continua.</div>
        </div>        
    </div>
    <div class="industry-footer">
        Visualiza la solución que transforma tu operación y acerca el futuro a tu realidad.
    </div>
</div>
""", unsafe_allow_html=True)

# ==============================
# SECCIÓN: EXPLORA POR SERVICIOS
# ==============================
st.markdown('<div id="servicios" style="margin-top:20px;"></div>', unsafe_allow_html=True)
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
    <div class="services-title">Explora por Servicios</div>
    <div class="services-intro">
        Desde servicios amigables para empezar tu transformación, hasta innovaciones disruptivas para liderar el mercado.
    </div>
    <div class="services-grid">
        <div class="services-card">
            <div class="services-name">Monitoreo básico</div>
        </div>
        <div class="services-card">
            <div class="services-name">Monitoreo avanzado</div>
        </div>
        <div class="services-card">
            <div class="services-name">Mantenimiento predictivo inteligente</div>
        </div>
        <div class="services-card">
            <div class="services-name">Data analitics</div>
        </div>
        <div class="services-card">
            <div class="services-name">Digital Twins y simulación</div>
        </div>
        <div class="services-card">
            <div class="services-name">IA agéntica y edge AI</div>
        </div>
        <div class="services-card">
            <div class="services-name">Blockchain y economía circular</div>
        </div>
        <div class="services-card">
            <div class="services-name">Formación y acompañamiento</div>
        </div>
    </div>
    <div class="services-footer">
        ¿Quieres probar cómo estas soluciones pueden impactar en tu negocio? Simula tu evolución aquí.
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
    <div class="timeline-title">Proceso de Valor</div>
    <div class="timeline-intro">
        Tu transformación digital se hace paso a paso, con acompañamiento experto y resultados medibles.
    </div>
    <div class="timeline-container">
        <div class="timeline-line"></div>
        <div class="phase-card">
            <div class="phase-name">Descubrimiento y diagnóstico</div>
            <div class="phase-description">Analizamos tu operación y detectamos oportunidades de mejora.</div>
        </div>
        <div class="phase-card">
            <div class="phase-name">Pilotaje y prueba de concepto</div>
            <div class="phase-description">Implementamos soluciones a pequeña escala para validar impacto.</div>
        </div>
        <div class="phase-card">
            <div class="phase-name">Escalabilidad progresiva</div>
            <div class="phase-description">Extendemos las soluciones a toda la operación de manera segura y controlada.</div>
        </div>
        <div class="phase-card">
            <div class="phase-name">Innovación continua y co-creación</div>
            <div class="phase-description">Mejoramos continuamente con tu feedback y nuevas tecnologías.</div>
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
