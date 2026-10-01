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

/* =========================
   TÍTULO PRINCIPAL
   ========================= */

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

/* =========================
   SIDEBAR
   ========================= */

section[data-testid="stSidebar"] {
    background:
        radial-gradient(
            circle at 30% 20%,
            #513924 0%,
            transparent 35%
        ),
        linear-gradient(
            160deg,
            #362419,
            #21140d
        );

    border-right: 8px solid #4b301d;

    box-shadow:
        8px 0px 20px #0e0805,
        inset -3px 0px 0px #6b4b2e;
}

/* =========================
   PLACA "PROPIEDADES"
   ========================= */

.propiedades {
    background:
        linear-gradient(
            145deg,
            #60452e,
            #3b281b
        );

    padding: 18px 15px;

    margin: 5px 0 20px 0;

    border-radius: 6px;

    border-top: 4px solid #806142;
    border-left: 4px solid #765437;
    border-right: 5px solid #24150d;
    border-bottom: 7px solid #1c1009;

    box-shadow:
        inset 0 0 15px #24150d,
        0 5px 10px #120a06;

    transform: rotate(-0.5deg);
}

.propiedades-titulo {
    color: #d5b47e;

    font-family: Georgia, serif;

    font-size: 21px;

    font-weight: bold;

    text-align: center;

    text-transform: uppercase;

    letter-spacing: 2px;

    text-shadow:
        2px 2px 0px #1b0f08;
}

/* =========================
   SECCIONES
   ========================= */

.seccion {
    background: #2b1c12;

    padding: 10px;

    margin: 12px 0;

    border-left: 4px solid #765437;

    border-bottom: 2px solid #513720;

    box-shadow:
        inset 0 0 8px #160c07;
}

.seccion-titulo {
    color: #bd9664;

    font-family: Georgia, serif;

    font-size: 14px;

    font-weight: bold;

    text-transform: uppercase;

    letter-spacing: 1.5px;

    margin-bottom: 5px;
}

/* =========================
   TEXTO
   ========================= */

label {
    color: #c9ad7e !important;
    font-family: Georgia, serif !important;
}

/* =========================
   SELECTBOX
   ========================= */

div[data-baseweb="select"] > div {
    background-color: #24170e;

    border: 2px solid #68472b;

    color: #d8bd91;

    border-radius: 3px;

    box-shadow:
        inset 0 0 6px #130a05;
}

/* =========================
   SLIDERS
   ========================= */

div[data-testid="stSlider"] {
    color: #c9a875;
}

/* =========================
   COLOR PICKERS
   ========================= */

div[data-testid="stColorPicker"] {
    background: #2b1c12;

    border: 2px solid #513720;

    border-radius: 4px;

    padding: 5px;

    box-shadow:
        inset 0 0 7px #160c07;
}

/* =========================
   SEPARADORES
   ========================= */

hr {
    border: none;

    border-top: 3px solid #513720;

    margin: 18px 0;
}

/* =========================
   MARCO DEL TABLERO
   ========================= */

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

/* =========================
   RÓTULO TABLERO DE SUM
   ========================= */

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

    # Placa principal
    st.markdown("""
    <div class="propiedades">
        <div class="propiedades-titulo">
            🪨 Propiedades<br>
            del Tablero
        </div>
    </div>
    """, unsafe_allow_html=True)


    # =========================
    # DIMENSIONES
    # =========================

    st.markdown("""
    <div class="seccion">
        <div class="seccion-titulo">
            📐 Tamaño de la piedra
        </div>
    </div>
    """, unsafe_allow_html=True)

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


    # =========================
    # HERRAMIENTAS
    # =========================

    st.markdown("""
    <div class="seccion">
        <div class="seccion-titulo">
            🪵 Herramientas de grabado
        </div>
    </div>
    """, unsafe_allow_html=True)

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
        "Grosor del grabado",
        1,
        30,
        15
    )


    # =========================
    # COLORES
    # =========================

    st.markdown("""
    <div class="seccion">
        <div class="seccion-titulo">
            🎨 Pigmentos
        </div>
    </div>
    """, unsafe_allow_html=True)

    stroke_color = st.color_picker(
        "Color del trazo",
        "#D2B48C"
    )

    bg_color = st.color_picker(
        "Color de la piedra",
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
