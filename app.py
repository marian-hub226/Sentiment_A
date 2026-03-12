from textblob import TextBlob
import streamlit as st
from googletrans import Translator
import json
from streamlit_lottie import st_lottie

# Cargar animación
with open("emoji_animation.json", "rb") as f:
    animation = json.load(f)

st_lottie(animation, height=250)

st.title("Análisis de Sentimiento")

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

translator = Translator()

# Sidebar explicativa
with st.sidebar:
    st.subheader("Polaridad y Subjetividad")

    st.write("""
    **Polaridad:** indica si el sentimiento es positivo, negativo o neutral.  
    Va de **-1 (muy negativo)** a **1 (muy positivo)**.

    **Subjetividad:** mide si el texto expresa opinión o hechos.  
    Va de **0 (objetivo)** a **1 (subjetivo)**.
    """)

# Entrada de texto
with st.expander("Analizar texto"):

    text = st.text_input("Escribe por favor:")

    if text:

        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text

        blob = TextBlob(trans_text)

        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.write("Polaridad:", polarity)
        st.write("Subjetividad:", subjectivity)

        # Interacción basada en sentimiento
        if polarity > 0:
            st.success("Es un sentimiento POSITIVO 😊")
            st.balloons()

        elif polarity < 0:
            st.error("Es un sentimiento NEGATIVO 😔")
            st.snow()

        else:
            st.info("Es un sentimiento NEUTRAL 😐")
