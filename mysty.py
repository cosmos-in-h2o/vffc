from tkinter import *


def button(master, text, command):
    return Button(master, text=text, width=30, height=2, relief=FLAT, fg="#252930",
                  bg="#4e76b7",
                  activebackground="#486ca8", command=command)


def button2(master, text, command):
    return Button(master, text=text, width=8,
                  relief=FLAT, fg="#252930",
                  bg="#4e76b7",
                  activebackground="#486ca8", command=command)
