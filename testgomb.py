from turtle import Screen
from n_mygameworld import *
from gamestage import Gamestage
import pgzrun
import tkinter as tk

gamestage = Gamestage()

def update(dt):
    gamestage.update(dt)


def on_key_down(key, mod, unicode):
    gamestage.on_key_down(key, mod, unicode)


def draw():
    screen.clear()
    gamestage.draw()

def exit():
    exit()


root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
WIDTH = screen_width
HEIGHT = screen_height
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

WIDTH = screen_width
HEIGHT = screen_height
print(screen_width)
print(screen_height)

# label
text1: MyButton = MyButton()
text1.set_x(900)
text1.set_y(310)
text1.set_fontsize(50)
text1.set_color(b=0, g=0, r=0)
text1.set_rotation(0)
text1.set_text("EXIT")
text1.set_on_mouse_down_listener(exit)
gamestage.add_actor(text1)

def on_mouse_down(pos, button):
    gamestage.on_mouse_down(pos, button)

pgzrun.go()
