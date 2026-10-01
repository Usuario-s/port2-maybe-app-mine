import streamlit as st
from streamlit_drawable_canvas import st_canvas

# =========================
# CONFIGURACIÓN DE PÁGINA
# =========================
st.set_page_config(
    page_title="Tablero Cavernícola",
    page_icon="🪨",
    layout="wide"
)

# =========================
# ESTILO CAVERNÍCOLA
# =========================
st.markdown("""
<style>

    /* Fondo general */
    .stApp {
        background-color: #241812;
        color: #E6D2B5;
    }

    /* Título */
    h1 {
        color: #D8B98A !important;
        text-align: center;
        font-family: Georgia, serif;
        font-size: 42px !important;
        text-shadow: 3px 3px 0px #120C08;
        letter-spacing: 2px;
    }

    /* Subtítulos */
    h2, h3 {
        color: #C69C6D !important;
        font-family: Georgia, serif;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #302017;
        border-right: 3px solid #5A3A25;
    }

    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #D8B98A !important;
        font-family: Georgia, serif;
    }

    /* Texto */
    label, .stMarkdown {
        color: #D9C2A3 !important;
    }

    /* Sliders */
    div[data-baseweb="slider"] {
        margin-bottom: 10px;
    }

    /* Selectbox */
    div[data-baseweb="select"] > div {
        background-color: #3A281C;
        border: 2px solid #705039;
        color: #E6D2B5;
    }

    /* Color pickers */
    div[data-testid="stColorPicker"] {
        background-color: #302017;
        border-radius: 8px;
    }

    /* Efecto de marco alrededor del tablero */
    .canvas-container {
        background-color: #463022;
        padding: 18px;
        border: 8px solid #5A3A25;
        border-radius: 18px;
        box-shadow:
            inset 0 0 20px #1A0F09,
            0 8px 20px #120B07;
    }

    /* Separadores */
    hr {
        border-color: #63452E;
    }

    /* Botones */
    button {
        background-color: #5A3A25 !important;
        color: #E6D2B5 !important;
        border: 2px solid #8A6747 !important;
    }

</style>
""", unsafe_allow_html=True)


# =========================
# TÍTULO
# =========================

st.title("🪨 Tablero de Pintura Cavernícola")

st.markdown(
    "<p style='text-align:center; color:#A98763; font-family:Georgia;'>"
    "Dibuja como en las paredes de una antigua caverna"
    "</p>",
    unsafe_allow_html=True
)


# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.subheader("🪨 Propiedades del Tablero")

    st.markdown("---")

    st.subheader("📐 Dimensiones del Tablero")

    canvas_width = st.slider(
        "Ancho del tablero",
        300,
        700,
        500,
        50
    )

    canvas_height = st.slider(
        "Alto del tablero",
        200,
        600,
        300,
        50
    )

    st.markdown("---")

    st.subheader("🖌️ Herramientas")

    drawing_mode = st.selectbox(
        "Herramienta de Dibujo:",
        (
            "freedraw",
            "line",
            "rect",
            "circle",
            "transform",
            "polygon",
            "point"
        )
    )

    stroke_width = st.slider(
        "Ancho de línea",
        1,
        30,
        15
    )

    stroke_color = st.color_picker(
        "Color de trazo",
        "#D8B98A"
    )

    bg_color = st.color_picker(
        "Color de fondo",
        "#3B2920"
    )


# =========================
# TABLERO
# =========================

st.markdown(
    '<div class="canvas-container">',
    unsafe_allow_html=True
)

canvas_result = st_canvas(
    fill_color="rgba(170, 120, 70, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)
