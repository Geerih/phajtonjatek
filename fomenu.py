from tkinter import *

class Game:
    def game_click():
        print("Megy")
    
    def credits_click():
        print("creditek")
    
    def options_click():
        print("beállítások")

    
    root =  Tk()
    root.geometry("900x600")
    root.rowconfigure(4, weight=1)
    root.configure(bg="black")
    root.resizable(0, 0)
    root.title("Race 2021")

    jatek = Button(text="Play", fg="black", width=20, height=5, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(0))
    jatek.grid(row=0, column=0, padx=360, pady=20)

    credits = Button(text="Credits", fg="black", width=20, height=5, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(0))
    credits.grid(row=1, column=0, padx=360, pady=20)

    options = Button(text="Options", fg="black", width=20, height=5, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(0))
    options.grid(row=2, column=0, padx=360, pady=20)

    exit = Button(text='Exit', fg="Red", width=20, height=5, bd=0, bg="#fff", cursor="hand2", command=root.destroy)
    exit.grid(row=3, column=0, padx=360, pady=20)

    root.mainloop()

Game()