import streamlit as st

from features import speech_to_text
from features import voice_commands
from features import audio_translator
from features import text_to_speech


# Page configuration
st.set_page_config(
    page_title="Audio AI Studio",
    page_icon="🎙️",
    layout="wide"
)

# App title
st.title("🎙️ Audio AI Studio")
st.write("Explore audio with artificial intelligence.")

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🎧 Speech to Text",
    "🎤 Voice Commands",
    "🌍 Audio Translator",
    "🔊 Text to Speech"
])

# Speech to Text
with tab1:
    speech_to_text.render()

# Voice Commands
with tab2:
    voice_commands.render()

# Audio Translator
with tab3:
    audio_translator.render()

# Text to Speech
with tab4:
    text_to_speech.render()