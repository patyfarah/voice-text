import streamlit as st
import speech_recognition as sr
from googletrans import Translator
import tempfile  # For saving audio files temporarily
import os

def speech_to_text_with_arabic_translation():
    """
    Captures speech from uploaded audio, converts it to text, and translates it to Arabic.
    This version avoids microphone access and uses file uploads for better cloud compatibility.
    """
    translator = Translator()

    st.title("Audio to Arabic Text Translation")

    uploaded_file = st.file_uploader("Upload an audio file (WAV)", type=["wav"])

    if uploaded_file is not None:
        try:
            # Save the uploaded file to a temporary location
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
                temp_audio.write(uploaded_file.read())
                temp_audio_path = temp_audio.name

            recognizer = sr.Recognizer()

            with sr.AudioFile(temp_audio_path) as source:
                audio_data = recognizer.record(source)  # Record the entire file
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
