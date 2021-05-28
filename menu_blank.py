from n_mygameworld import *
from fomenu import *

class BlankStage(MyStage):

    def keydown(self, key, mod, unicode):
        print(key)
        if key == keys.ESCAPE:
            self.menu.menu_Main()

    def __init__(self, menu: 'Menustage'):
        super().__init__()
        self.menu = menu
        self.set_on_mouse_down_listener(self.keydown())