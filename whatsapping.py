import pyautogui
import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
from datetime import timedelta
from datetime import datetime
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=.8
        audio=r.listen(source,0,4)

    try:
        print("catching..")
        query=r.recognize_google(audio,language="en-in")
        print(f"You said {query}")

    except Exception as e:
        print("come again please")
        return "None"
    return query

def sendMsg():
    speak("who do you wanna massage")
    contacts={
        "sweeti":"+919899515300",
        "aryan":"+919140222527",
        "arya":"+919307141147",
        "pranav":"+919882832640",
        "gaurang":"+918279515503",
        "aniket":"+919528705854",
        "asma":"917903003302",
        "aasma":"+917903003302",
        "sameer":"+916398574932",
        "adarsh bhaiya":"+919983317108",
        "adarsh":"+919983317108",
    }
    a=take_command().lower()

    for key in contacts.keys():
        if key in a:
            speak("and what is the message")
            message=str(input("enter:\t"))
            hour = int(datetime.now().strftime("%H"))
            update = int((datetime.now().strftime("%M"))) + 1
            pywhatkit.sendwhatmsg(f"{contacts[key]}",message,time_hour=hour,time_min=update)
            # pyautogui.press("enter")
            exit()

    else:
        speak("This person is not in contact list")

sendMsg()