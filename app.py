import streamlit as st
import requests

API_TEXT = "http://127.0.0.1:8000/translate-text"
API_AUDIO = "http://127.0.0.1:8000/translate-audio"

st.set_page_config(page_title="Voice Translator", page_icon="🎙️")
st.title("🎙️ Voice Translator (EN → HI → JA)")

tab1, tab2 = st.tabs(["📝 Text Input", "🎤 Voice Input"])

# TEXT → SPEECH
with tab1:
    text = st.text_area("Enter English Text")

    if st.button("Translate Text"):
        res = requests.post(API_TEXT, json={"text": text}).json()

        st.subheader("Hindi 🇮🇳")
        st.success(res["hindi"])
        st.audio(res["hindi_audio"])

        st.subheader("Japanese 🇯🇵")
        st.success(res["japanese"])
        st.audio(res["japanese_audio"])

# SPEECH → TEXT
with tab2:
    audio_file = st.file_uploader("Upload English Audio", type=["wav", "mp3"])

    if audio_file and st.button("Translate Voice"):
        files = {"file": audio_file}
        res = requests.post(API_AUDIO, files=files).json()

        st.subheader("Recognized English")
        st.info(res["english"])

        st.subheader("Hindi 🇮🇳")
        st.success(res["hindi"])
        st.audio(res["hindi_audio"])

        st.subheader("Japanese 🇯🇵")
        st.success(res["japanese"])
        st.audio(res["japanese_audio"])
