import requests
import json
import pyttsx3
import speech_recognition as sr

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
        speak("come again please")
        return "None"
    return query
def latestNews():
    api_dict={"business":"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=48bd1520c326449d973b366a9ea40449",
             "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=48bd1520c326449d973b366a9ea40449",
             "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=48bd1520c326449d973b366a9ea40449",
             "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=48bd1520c326449d973b366a9ea40449",
             "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=48bd1520c326449d973b366a9ea40449",
             "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=48bd1520c326449d973b366a9ea40449"}

    content=None
    url=None
    speak("which field news do you wanna know about , business, technology, science, sports, entertainment, health")
    field=input("type news field wanna know:\t")
    for key,value in api_dict.items():
        if key.lower() in field.lower():
            url=value
            print("let's begin")
            break
        else:
            url=True
    if url is True:
        print("url not found")

    new=requests.get(url).text
    news=json.loads(new)
    speak("here is news")
    arts=news["articles"]
    for article in arts:
        article1=article["title"]
        article2=article["description"]
        print(article1)
        speak(article1)
        print(article2)
        speak(article2)
        newsurl=article["url"]
        print(f"for more info visit {newsurl}")
        speak("wanna continue")
        print("yes or no")
        a=take_command().lower()
        if "yes" in a:
            pass
        else:
            break

    speak("that's all")