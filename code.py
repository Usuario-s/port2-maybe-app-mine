import streamlit as st
from streamlit_drawable_canvas import st_canvas

# =========================
# CONFIGURACIÓN
# =========================

st.set_page_config(
    page_title="Tablero de SUM",
    page_icon="🪨",
    layout="wide"
)

# =========================
# ESTILO RÚSTICO / CAVERNÍCOLA
# =========================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 20% 20%, #4a3423 0%, transparent 25%),
        radial-gradient(circle at 80% 70%, #3b281b 0%, transparent 30%),
        #21150e;
    color: #d8bd91;
}

/* Título */
h1 {
    color: #c9a875 !important;
    font-family: Georgia, serif !important;
    font-size: 46px !important;
    text-align: center;
    letter-spacing: 4px;
    text-transform: uppercase;
    text-shadow:
        3px 3px 0px #120b07,
        -1px -1px 0px #6b4b2d;
}

/* Subtítulo */
.subtitulo {
    text-align: center;
    color: #8f704b;
    font-family: Georgia, serif;
    font-style: italic;
    margin-top: -15px;
    margin-bottom: 25px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            145deg,
            #352318,
            #24160e
        );
    border-right: 6px solid #4f3522;
    box-shadow: 5px 0px 15px #100a06;
}

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #c9a875 !important;
    font-family: Georgia, serif !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Texto */
label {
    color: #c4a77d !important;
    font-family: Georgia, serif !important;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    background-color: #2b1c12;
    border: 2px solid #67472b;
    color: #d8bd91;
}

/* Separadores */
hr {
    border: none;
    border-top: 3px solid #533720;
    margin: 20px 0;
}

/* Marco del tablero */
.canvas-frame {
    padding: 22px;
    background:
        linear-gradient(
            135deg,
            #60452e,
            #392619,
            #523a25
        );
    border: 10px solid #2a1a10;
    border-radius: 8px;
    box-shadow:
        inset 0 0 0 4px #806142,
        inset 0 0 25px #160d08,
        0 12px 25px #100905;
}

/* Rótulo TABLERO DE SUM */
.stone-title {
    display: inline-block;
    padding: 12px 28px;
    margin-bottom: 18px;

    background: #4a3423;

    border-top: 4px solid #76583a;
    border-left: 4px solid #694b30;
    border-right: 4px solid #2a1a10;
    border-bottom: 6px solid #21130b;

    color: #c9ad7e;

    font-family: Georgia, serif;
    font-size: 22px;
    font-weight: bold;
    letter-spacing: 3px;

    text-shadow:
        2px 2px 0px #1c1009;

    transform: rotate(-1deg);
}

</style>
""", unsafe_allow_html=True)


# =========================
# ENCABEZADO
# =========================

st.markdown(
    '<div class="stone-title">🪨 TABLERO DE SUM</div>',
    unsafe_allow_html=True
)

st.title("Tablero para dibujo")

st.markdown(
    '<div class="subtitulo">'
    'Pinta, dibuja y deja tu marca en la piedra'
    '</div>',
    unsafe_allow_html=True
)


# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.subheader("🪨 Propiedades del tablero")

    st.markdown("---")

    st.subheader("Dimensiones")

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

    st.subheader("Herramientas")

    drawing_mode = st.selectbox(
        "Herramienta de dibujo:",
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
        "#D2B48C"
    )

    bg_color = st.color_picker(
        "Color de fondo",
        "#3A291C"
    )


# =========================
# TABLERO
# =========================

st.markdown(
    '<div class="canvas-frame">',
    unsafe_allow_html=True
)

canvas_result = st_canvas(
    fill_color="rgba(139, 94, 52, 0.35)",
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
