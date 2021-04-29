from tkinter import Tk, Canvas, Button
CHANGED = False
button1 = None
button2 = None

def options():
    global button1, button2

    button1 = Button(window, text='Click to change door')
    button1.bind("<Button-1>", change)
    button1.grid(row=0, sticky='w')

    button2 = Button(window, text='Click to keep door')
    button2.bind("<Button-1>", keep)
    button2.grid(row=1, sticky='w')

def change(*args):
    global CHANGED
    CHANGED = True
def keep(*args):
    global CHANGED
    CHANGED = False
def door1(*args):
    if button1 is None and button2 is None:
        options()

window = Tk()
window.geometry("600x600")
window.rowconfigure(2,weight=1)
canvas = Canvas(window, width=600, height=500)
square1 = canvas.create_rectangle(50, 500, 150, 200, fill="blue", tags="open_door_1")

canvas.tag_bind("open_door_1", "<Button-1>", door1)
canvas.grid(row=2,sticky='s')
window.mainloop()