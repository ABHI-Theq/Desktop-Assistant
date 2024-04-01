from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time
import pygame
from pygame import mixer
mixer.init()



root=Tk()
root.title("Jarvis")
root.geometry("1000x600")

def play_img():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img=Image.open("IronMan.gif")
    lb=(Label(root))
    lb.place(x=0,y=0)
    i=0
    mixer.music.load("BeginSound.mp3")
    mixer.music.play()
    for img in ImageSequence.Iterator(img):
        img=img.resize((1000,600))
        img=ImageTk.PhotoImage(img)
        lb.config(image=img)
        root.update()
        time.sleep(.3)
    root.destroy()

play_img()
root.mainloop()