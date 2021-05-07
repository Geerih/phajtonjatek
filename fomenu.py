from tkinter import *

class Game:
    def game_click():
        print("Megy")
    
    def credits_click():
        print("creditek")
    
    def options_click():
        print("beállítások")

    
    root =  Tk()
    root.geometry("1920x1080")
    bg = PhotoImage(file="img\\kezdokep.png")
    my_label = Label(root, image=bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.rowconfigure(4, weight=1)
    root.configure(bg="black")
    root.resizable(0, 0)
    root.title("Pro Street Racer")

    jatek = Button(text="Play", fg="black", width=40, height=6, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(0))
    jatek.grid(row=0, column=0, padx=1265, pady=20)

    credits = Button(text="Credits", fg="black", width=40, height=6, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(0))
    credits.grid(row=1, column=400, padx=1265, pady=20)

    options = Button(text="Options", fg="black", width=40, height=6, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(0))
    options.grid(row=2, column=0, padx=1265, pady=20)

    exit = Button(text='Exit', fg="Red", width=40, height=6, bd=0, bg="#fff", cursor="hand2", command=root.destroy)
    exit.grid(row=3, column=0, padx=1265, pady=20)

    jatek.place(x=1263, y=410)
    credits.place(x=1263, y=556)
    options.place(x=1263, y=706)
    exit.place(x=1263, y=860)
    root.mainloop()

Game()