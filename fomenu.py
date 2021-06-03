from n_mygameworld import *
import pgzrun
import tkinter as tk
import credit as ct

menustage = MyStage()

# screen

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
WIDTH = screen_width
HEIGHT = screen_height
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


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


# label

text1: MyButton = MyButton()
text1.set_x(1650)
text1.set_y(400)
text1.set_height(115)
text1.set_fontsize(50)
text1.set_fontsize(50)
text1.set_color(b=0, g=0, r=0)
text1.set_rotation(0)
text1.set_text("PLAY")
text1.set_on_mouse_down_listener(func=startgame)
menustage.add_actor(text1)

text2: MyButton = MyButton()
text2.set_x(1650)
text2.set_y(547)
text2.set_height(115)
text2.set_fontsize(50)
text2.set_fontsize(50)
text2.set_color(b=0, g=0, r=0)
text2.set_rotation(0)
text2.set_text("CREDIT")
text2.set_on_mouse_down_listener(func=credit)
menustage.add_actor(text2)

text3: MyButton = MyButton()
text3.set_x(1650)
text3.set_y(695)
text3.set_height(115)
text3.set_fontsize(50)
text3.set_fontsize(50)
text3.set_color(b=0, g=0, r=0)
text3.set_rotation(0)
text3.set_text("OPTIONS")
text3.set_on_mouse_down_listener(func=options)
menustage.add_actor(text3)

text4: MyButton = MyButton()
text4.set_x(1650)
text4.set_y(847)
text4.set_width(100)
text4.set_height(115)
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
