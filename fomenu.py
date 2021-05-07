from tkinter import *

class Game:
    def game_click():
        print("Megy")
    
    def credits_click():
        print("creditek")
    
    def options_click():
        print("beállítások")

    
    root =  Tk()
    root.iconbitmap("img/Icon.ico")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
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

    jatek.place(x=root.winfo_screenwidth() / 100 * 65.78125, y=root.winfo_screenheight() / 100 * 37.962)
    credits.place(x=root.winfo_screenwidth() / 100 * 65.78125, y=root.winfo_screenheight() / 100 * 51.481)
    options.place(x=root.winfo_screenwidth() / 100 * 65.78125, y=root.winfo_screenheight() / 100 * 65.370)
    exit.place(x=root.winfo_screenwidth() / 100 * 65.78125, y=root.winfo_screenheight() / 100 * 79.629)
    root.mainloop()

Game()