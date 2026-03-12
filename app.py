import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from streamlit_lottie import st_lottie
import json

# -------- Cargar animación --------
def load_lottie_file(filepath):
    with open(filepath, "rb") as f:
        data = f.read().decode("utf-8", errors="ignore")
        return json.loads(data)

animation = load_lottie_file("emoji_animation.json")

# -------- Interfaz --------
st_lottie(animation, height=250)

st.title("Análisis de Sentimiento")
st.subheader("Escribe una frase para analizar su sentimiento")

translator = Translator()

# -------- Sidebar informativa --------
with st.sidebar:
    st.subheader("Polaridad y Subjetividad")

    st.write("""
    **Polaridad:** indica si el sentimiento del texto es positivo, negativo o neutral.  
    Va desde **-1 (muy negativo)** hasta **1 (muy positivo)**.

    **Subjetividad:** mide cuánto del texto es opinión o emoción.  
    Va de **0 (objetivo)** a **1 (subjetivo)**.
    """)

# -------- Entrada de texto --------
with st.expander("Analizar texto"):

    text = st.text_input("Escribe una frase:")

    if text:

        # traducir a inglés para el análisis
        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text

        blob = TextBlob(trans_text)

        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.write("**Polaridad:**", polarity)
        st.write("**Subjetividad:**", subjectivity)

        # -------- Interacción según sentimiento --------
        if polarity > 0:
            st.success("Sentimiento POSITIVO 😊")
            st.balloons()

        elif polarity < 0:
            st.error("Sentimiento NEGATIVO 😔")
            st.snow()

        else:
            st.info("Sentimiento NEUTRAL 😐")
