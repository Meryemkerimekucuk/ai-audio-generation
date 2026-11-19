import streamlit as st
from pathlib import Path

from config import aai, gemini_client, GEMINI_MODEL
from utils import get_error_message, temporary_audio_file


def render():
    st.header("Audio Translator")
    st.write("Translate audio into your desired language.")

    # Upload audio file
    audio_file = st.file_uploader(
        "Upload an audio file",
        type=["mp3", "wav", "m4a"],
        key="translator_file"
    )

    # Select target language
    target_language = st.selectbox(
        "Select target language",
        [
            "Turkish",
            "English",
            "German",
            "French",
            "Spanish",
            "Italian",
            "Japanese",
            "Korean"
        ]
    )

    if audio_file:
        st.audio(audio_file)

        if st.button("Translate Audio", key="translate_button"):

            try:
                # Step 1: Transcribe audio
                with st.spinner("Transcribing audio..."):

                    suffix = Path(audio_file.name).suffix

                    with temporary_audio_file(
                        audio_file.getvalue(),
                        suffix
                    ) as temp_audio_path:

                        transcriber = aai.Transcriber()
                        transcript = transcriber.transcribe(temp_audio_path)

                if transcript.text:

                    st.subheader("Original Transcript")

                    st.text_area(
                        "Original text",
                        value=transcript.text,
                        height=150
                    )

                    # Step 2: Translate with Gemini
                    with st.spinner("Translating with AI..."):

                        prompt = f"""
                        Translate the following text into {target_language}.

                        Preserve the original meaning and tone.
                        Do not add explanations or comments.
                        Return only the translated text.

                        Text:
                        {transcript.text}
                        """

                        response = gemini_client.models.generate_content(
                            model=GEMINI_MODEL,
                            contents=prompt
                        )

                    # Step 3: Display translation
                    st.subheader(f"Translation ({target_language})")

                    st.text_area(
                        "Translated text",
                        value=response.text,
                        height=150
                    )

                    # Download translation
                    st.download_button(
                        label="Download Translation",
                        data=response.text,
                        file_name="translation.txt",
                        mime="text/plain"
                    )

                else:
                    st.warning("No speech could be detected.")

            except Exception as e:
                st.error(get_error_message(e))