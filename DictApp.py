import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



appsi={"commandprompt":"cmd","paint":"paint","wsp":"whatsapp","word":"winword","excel":"excel","chrome":"chrome","vs code":"code","powerpoint":"powerpnt"}
def opneApps(query):
    speak("launching, bro")
    # if ".com" in query or ".co.in" in query or ".org" in query:
    query=query.replace("open","")
    query=query.replace("launch","")
    query=query.replace("jarvis","")
    query=query.replace(" ","")
    webbrowser.open(f"https://www.{query}")
    # else:
    #     keys=list(appsi.keys())
    #     for app in keys:
    #         if app in query:
    #             os.system(f"start {appsi[app]}")


def closeapp(query):
    speak("Closing,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    elif "4 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    else:
        keys = list(appsi.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {appsi[app]}.exe")





