from n_mygameworld import *
import tkinter as tk
from random import randint

class Gamestage(MyStage):

    def keydownlistener(self, key, mod, unicode):
        if key == keys.UP:
            animate(self.kocsi, pos=(self.kocsi.pos[0], self.kocsi.pos[1] - 100), duration=0.1)
        if key == keys.DOWN:
            animate(self.kocsi, pos=(self.kocsi.pos[0], self.kocsi.pos[1] + 100), duration=0.1)
        if key == keys.LEFT:
            animate(self.kocsi, pos=(self.kocsi.pos[0] - 50, self.kocsi.pos[1]), duration=0.1)
        if key == keys.RIGHT:
            animate(self.kocsi, pos=(self.kocsi.pos[0] + 50, self.kocsi.pos[1]), duration=0.1)

    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    def __init__(self):
        super().__init__()

        self.alap = MyActor(image="hatter_jatek.png", pos=(0, 0), anchor=(0, 0))
        self.alap.set_size(width=self.screen_width, height=self.screen_height)
        self.add_actor(self.alap)

        self.kocsi = MyActor(image="seat_ibiza_19tdi.png", pos=(980, 630), anchor=(0, 0))
        self.add_actor(self.kocsi)

        self.kocsi2 = MyActor(image="bmw_m4_comp.png", pos=(980, 630), anchor=(0, 0))
        self.add_actor(self.kocsi2)

        #self.kocsi1 = MyActor(image="bmw_m4_comp.png")
        #self.kocsi1.pos = randint(0, 800), randint(-800, 0)
        #self.add_actor(self.kocsi1)

        self.set_on_key_down_listener(self.keydownlistener)
