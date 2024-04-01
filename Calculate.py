import wolframalpha
import pyttsx3
import speech_recognition

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wolframalphafunc(query):
    apikey="72KW7Q-LKRK76WY8H"
    requesting=wolframalpha.Client(apikey)
    requested=requesting.query(query)
    try:
        ans=next(requested.results).text
        return ans
    except:
        speak("not answerable")

def calc(query):
    term=str(query)
    term=term.replace("jarvis","")
    term=term.replace("calculate","")
    term=term.replace("find","")
    term=term.replace("into","*")
    term=term.replace("multiply","*")
    term=term.replace("multiply by","*")
    term=term.replace("plus","+")
    term=term.replace("minus","-")
    term=term.replace("divide","/")
    term=term.replace("by","/")
    final=str(term)

    try:
        result=wolframalphafunc(final)
        print(result)
        speak(result)
    except:
        speak("value is not answerable")