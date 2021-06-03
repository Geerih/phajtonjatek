from n_mygameworld import *
import tkinter as tk
from random import randint


class Gamestage(MyStage):
    def keydownlistener(self, key, mod, unicode):
        if key == keys.SPACE:
            animate(self.kocsi, pos=(self.kocsi.pos[0], self.kocsi.pos[1] - 0), duration=0.1)
        if key == keys.SPACE:
            animate(self.kocsi, pos=(self.kocsi.pos[0], self.kocsi.pos[1] + 0), duration=0.1)
        if key == keys.LEFT:
            if self.kocsi.x > 650:
                animate(self.kocsi, pos=(self.kocsi.pos[0] - 200, self.kocsi.pos[1]), duration=0.1)
        if key == keys.RIGHT:
            if self.kocsi.x < 1050:
                animate(self.kocsi, pos=(self.kocsi.pos[0] + 200, self.kocsi.pos[1]), duration=0.1)

    def keyuplistener(self, key, mod):
        print(key)

    def update(self):
        self.kocsi2.y = self.kocsi2.y+5
        self.elloko()
        self.kocsi1.y = self.kocsi1.y+5

    def elloko(self):
        if self.kocsi.overlaps_with(self.kocsi2):
            self.kocsi.set_x(self.kocsi.x + 100)

    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    def __init__(self):
        super().__init__()

        music.play('proba.mp3')

        self.alap = MyActor(image="hatter_jatek.png", pos=(0, 0), anchor=(0, 0))
        self.alap.set_size(width=self.screen_width, height=self.screen_height)
        self.add_actor(self.alap)

        self.kocsi = MyActor(image="seat_ibiza_19tdi.png", pos=(980, 630), anchor=(0, 0))
        self.add_actor(self.kocsi)

        self.kocsi2 = MyActor(image="bmw_m4_comp.png", pos=(randint(650, 700), -400))
        self.add_actor(self.kocsi2)

        self.kocsi1 = MyActor(image="bmw_m4_comp.png", pos=(randint(1000, 1200), -400))
        self.add_actor(self.kocsi1)

        self.set_on_key_down_listener(self.keydownlistener)
        self.set_on_key_up_listener(self.keyuplistener)
