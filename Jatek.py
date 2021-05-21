import pgzrun
import pygame
from n_mygameworld import *
from n_staractor import StarActor


def keydownlistener(key, mod, unicode, keys):
    if key == keys.LEFT:
        animate(car1, pos=(car1.pos[0] - 10, car1.pos[1]), duration=0.1)
    if key == keys.RIGHT:
        animate(car1, pos=(car1.pos[0] + 10, car1.pos[1]), duration=0.1)


gamestage = MyStage()


def on_key_left(key, mod, unicode):
    print("LEFT: " + str(key) + " " + str(mod) + " " + str(unicode))
    gamestage.on_key_down(key, mod, unicode)


def on_key_right(key, mod):
    print("RIGHT: " + str(key) + " " + str(mod))
    gamestage.on_key_up(key, mod)


for i in range(100):
    gamestage.add_actor(StarActor())


def update(dt):
    gamestage.update(dt)


car1 = MyActor(image="kocsi_kek.png", pos=(0, 0), anchor=(0, 0))
car1.set_width(30, 30)

gamestage.add_actor(car1)

pgzrun.go()