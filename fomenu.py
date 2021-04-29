from tkinter import *
import tkinter

class Game:
    def game_click():
        print("Megy")
    
    def credits_click():
        print("creditek")
    
    def options_click():
        print("beállítások")

    
    root =  Tk()
    root.geometry("900x600")
    root.rowconfigure(2,weight=1)
    root.configure(bg = "black")
    root.resizable(0, 0)
    root.title("Race 2021")
    jatek = Button(text = "Play", fg = "black", width = 20, height = 5, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 1)
    credits = Button(text = "Credits", fg = "black", width = 20, height = 5, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 1, column = 0, columnspan = 2, padx = 1, pady = 1)
    options = Button(text = "Options", fg = "black", width = 20, height = 5, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 2, column = 0, columnspan = 2, padx = 1, pady = 1)
    exit = Button(root, text='Exit', fg = "Red", command = root.destroy)
    root.mainloop()

Game()