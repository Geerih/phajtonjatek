from n_mygameworld import *
#from n_menu_blank import *
from gamestage import *
#from n_menu_main import scr

class Menustage(MyStage):

    def menu_Main(self, pos=0, btn=0):
        self.onscreenstage = self

    def menu_Game(self, pos=0, btn=0):
        self.onscreenstage = Gamestage(self)

    #def menu_Blank(self, pos=0, btn=0):
        #self.onscreenstage = BlankStage(self)

    def menu_Exit(self, pos=0, btn=0):
        exit()

    def __init__(self):
        super().__init__()

        menuitem1: MyActor = MyActor("car.png", pos=(100, 100), anchor=(0, 0))
        self.add_actor(menuitem1)
        menuitem1.set_on_mouse_down_listener(self.menu_Game)

        menuitem2: MyActor = MyActor("car.png", pos=(100, 250), anchor=(0, 0))
        self.add_actor(menuitem2)
        menuitem2.set_on_mouse_down_listener(self.menu_Exit)

        #menuitem3: MyActor = MyActor("star.png", pos=(300, 250), anchor=(0, 0))
        #self.add_actor(menuitem3)
        #menuitem3.set_on_mouse_down_listener(self.menu_Blank)

        text1: MyLabel = MyLabel()
        text1.set_x(40)
        text1.set_rotation(-20)
        self.add_actor(text1)


        text2: MyButton = MyButton()
        text2.set_x(140)
        text2.set_y(100)
        self.add_actor(text2)

        self.onscreenstage : MyStage = self

        #self.ttt = MyMultiTickTimer(self.tikk, interval=1, count=3)
        #self.add_timer(self.ttt)

        #self.add_timer(MyMultiTickTimer(self.tikk, startdelay=1, interval=0.2, count=3))
        #text2.add_timer(MyTickTimer(self.tikk))

    #def tikk(self, timer: MyMultiTickTimer):
        #print("TIKK " + str(timer.count))

    def draw(self):
        if self == self.onscreenstage:
            super(Menustage, self).draw()
        else:
            self.onscreenstage.draw()

    def update(self, delta_time: float = 0.0166666666666666666666):
        if self == self.onscreenstage:
            super(Menustage, self).update(delta_time)
        else:
            self.onscreenstage.update(delta_time)

    def on_mouse_down(self, pos, button):
        if self == self.onscreenstage:
            super(Menustage, self).on_mouse_down(pos, button)
        else:
            self.onscreenstage.on_mouse_down(pos, button)

    def on_key_down(self, key, mod, unicode):
        if self == self.onscreenstage:
            super().on_key_down(key, mod, unicode)
        else:
            self.onscreenstage.on_key_down(key, mod, unicode)



