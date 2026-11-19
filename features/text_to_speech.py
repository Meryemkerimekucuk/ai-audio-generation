import streamlit as st
import pyttsx3
from utils import get_error_message

def render():
    st.header("Text to Speech")
    st.write("Convert written text into speech.")

    # Text input
    text_input = st.text_area(
        "Enter your text",
        placeholder="Write something you want to convert into speech...",
        height=200,
        key="tts_text"
    )

    # Initialize speech engine
    engine = pyttsx3.init()

    # Get available voices
    voices = engine.getProperty("voices")
    voice_options = [voice.name for voice in voices]

    # Voice selection
    selected_voice = st.selectbox(
        "Select voice",
        voice_options,
        key="tts_voice"
    )

    # Speech rate
    speech_rate = st.slider(
        "Speech speed",
        min_value=100,
        max_value=250,
        value=175,
        step=25,
        key="tts_rate"
    )

    # Generate speech
    if st.button("Generate Speech", key="tts_button"):

        if text_input.strip():

            try:
                # Select voice
                selected_index = voice_options.index(selected_voice)
                engine.setProperty("voice", voices[selected_index].id)

                # Set speech rate
                engine.setProperty("rate", speech_rate)

                # Convert text to speech
                with st.spinner("Generating speech..."):
                    engine.say(text_input)
                    engine.runAndWait()

                st.success("Speech completed!")

            except Exception as e:
                  st.error(get_error_message(e))
        else:
            st.warning("Please enter some text.")
