from tkinter import *
from tkinter.ttk import *

master = Tk()
master.geometry("200x200")

def openNewWindow():
    newWindow = Toplevel(master)
    newWindow.title("Kilépés")
    newWindow.geometry("200x200")
    Label(newWindow, text ="Ez az új ablak").pack()

label = Label(master, text ="Ez a fő ablak")

label.pack(pady = 10)

btn = Button(master, text ="Kattints ide a kilépéshez", command = exit)
btn.pack(pady = 10)

mainloop()