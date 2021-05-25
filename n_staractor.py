from random import *
from n_mygameworld import *

class StarActor(MyActor):
    __speed: float

    def __init__(self):
        r = Random()
        self.__speed = (r.random() - 0.5) * 50
        super().__init__('kocsi_kek.png', (r.randint(0, 600), r.randint(0, 600)))
        # self.setsize(20, 20)
        self.set_on_mouse_down_listener(self.click)

    def update(self, deltaTime: float = 0.0166666666666666666666):
        super().update(deltaTime)
        self.rotate_with(self.__speed * deltaTime)



