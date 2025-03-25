import streamlit as st
import speech_recognition as sr
from googletrans import Translator
from audio_recorder_streamlit import audio_recorder
import tempfile
import os

def speech_to_text_with_arabic_translation():
    """
    Captures speech from recorded audio, converts it to text, and translates it to Arabic.
    Uses audio-recorder-streamlit for audio capture.
    """
    translator = Translator()

    st.title("Recorded Audio to Arabic Text Translation")

    audio_bytes = audio_recorder()

    if audio_bytes:
        try:
            # Save the recorded audio to a temporary WAV file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
                temp_audio.write(audio_bytes)
                temp_audio_path = temp_audio.name

            recognizer = sr.Recognizer()

            with sr.AudioFile(temp_audio_path) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data)

            st.write(f"Recognized Text: {text}")

            # Translate to Arabic
            translation = translator.translate(text, dest="ar")
            st.write(f"Arabic Translation: {translation.text}")

        except sr.UnknownValueError:
            st.error("Could not understand audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
        finally:
            # Clean up the temporary audio file
            if 'temp_audio_path' in locals():
                os.remove(temp_audio_path)

if __name__ == "__main__":
    speech_to_text_with_arabic_translation()
