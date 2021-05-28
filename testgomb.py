from turtle import Screen
from n_mygameworld import *
from gamestage import Gamestage
import pgzrun
import tkinter as tk


def update(dt):
    gamestage.update(dt)


def on_key_down(key, mod, unicode):
    gamestage.on_key_down(key, mod, unicode)


def draw():
    screen.clear()
    gamestage.draw()
    menu.draw()


def exit():
    exit()


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

menu = Actor("Menu", (440, 300))

pgzrun.go()
