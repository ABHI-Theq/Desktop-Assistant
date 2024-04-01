import pyttsx3
import speech_recognition
import datetime
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning, sir")
    elif hour>12 and hour<=18:
        speak("good afternoon, sir")
    else:
        speak("good evening, sir")

    speak("how can i help you sir")