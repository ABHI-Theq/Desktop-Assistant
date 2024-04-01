import webbrowser

import pyttsx3
import pywhatkit
import wikipedia

engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def searchgoogle(query):
    if "google" in query or ("what" in query or "who" in query):
        import wikipedia as wki
        query=query.replace("jarvis","")
        query=query.replace("google","")
        query=query.replace("google search","")

        try:
            pywhatkit.search(query)
            result=wki.summary(query,2)
            print(result)
            speak(result)
        except:
            speak("no speakable output available")

def searchyoutube(query):
    if "youtube" in query or (("song" in query and "play" in query) or ("song" in query)):
        query=query.replace("jarvis","")
        query=query.replace("youtube","")
        query=query.replace("youtube search","")
        web="https://www.youtube.com/results?search_query="+query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("finished")

def searchwiki(query):
    if "wikipedia" in query:
        speak("searching in wikipedia")
        query=query.replace("jarvis","")
        query=query.replace("wikipedia","")
        query=query.replace("wikipedia search","")
        wiki=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(wiki)
        speak(wiki)