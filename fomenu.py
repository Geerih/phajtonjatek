from n_mygameworld import *
import pgzrun
import tkinter as tk

menustage = MyStage()

# screen
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
WIDTH = screen_width
HEIGHT = screen_height
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# actorok
m1 = MyActor(image="kezdokep.png", pos=(0, 0), anchor=(0, 0))
m1.set_size(width=screen_width, height=screen_height)
menustage.add_actor(m1)

# label
text1: MyButton = MyButton()
text1.set_x(900)
text1.set_y(310)
text1.set_fontsize(50)
text1.set_color(b=0, g=0, r=0)
text1.set_rotation(0)
text1.set_text("bob es a meki")
menustage.add_actor(text1)




def update(dt):
    menustage.update(dt)


def draw():
    menustage.draw()


pgzrun.go()
