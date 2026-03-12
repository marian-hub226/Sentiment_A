import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from streamlit_lottie import st_lottie
import requests

# -------- Cargar animación desde URL --------
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://assets5.lottiefiles.com/packages/lf20_touohxv0.json"

animation = load_lottieurl(lottie_url)

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
