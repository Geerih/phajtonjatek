from turtle import Screen

from pgzero import screen

from n_mygameworld import *
from gamestage import Gamestage
import pgzrun
import tkinter as tk


def update(dt):
    gamestage.update(dt)


def on_key_down(key, mod, unicode):
    gamestage.on_key_down(key, mod, unicode)


def on_key_up(key, mod):
    gamestage.on_key_up(key, mod)

def draw():
    screen.clear()
    gamestage.draw()

gamestage = Gamestage()

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


pgzrun.go()
