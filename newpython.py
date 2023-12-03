import sounddevice as sd
import numpy as np
import speech_recognition as sr
import wavio
import io

def record_audio(duration, fs=44100):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='float32')
    sd.wait()
    print("Recording finished.")
    return recording

# Set the duration (in seconds) and sampling frequency of your recording here
duration = 5
fs = 44100

# Record audio
audio_data = record_audio(duration, fs)

# Convert audio data to an audio file in memory (PCM WAV format)
wav_data = io.BytesIO()
wavio.write(wav_data, audio_data, fs, sampwidth=2)

# Rewind the BytesIO object to the beginning
wav_data.seek(0)

# Use SpeechRecognition to recognize the audio
recognizer = sr.Recognizer()
with sr.AudioFile(wav_data) as source:
    audio = recognizer.listen(source)
    try:
        # Recognize the content using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError:
        print("Google Web Speech API request failed")


#Run this combined code, and it should record your speech, save it as a WAV in memory, and then transcribe it using the Google Web Speech API.