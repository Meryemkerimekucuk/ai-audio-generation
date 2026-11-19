import streamlit as st
from pathlib import Path

from config import aai
from utils import get_error_message, temporary_audio_file


def render():
    st.header("Speech to Text")
    st.write("Convert your audio into text.")

    audio_file = st.file_uploader(
        "Upload an audio file",
        type=["mp3", "wav", "m4a"],
        key="stt_file"
    )

    if audio_file:
        st.audio(audio_file)

        if st.button("Transcribe Audio", key="stt_button"):

            try:
                with st.spinner("Audio is being transcribed..."):

                    suffix = Path(audio_file.name).suffix

                    with temporary_audio_file(
                        audio_file.getvalue(),
                        suffix
                    ) as temp_audio_path:

                        transcriber = aai.Transcriber()
                        transcript = transcriber.transcribe(temp_audio_path)

                if transcript.text:
                    st.success("Transcription completed!")
                    st.subheader("Transcription Result")

                    st.text_area(
                        "Your text",
                        value=transcript.text,
                        height=250
                    )

                    st.download_button(
                        label="Download Transcript",
                        data=transcript.text,
                        file_name="transcription.txt",
                        mime="text/plain"
                    )

                else:
                    st.warning("No speech could be detected.")

            except Exception as e:
                st.error(get_error_message(e))