import self as self

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

m1 = MyActor(image="credit.png", pos=(0, 0), anchor=(0, 0))
m1.set_size(width=screen_width, height=screen_height)
menustage.add_actor(m1)

# label



def update(dt):
    menustage.update(dt)


def draw():
    menustage.draw()

text1: MyButton = MyButton()
text1.set_x(400)
text1.set_y(80)
text1.set_fontsize(80)
text1.set_color(b=255, g=255, r=255)
text1.set_rotation(0)
text1.set_text("Fejlesztők / Készítők:")
menustage.add_actor(text1)

text2: MyButton = MyButton()
text2.set_x(540)
text2.set_y(200)
text2.set_fontsize(40)
text2.set_color(b=255, g=255, r=255)
text2.set_rotation(0)
text2.set_text("Troznai Roland")
menustage.add_actor(text2)

text3: MyButton = MyButton()
text3.set_x(540)
text3.set_y(250)
text3.set_fontsize(40)
text3.set_color(b=255, g=255, r=255)
text3.set_rotation(0)
text3.set_text("Németh Csaba Bence")
menustage.add_actor(text3)

text4: MyButton = MyButton()
text4.set_x(540)
text4.set_y(300)
text4.set_fontsize(40)
text4.set_color(b=255, g=255, r=255)
text4.set_rotation(0)
text4.set_text("Zsebők Dávid")
menustage.add_actor(text4)

text5: MyButton = MyButton()
text5.set_x(540)
text5.set_y(350)
text5.set_fontsize(40)
text5.set_color(b=255, g=255, r=255)
text5.set_rotation(0)
text5.set_text("Oláh Gergő")
menustage.add_actor(text5)

pgzrun.go()