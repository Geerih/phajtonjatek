from n_mygameworld import *
import pgzrun
import pygame

WIDTH  = 800
HEIGHT = 600

menustage = MyStage()

bg = MyActor(image="kezdokep.png", pos=(0, 0), anchor=(0, 0))
bg.set_width(30)
menustage.add_actor(bg)

def update(dt):
    menustage.update(dt)

def draw():
    menustage.draw()


pgzrun.go()