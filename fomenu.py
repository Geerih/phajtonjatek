from n_mygameworld import *
import pgzrun
import tkinter as tk
import credit as ct
import controls as ctls

menustage = MyStage()

# screen

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
WIDTH = screen_width
HEIGHT = screen_height
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
buttonheighttt: int = screen_height / 100 * 10.648148148148149


# actors

m1 = MyActor(image="kezdokep.png", pos=(0, 0), anchor=(0, 0))
m1.set_size(width=screen_width, height=screen_height)
menustage.add_actor(m1)


# function

def exit(pos=0, btn=0):
    print('exit')
    exit()


def startgame(pos=0, btn=0):
    print('play')


def credit(self, pos=0, btn=0):
    print('credit')
    ct.Creditstage()




def options(pos=0, btn=0):
    print('options')
    ctls.Controlsstage()


# label

""" ** 10.648148148148149"""
text1: MyButton = MyButton()
text1.set_x(screen_width / 100 * 64.453125)
text1.set_y(screen_height / 100 * 37.03703703703704)
text1.set_size(height=screen_height // 100 * 10, width=180)
text1.set_fontsize(50)
text1.set_color(b=0, g=0, r=0)
text1.set_rotation(0)
text1.set_text("PLAY")
text1.set_on_mouse_down_listener(func=startgame)
menustage.add_actor(text1)

text2: MyButton = MyButton()
text2.set_x(screen_width / 100 * 64.453125)
text2.set_y(screen_height / 100 * 50.648148148148145)
text2.set_size(height=screen_height // 100, width=180)
text2.set_fontsize(50)
text2.set_color(b=0, g=0, r=0)
text2.set_rotation(0)
text2.set_text("CREDIT")
text2.set_on_mouse_down_listener(func=credit)
menustage.add_actor(text2)

text3: MyButton = MyButton()
text3.set_x(screen_width / 100 * 64.453125)
text3.set_y(screen_height / 100 * 64.35185185185185)
text3.set_size(height=screen_height // 100, width=180)
text3.set_fontsize(50)
text3.set_color(b=0, g=0, r=0)
text3.set_rotation(0)
text3.set_text("OPTIONS")
text3.set_on_mouse_down_listener(func=options)
menustage.add_actor(text3)

text4: MyButton = MyButton()
text4.set_x(screen_width / 100 * 64.453125)
text4.set_y(screen_height / 100 * 78.42592592592592)
text4.set_width(100)
text4.set_size(height=screen_height // 100, width=180)
text4.set_fontsize(50)
text4.set_color(b=0, g=0, r=0)
text4.set_rotation(0)
text4.set_text("EXIT")
text4.set_on_mouse_down_listener(func=exit)
menustage.add_actor(text4)


# other

def update(dt):
    menustage.update(dt)


def draw():
    menustage.draw()


def on_mouse_down(pos, button):
    menustage.on_mouse_down(pos, button)


pgzrun.go()
