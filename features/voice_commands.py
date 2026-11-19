import streamlit as st

from streamlit_mic_recorder import mic_recorder
from config import aai, gemini_client, GEMINI_MODEL
from utils import get_error_message, temporary_audio_file


def render():
    st.header("Voice Commands")
    st.write("Speak naturally and let AI understand your request.")

    # Microphone
    audio = mic_recorder(
        start_prompt="🎙️ Start Recording",
        stop_prompt="⏹️ Stop Recording",
        key="voice_command_recorder",
        format="wav"
    )

    if audio:
        st.success("Recording completed!")
        st.audio(audio["bytes"], format="audio/wav")

        if st.button("Analyze Voice Command", key="voice_analyze"):

            try:
                # Step 1: Convert voice to text
                with st.spinner("Converting your voice to text..."):

                    with temporary_audio_file(
                        audio["bytes"],
                        ".wav"
                    ) as temp_audio_path:

                        transcriber = aai.Transcriber()
                        transcript = transcriber.transcribe(temp_audio_path)

                # Step 2: Check transcription
                if transcript.text:

                    st.subheader("What you said")

                    st.text_area(
                        "Transcribed text",
                        value=transcript.text,
                        height=120
                    )

                    # Step 3: Send text to Gemini
                    with st.spinner("Gemini is thinking..."):

                        prompt = f"""
                        You are a helpful AI voice assistant.

                        The user gave you the following voice command:
                        {transcript.text}

                        Understand the user's intention and respond helpfully.
                        Answer in Turkish unless the user speaks another language.
                        Be clear, natural and concise.
                        """

                        response = gemini_client.models.generate_content(
                            model=GEMINI_MODEL,
                            contents=prompt
                        )

                    # Step 4: Display AI response
                    st.subheader("AI Assistant Response")
                    st.write(response.text)

                else:
                    st.warning("No speech could be detected.")

            except Exception as e:
                st.error(get_error_message(e))