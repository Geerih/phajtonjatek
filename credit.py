import tkinter
from tkinter import *

class Credit:

    root = Tk()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    bg = PhotoImage(file="images\\credit.png")
    my_label = Label(root, image=bg)
    my_label.place(x=0, y=0, relwidth=0.5, relheight=0.5)
    root.rowconfigure(4, weight=1)
    root.configure(bg="black")
    root.resizable(0, 0)
    root.title("Credit")

    exit = Button(text='Exit', fg="Red", width=45, height=6, bd=0, bg="#fff", cursor="hand2", command=root.destroy)
    exit.grid(row=3, column=0, padx=1265, pady=20)

    keszitok.set("Készítők/Fejlesztők")
    text = StringVar()
    keszitok = Label(root, text="Készítők/Fejlesztők:")
    keszitok.place(x=300, y=300)

    exit.place(x=1500, y=900)
    root.mainloop()

Credit()