from tkinter import *
import tkinter

class Game:
    jatek = Button(text = "Play", fg = "black", width = 50, height = 30, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)

    root =  Tk()
    root.geometry("900x600")
    root.rowconfigure(2,weight=1)
    root.resizable(0, 0)
    root.title("Race 2021")
    root.mainloop()

Game()