from n_mygameworld import *
import pgzrun
import tkinter as tk

controlsstage = MyStage()

# screen

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
WIDTH = screen_width
HEIGHT = screen_height
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


# actors

m1 = MyActor(image="controls.jpg", pos=(0, 0), anchor=(0, 0))
m1.set_size(width=screen_width, height=screen_height)
controlsstage.add_actor(m1)


# function

def exit(pos=0, btn=0):
    print('exit')
    exit()


def startgame(pos=0, btn=0):
    print('play')


# label
    text1: MyLabel = MyLabel()
    text1.set_x(400)
    text1.set_y(80)
    text1.set_fontsize(80)
    text1.set_color(b=255, g=255, r=255)
    text1.set_rotation(0)
    text1.set_text("Fejlesztők / Készítők:")
    controlsstage.add_actor(text1)

# other

def update(dt):
    controlsstage.update(dt)


def draw():
    controlsstage.draw()


def on_mouse_down(pos, button):
    controlsstage.on_mouse_down(pos, button)


pgzrun.go()
