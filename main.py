import datetime
import os
from pygame import mixer
from plyer import notification
import pyautogui
import speedtest
import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup

for i in range(3):
    with open("password.txt") as f:
        se=f.read()
    a=input("enter password:\t")
    if i==0 or i==1:
        if a==se:
            print("WELCOME SIR! WAKE UP TO LOAD ME UP")
            break
        else:
            print("Try again")
    if i==2:
        if a==se:
            print("WELCOME SIR! WAKE UP TO LOAD ME UP")
            break
        else:
            print("chances ended")
            exit()

from INtro import play_img
play_img


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


def alarm(query):
    with open("Alarmtext.txt","a") as f:
        f.write(query)
        # f.write(f"{query.split(" and ")[0]}:{query.split(" and ")[1]}:{query.split(" and ")[2]}")
    os.startfile("alarm.py")
if __name__=="__main__":
    import Search as sch
    from DictApp import opneApps, closeapp
    while True:
        query=take_command().lower()
        if "wake up" in query or "breakup" in query or "makeup" in query:
            from Greet import greet
            greet()
            while True:
                query = take_command().lower()
                if "go in sleep" in query or "relax" in query:
                    break
                elif "open" in query and "whatsapp" in query:
                    os.startfile("whatsapping.py")
                    # from whatsapping import sendMsg
                    # sendMsg()
                elif "full screen" in query:
                    pyautogui.press("f")
                elif "exit full screen" in query or "go normal" in query:
                    pyautogui.keyDown('esc')
                    pyautogui.keyUp('esc')
                elif "open" in query and (".com" in query or ".co.in" in query or ".org" in query):
                    opneApps(query)
                elif "close" in query:
                    closeapp(query)
                elif "open" in query:
                    query=query.replace("open","")
                    query=query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    # pyautogui.sleep(2)
                    pyautogui.press("enter")

                elif "internet" in query and "speed" in query:
                    wifi=speedtest.Speedtest()
                    upload_net=round(wifi.upload()/1048576,2)        #1M = 1024*1024
                    download_net=round(wifi.download()/1048576,2)
                    print(f"wifi upload speed is: {upload_net}")
                    print(f"wifi download speed is: {download_net}")
                    speak(f"wifi upload speed is: {upload_net}")
                    speak(f"wifi download speed is: {download_net}")

                elif "ipl score" in query:
                    url="https://www.cricbuzz.com/cricket-match/live-scores"
                    r=requests.get(url)
                    score=BeautifulSoup(r.text,"html.parser")
                    team1=score.findAll(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2=score.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()

                    t1_score=score.find_all(class_="cb-ovr-flo")[8].get_text()
                    t2_score=score.find_all(class_="cb-ovr-flo")[10].get_text()

                    a=print(f"{team1} : {t1_score}")
                    b=print(f"{team2} : {t2_score}")
                    notification.notify(
                        title="IPL Live Score:- ",
                        message=f"{team1} : {t1_score}\n{team2} : {t2_score}",
                        timeout=15
                   )

                elif "play" in query and "game" in query:
                    from game import game_play
                    game_play()

                elif "screenshot" in query:
                    img=pyautogui.screenshot()
                    img.save("Screenshot/sc1.jpg")
                    speak("Picture taken")
                elif "click" in query and "photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("smile")
                    pyautogui.press("enter")
                    speak("Done sir")
                elif "translate" in query:
                    from Translatoring import translategl
                    query=query.replace("jarvis","")
                    query=query.replace("translate","")
                    translategl(query)

                elif ("song" in query and "play" in query) or ("song" in query):
                    sch.searchyoutube(query)
                elif "hello" in query:
                    speak("hey sir , how are you doing")
                elif "doing good" in query or "going good" in query or "i am good" in query:
                    speak("great sir")
                elif "how are you" in query:
                    speak("fantastic sir")
                elif "change the password" in query or ("change the password" in query and "jarvis" in query):
                    with open("password.txt","w") as f:
                        speak("enter the new password\n")
                        ps=input("Enter new password:\t")
                        f.write(ps)
                        speak(f"your new password is {ps}")
                        print(f"your new password is {ps}")


                elif "schedule" in query and "day" in query:
                    tasks = []  # Empty list

                    speak("Do you want to clear old tasks (Plz speak YES or NO)")

                    query = take_command().lower()

                    if "yes" in query:

                        file = open("tasks.txt", "w")

                        file.write(f"")

                        file.close()

                        no_tasks = int(input("Enter the no. of tasks :- "))

                        i = 0

                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))

                            file = open("tasks.txt", "a")

                            file.write(f"{i}. {tasks[i]}\n")

                            file.close()

                    elif "no" in query:

                        i = 0

                        no_tasks = int(input("Enter the no. of tasks :- "))

                        for i in range(no_tasks+1):
                            tasks.append(input("Enter the task :- "))

                            file = open("tasks.txt", "a")

                            file.write(f"{tasks[i]}\n")

                            file.close()
                elif "show my schedule" in query or ("show" in query and ("tasks" in query or "task" in query)):
                    file = open("tasks.txt", "r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title="My schedule :-",
                        message=content,
                        timeout=20
                    )
                elif "show" in query and "focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()
                elif "focus mode" in query or "focus more" in query or "focus mod" in query:
                    speak("Are you Sure if you wanna enter in focus mode")
                    if "yes" in take_command().lower():
                        speak("Entering in the focus mode")
                        # os.startfile("C:\\Users\\SWEETY\\OneDrive\\Desktop\\coding_python\\JARVIS\\Focus_mode.py")
                        from Focus_mode import is_admin
                        is_admin()
                        exit()
                    else:
                        pass
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play the video" in query:
                    pyautogui.press("k")
                    speak("video played again")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "volume up" in query or "increase the volume" in query:
                    from Keyboard import volumeup
                    speak("increasing theb volume")
                    volumeup()
                elif "volume down" in query or "decrease the volume" in query:
                    from Keyboard import volumedown
                    speak("decreasing the volume")
                    volumedown()
                elif "shutdown" in query:
                    speak("are you sure")
                    if "yes" in take_command().lower():
                        os.system("shutdown /s /t 1")
                    elif "no" in take_command().lower():
                        break
                elif "google" in query:
                    sch.searchgoogle(query)
                elif "youtube" in query:
                    sch.searchyoutube(query)
                elif "wikipedia" in query:
                    sch.searchwiki(query)
                elif "news" in query:
                    from NewsQuery import latestNews
                    latestNews()
                elif "calculate" in query or "find" in query:
                    from Calculate import wolframalphafunc,calc
                    calc(query)
                elif ("what" in query and "temperature" in query) or ("temperature" in query):
                    url=f"https://www.google.com/search?q={query}"
                    r=requests.get(url)
                    data=BeautifulSoup(r.text,"html.parser")
                    temp=data.find("div",class_="BNeawe").text
                    speak(f"current temperature is {temp}")
                    print(f"current temperature is {temp}")
                elif("what" in query and "weather" in query) or ("weather" in query):
                    url=f"https://www.google.com/search?q={query}"
                    r=requests.get(url)
                    data=BeautifulSoup(r.text,"html.parser")
                    temp=data.find("div",class_="BNeawe").text
                    speak(f"current weather is {temp}")
                    print(f"current weather is {temp}")
                elif "set the alarm" in query or ("set" in query and "alarm" in query):
                    print("Time given should be like: H and M and S")
                    speak("set the time\n")
                    a=input()
                    alarm(a)
                    speak("Done Sir")
                elif ("what" in query and "the time" in query) or ("the time" in query):
                    strftime=datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"the time is {strftime}")
                elif "remember this" in query or "remember that" in query:
                    recallmsg=query.replace("remember that","")
                    recallmsg=recallmsg.replace("jarvis","")
                    speak(f"you told me to remember {recallmsg}")
                    with open("remember.txt","w") as f:
                        f.write(recallmsg)
                elif "what did i say to remember" in query or ("what" in query and "remember" in query):
                    with open("remember.txt","r") as f:
                        speak(f.read())
                elif "what" in query or "who" in query:
                    sch.searchgoogle(query)
                elif "bye buddy" in query or "so jao" in query:
                    exit()