from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import cv2
import tkinter as tk
import time

class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(text="", fg="black", font=("Gotham", 14))
        self.label.grid(row = 0, column=11, padx=0, pady=2)
        self.update_clock()

    def update_clock(self):
        now = time.strftime("%H:%M")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)

#Set up GUI
root = Tk()  #Makes main window
root.wm_title("HAICV")
app=App(root)


Label(text="Зашло:", fg="black", font=("Gotham", 14))\
    .grid(row = 0, column=0, padx=0, pady=2)
Label(text="10", fg="black", font=("Gotham", 14))\
    .grid(row = 0, column=1, padx=0, pady=2)
Label(text="Вышло:", fg="black", font=("Gotham", 14))\
    .grid(row = 0, column=2, padx=0, pady=2)
Label(text="5", fg="black", font=("Gotham", 14))\
    .grid(row = 0, column=3, padx=0, pady=2)
Label(text="IP:", fg="black", font=("Gotham", 14))\
    .grid(row = 0, column=4, padx=0, pady=2)
Entry(width=30, font=("Gotham", 10))\
    .grid(row=0, column=5, columnspan=3)
Button(text="Отправить", font=("Gotham", 9)).grid(row=0, column=10)

#Graphics window
imageFrame = Frame(root, width=602, height=600)
imageFrame.grid(row=2, column=0, columnspan=12, padx=10, pady=2)

#Capture video frames
lmain = Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)
def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame) 


root.after(1000, app.update_clock)
show_frame()  #Display 2
root.mainloop()  #Starts GUI