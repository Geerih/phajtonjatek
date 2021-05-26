from n_mygameworld import *
import pgzrun
import tkinter as tk

menustage = MyStage()

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
WIDTH = screen_width
HEIGHT = screen_height
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

m1 = MyActor(image="kezdokep.png", pos=(0, 0), anchor=(0, 0))
m1.set_size(width=screen_width, height=screen_height)
menustage.add_actor(m1)

def update(dt):
    menustage.update(dt)

def draw():
    menustage.draw()




pgzrun.go()