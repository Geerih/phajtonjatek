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

def exit():
    exit()

def update(dt):
    menustage.update(dt)

def on_mouse_down(pos, button):
    menustage.on_mouse_down(pos, button)

def draw():
    menustage.draw()

text1: MyButton = MyButton()
text1.set_x(650)
text1.set_y(80)
text1.set_fontsize(80)
text1.set_color(b=255, g=255, r=255)
text1.set_rotation(0)
text1.set_text("Developers / Creators:")
menustage.add_actor(text1)

text2: MyButton = MyButton()
text2.set_x(810)
text2.set_y(210)
text2.set_fontsize(40)
text2.set_color(b=255, g=255, r=255)
text2.set_rotation(0)
text2.set_text("Troznai Roland")
menustage.add_actor(text2)

text3: MyButton = MyButton()
text3.set_x(810)
text3.set_y(290)
text3.set_fontsize(40)
text3.set_color(b=255, g=255, r=255)
text3.set_rotation(0)
text3.set_text("Németh Csaba Bence")
menustage.add_actor(text3)

text4: MyButton = MyButton()
text4.set_x(810)
text4.set_y(370)
text4.set_fontsize(40)
text4.set_color(b=255, g=255, r=255)
text4.set_rotation(0)
text4.set_text("Zsebők Dávid Ferenc")
menustage.add_actor(text4)

text5: MyButton = MyButton()
text5.set_x(810)
text5.set_y(450)
text5.set_fontsize(40)
text5.set_color(b=255, g=255, r=255)
text5.set_rotation(0)
text5.set_text("Oláh Gergő László")
menustage.add_actor(text5)

text1: MyButton = MyButton()
text1.set_x(1550)
text1.set_y(980)
text1.set_fontsize(50)
text1.set_color(b=50, g=50, r=210)
text1.set_rotation(0)
text1.set_text("Back to main menu")
text1.set_on_mouse_down_listener(exit)
menustage.add_actor(text1)

pgzrun.go()