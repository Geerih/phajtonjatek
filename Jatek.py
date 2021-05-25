from n_mygameworld import *
import pgzrun

gamestage = MyStage()

WIDTH = 1920
HEIGHT = 1080

kocsi = MyActor(image="seat_ibiza_19tdi.png", pos=(0, 0), anchor=(0, 0))
gamestage.add_actor(kocsi)

def update(dt):
    gamestage.update(dt)

def draw():
    gamestage.draw()




pgzrun.go()