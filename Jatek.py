from turtle import Screen
from turtle import Turtle
import tkinter

class Game:

    def __init__(self):
        screen = Screen()
        turtle = Turtle()
        root = tkinter.Tk()
        root.overrideredirect(True)
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        screen.mainloop()

Game()