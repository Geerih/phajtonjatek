from tkinter import *

class Credit:

    root = Tk()
    root.geometry("1080x720")
    bg = PhotoImage(file="img\\credit_hatter.png")
    my_label = Label(root, image=bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.rowconfigure(4, weight=1)
    root.configure(bg="black")
    root.resizable(0, 0)
    root.title("Credit")

    exit = Button(text='Exit', fg="Red", width=20, height=4, bd=0, bg="#fff", cursor="hand2", command=root.destroy)
    exit.grid(row=3, column=0, padx=1265, pady=20)

    text = StringVar()
    text.set("asdasd/nasd")
    kiiras = Label(root, text="asddas/nasdasd")
    kiiras.place(x=300, y=300)

    exit.place(x=900, y=630)
    root.mainloop()

Credit()