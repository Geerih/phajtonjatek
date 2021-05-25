from n_mygameworld import *
import pgzrun


menustage = MyStage()

m1 = MyActor(image="kezdokep.png", pos=(0, 0), anchor=(0, 0))
m1.set_width(1920)
menustage.add_actor(m1)

def update(dt):
    menustage.update(dt)

def draw():
    menustage.draw()




pgzrun.go()