from turtle import Screen
from n_mygameworld import *
import pgzrun
import tkinter as tk

gamestage = MyStage()

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
WIDTH = screen_width
HEIGHT = screen_height
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

WIDTH = screen_width
HEIGHT = screen_height
print(screen_width)
print(screen_height)

alap = MyActor(image="game_backkground.png", pos=(0, 0), anchor=(0, 0))
alap.set_size(width=screen_width, height=screen_height)
gamestage.add_actor(alap)

kocsi = MyActor(image="seat_ibiza_19tdi.png", pos=(0, 0), anchor=(0, 0))
gamestage.add_actor(kocsi)

def update(dt):
    gamestage.update(dt)


class MyText:
    text: str = "Menu"
    color = (0, 0, 153)
    alpha: float = 1
    background = None
    fontname = None
    fontsize = 32

    def set_color(self, r: int, g: int, b: int, a: float = 1):
        self.color = (r, g, b)
        self.alpha = a

    def set_background(self, r: int, g: int, b: int):
        self.color = (r, g, b)

    def set_text(self, text: str):
        self.text = text

    def set_alpha(self, a: float):
        self.alpha = a

    def set_fontname(self, fontname: str):
        self.fontname = fontname

    def set_fontsize(self, size: float):
        self.fontsize = size


class MyLabel(MyText):

    _stage: 'MyStage' = 0
    elapsed_time: float = 0

    def set_stage(self, stage: 'MyStage'):
        self._stage = stage

    def __init__(self, pos=(0, 0), angle=0):
        self.x: int = pos[0]
        self.y: int = pos[1]
        self.angle: int = angle

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y

    def update(self, deltaTime: float = 0.0166666666666666666666):
        self.elapsed_time += deltaTime

    def draw(self):
        Screen(pygame.display.get_surface()).draw.text(self.text, (self.x, self.y), angle=self.angle, color=self.color, background=self.background, fontname=self.fontname, fontsize=self.fontsize, alpha=self.alpha)

    def set_rotation(self, angle: int):
        self.angle = angle


class MyButton(MyActor, MyText):

    def __init__(self, image="credit.png", pos=(0, 0), anchor=(0, 0), width:int=256, height:int=64, **kwargs):
        super().__init__(image, pos, anchor, **kwargs)
        self.set_size(width, height)
        self.set_x(20)
        self.set_y(80)

    def draw(self):
        super().draw()
        Screen(pygame.display.get_surface()).draw.text(self.text, (self.x, self.y), angle=self.angle, color=self.color, background=self.background, fontname=self.fontname, fontsize=self.fontsize, alpha=self.alpha)

def draw():
    gamestage.draw()


pgzrun.go()