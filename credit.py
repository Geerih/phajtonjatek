from n_mygameworld import *
import pgzrun
import tkinter as tk


class Creditstage(MyStage):

    def __init__(self):
        super().__init__()
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        WIDTH = screen_width
        HEIGHT = screen_height
        DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        m1 = MyActor(image="credit.jpg", pos=(0, 0), anchor=(0, 0))
        m1.set_size(width=screen_width, height=screen_height)
        self.add_actor(m1)

        text1: MyLabel = MyLabel()
        text1.set_x(400)
        text1.set_y(80)
        text1.set_fontsize(80)
        text1.set_color(b=255, g=255, r=255)
        text1.set_rotation(0)
        text1.set_text("Fejlesztők / Készítők:")
        self.add_actor(text1)


        text2: MyLabel = MyLabel()
        text2.set_x(540)
        text2.set_y(210)
        text2.set_fontsize(40)
        text2.set_color(b=255, g=255, r=255)
        text2.set_rotation(0)
        text2.set_text("Troznai Roland")
        self.add_actor(text2)

        text3: MyLabel = MyLabel()
        text3.set_x(540)
        text3.set_y(290)
        text3.set_fontsize(40)
        text3.set_color(b=255, g=255, r=255)
        text3.set_rotation(0)
        text3.set_text("Németh Csaba Bence")
        self.add_actor(text3)

        text4: MyLabel = MyLabel()
        text4.set_x(540)
        text4.set_y(370)
        text4.set_fontsize(40)
        text4.set_color(b=255, g=255, r=255)
        text4.set_rotation(0)
        text4.set_text("Zsebők Dávid Ferenc")
        self.add_actor(text4)


        text5: MyLabel = MyLabel()
        text5.set_x(540)
        text5.set_y(450)
        text5.set_fontsize(40)
        text5.set_color(b=255, g=255, r=255)
        text5.set_rotation(0)
        text5.set_text("Oláh Gergő László")
        self.add_actor(text5)


    # label

    def update(self, delta_time: float = 0.0166666666666666666666):
        self.update(delta_time)

    def draw(self):
        self.draw()



