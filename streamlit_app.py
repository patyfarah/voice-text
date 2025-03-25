import streamlit as st
import speech_recognition as sr
from googletrans import Translator

def speech_to_text_with_arabic_translation():
    """
    Captures speech, converts it to text, and translates it to Arabic.
    """
    recognizer = sr.Recognizer()
    translator = Translator()

    st.title("Speech to Arabic Text Translation")

    if st.button("Start Recording"):
        with sr.Microphone() as source:
            st.info("Speak now...")
            try:
                audio = recognizer.listen(source, timeout=10) # 10 second timeout

                st.success("Recording complete!")
                text = recognizer.recognize_google(audio)

                st.write(f"Recognized Text: {text}")

                # Translate to Arabic
                translation = translator.translate(text, dest="ar")
                st.write(f"Arabic Translation: {translation.text}")

            except sr.WaitTimeoutError:
                st.error("Timeout: No speech detected within 10 seconds.")
            except sr.UnknownValueError:
                st.error("Could not understand audio.")
            except sr.RequestError as e:
                st.error(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    speech_to_text_with_arabic_translation()
