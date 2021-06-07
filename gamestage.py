from pgzero.game import screen
from pygame.time import delay

from n_mygameworld import *
import tkinter as tk
from random import randint


class Gamestage(MyStage):
    savvalto = 2
    score = 0

    def keydownlistener(self, key, mod, unicode):
        if key == keys.SPACE:
            animate(self.kocsi, pos=(self.kocsi.pos[0], self.kocsi.pos[1] - 0), duration=0.1)
        if key == keys.SPACE:
            animate(self.kocsi, pos=(self.kocsi.pos[0], self.kocsi.pos[1] + 0), duration=0.1)
        if key == keys.LEFT:
            if self.savvalto < 4:
                animate(self.kocsi, pos=(self.kocsi.pos[0] - self.screen_width / 100 * 10.15625, self.kocsi.pos[1]), duration=0.1)
                self.savvalto = self.savvalto + 1
                self.score = self.score + 1
                print("A pontjaid: " + str(self.score))
        if key == keys.RIGHT:
            if self.savvalto > 1:
                animate(self.kocsi, pos=(self.kocsi.pos[0] + self.screen_width / 100 * 10.15625, self.kocsi.pos[1]), duration=0.1)
                self.savvalto = self.savvalto - 1
                self.score = self.score + 1
                print("A pontjaid: " + str(self.score))


    def keyuplistener(self, key, mod):
        print(key)

    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()


    def update(self):
        self.elloko()
        self.text1.set_text(str(self.score))
        if self.kocsi1.y == self.screen_height:
            self.kocsi1.set_y(-400)
            print("kocsi")
        else:
            self.kocsi1.y = self.kocsi1.y + 10

        if self.kocsi2.y == self.screen_height:
            self.kocsi2.set_y(-700)
            print("kocsi")
        else:
            self.kocsi2.y = self.kocsi2.y + 10

        if self.kocsi3.y == self.screen_height:
            self.kocsi3.set_y(-1700)
            print("kocsi")
        else:
            self.kocsi3.y = self.kocsi3.y + 10

        if self.kocsi4.y == self.screen_height:
            self.kocsi4.set_y(-1300)
            print("kocsi")
        else:
            self.kocsi4.y = self.kocsi4.y + 10

        if self.alap.y == self.screen_height + self.screen_height:
            self.alap.set_y(self.alap3.y - self.screen_height + 20)
        else:
            self.alap.y = self.alap.y + 20
        #szoköz
        if self.alap2.y == self.screen_height + self.screen_height:
            self.alap2.set_y(self.alap.y - self.screen_height)
        else:
            self.alap2.y = self.alap2.y + 20
        #szokoz
        if self.alap3.y == self.screen_height + self.screen_height:
            self.alap3.set_y(self.alap2.y - self.screen_height)
        else:
            self.alap3.y = self.alap3.y + 20

    def elloko(self):
        if self.kocsi.overlaps_with(self.kocsi2):
            self.kocsi.set_x(self.kocsi.x + 200)


    def __init__(self):
        super().__init__()


        music.play('in_the_end.mp3')

        self.alap3 = MyActor(image="hater_jatek3.png", pos=(0, -self.screen_height - self.screen_height), anchor=(0, 0))
        self.alap3.set_size(width=self.screen_width, height=self.screen_height)
        self.add_actor(self.alap3)

        self.alap2 = MyActor(image="hater_jatek2.png", pos=(0, -self.screen_height), anchor=(0, 0))
        self.alap2.set_size(width=self.screen_width, height=self.screen_height)
        self.add_actor(self.alap2)

        self.alap = MyActor(image="hater_jatek1.png", pos=(0, 0), anchor=(0, 0))
        self.alap.set_size(width=self.screen_width, height=self.screen_height)
        self.add_actor(self.alap)

        self.kocsi = MyActor(image="seat_ibiza_19tdi.png", pos=(self.screen_width / 100 * 51.5625, 630), anchor=(0, 0))
        self.add_actor(self.kocsi)

        self.kocsi1 = MyActor(image="alfa_romeo_gulia.png", pos=(self.screen_width / 100 * 35.15625, -400))
        self.add_actor(self.kocsi1)

        self.kocsi2 = MyActor(image="bmw_m4_comp.png", pos=(self.screen_width / 100 * 45.3125, -700))
        self.add_actor(self.kocsi2)

        self.kocsi3 = MyActor(image="honda_civic.png", pos=(self.screen_width / 100 * 54.6875, -1700))
        self.kocsi3.set_size(width=175, height=350)
        self.add_actor(self.kocsi3)

        self.kocsi4 = MyActor(image="bmw_m4_comp.png", pos=(self.screen_width / 100 * 66.40625, -1300))
        self.add_actor(self.kocsi4)

        self.text1: MyButton = MyButton()
        self.text1.set_x(0)
        self.text1.set_y(0)
        self.text1.set_size(height=self.screen_height // 100 * 1, width=self.screen_width // 100 * 1)
        self.text1.set_fontsize(50)
        self.text1.set_color(b=0, g=0, r=0)
        self.text1.set_rotation(0)
        self.add_actor(self.text1)

        self.set_on_key_down_listener(self.keydownlistener)
        self.set_on_key_up_listener(self.keyuplistener)
