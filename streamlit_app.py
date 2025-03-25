import streamlit as st
import speech_recognition as sr

def test_microphone():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("Microphone available")
    except Exception as e:
        st.write(f"Microphone error: {e}")

test_microphone()
