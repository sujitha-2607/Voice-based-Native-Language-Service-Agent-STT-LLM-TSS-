import speech_recognition as sr
import pygame
import time
from gtts import gTTS
import os
import tempfile

# ---------------- SPEECH TO TEXT (TELUGU) ----------------
def listen_te():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎙 వింటున్నాను...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5, phrase_time_limit=8)

        text = r.recognize_google(audio, language="te-IN")
        print(f"[USER] {text}")
        return text

    except Exception as e:
        print(f"❌ STT error: {e}")
        return ""


# ---------------- TEXT TO SPEECH (TELUGU) ----------------
def speak_te(text):
    try:
        print(f"[TTS] {text}")

        tts = gTTS(text=text, lang="te")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            filename = f.name
            tts.save(filename)

        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.quit()
        os.remove(filename)

    except Exception as e:
        print(f"❌ TTS error: {e}")
