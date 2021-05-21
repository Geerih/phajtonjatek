import pgzrun
from typing import List
import pygame
from pgzero.builtins import *


class MyActor(Actor):

    elapsed_time: float = 0
    _stage: 'MyStage' = 0
    _on_mouse_down_listener = 0
    _on_mouse_up_listener = 0
    _on_mouse_move_listener = 0
    _on_key_up_listener = 0
    _on_key_down_listener = 0
    _w: int = -1
    _h: int = -1

    def update(self, deltaTime: float = 0.0166666666666666666666):
        self.elapsed_time += deltaTime

    def overlaps_with(self, otheractor: 'MyActor') -> bool:
        return self.colliderect(otheractor)

    def overlaps_point(self, pos) -> bool:
        return self.collidepoint(pos)

    def set_on_mouse_down_listener(self, func):
        self._on_mouse_down_listener = func

    def on_mouse_down(self, pos, button):
        if self.overlaps_point(pos):
            if self._on_mouse_down_listener != 0:
                self._on_mouse_down_listener(pos, button)

    def set_on_mouse_up_listener(self, func):
        self._on_mouse_up_listener = func

    def on_mouse_up(self, pos, button):
        if self.overlaps_point(pos):
            if self._on_mouse_up_listener != 0:
                self._on_mouse_up_listener(pos, button)

    def set_on_mouse_move_listener(self, func):
        self._on_mouse_move_listener = func

    def on_mouse_move(self, pos):
        if self.overlaps_point(pos):
            if self._on_mouse_move_listener != 0:
                self._on_mouse_move_listener(pos)

    def remove_from_stage(self):
        try:
            self._stage.remove_actor(actor=self)
        except ValueError:
            print("A következő objektum már el lett távolítva korábban: " + str(id(self)))

    def remove_on_mouse_down_listener(self):
        self._on_mouse_down_listener = 0

    def remove_on_mouse_up_listener(self):
        self._on_mouse_up_listener = 0

    def remove_on_mouse_move_listener(self):
        self._on_mouse_move_listener = 0

    def on_key_down(self, key, mod, unicode):
        if self._on_key_down_listener != 0:
            self._on_key_down_listener(key, mod, unicode)

    def on_key_up(self, key, mod):
        if self._on_key_up_listener != 0:
            self._on_key_up_listener(key, mod)

    def set_on_key_down_listener(self, func):
        self._on_key_down_listener = func

    def set_on_key_up_listener(self, func):
        self._on_key_up_listener = func

    def remove_on_key_down_listener(self):
        self._on_key_down_listener = 0

    def remove_on_key_up_listener(self):
        self._on_key_up_listener = 0

    def set_image(self, image_url:str):
        self.image = image_url

    def set_size(self, width: int, height: int):
        if width == -1 and height == -1:
            if self._w == -1 and self._h == -1:
                self._surf = pygame.transform.scale(self._surf, (self.width, self.height))
            else:
                self._surf = pygame.transform.scale(self._surf, (self._w, self._h))
        else:
            self._surf = pygame.transform.scale(self._surf, (width, height))
            self._w = width
            self._h = height
        self._update_pos()

    def set_stage(self, stage: 'MyStage'):
        self._stage = stage

    def set_rotation(self, degree: int):
        self.angle = degree
        self.set_size(-1, -1)

    def rotate_with(self, degree: int):
        self.set_rotation(self.angle + degree)

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y

    def set_width(self, width: int, aspect_ratio: bool = True):
        if aspect_ratio:
            self.set_size(width, int(float(self._h) * (float(width) / float(self._w))))
        else:
            self.set_size(width, self._h)

    def set_height(self, height: int, aspect_ratio: bool = True):
        if aspect_ratio:
            self.set_size(int(float(self._w) * (float(height) / float(self._h))), height)
        else:
            self.set_size(self._w, height)

    def get_width(self)->int:
        return self._w

    def get_height(self)->int:
        return self._h

class MyStage:
    actors: List[MyActor]
    elapsedTime: float = 0
    _on_mouse_down_listener = 0
    _on_mouse_up_listener = 0
    _on_mouse_move_listener = 0
    _on_key_up_listener = 0
    _on_key_down_listener = 0

    def __init__(self):
        self.actors = []

    def update(self, deltaTime: float = 0.0166666666666666666666):
        self.elapsedTime += deltaTime
        for obj in self.actors:
            obj.update(deltaTime)

    def draw(self):
        for obj in self.actors:
            obj.draw()

    def add_actor(self, actor: MyActor):
        self.actors.append(actor)
        if actor._stage != 0:
            print("A következő actor át lett helyezve a " + str(id(actor._stage)) + " stageből a " + str(id(self)) + " stagebe.")
            actor.remove_from_stage()
        actor.set_stage(self)

    def remove_actor(self, actor: MyActor):
        self.actors.remove(actor)

    def on_mouse_down(self, pos, button):
        if self._on_mouse_down_listener != 0:
            self._on_mouse_down_listener(pos, button)
        for obj in self.actors:
            obj.on_mouse_down(pos, button)

    def on_mouse_up(self, pos, button):
        if self._on_mouse_up_listener != 0:
            self._on_mouse_up_listener(pos, button)
        for obj in self.actors:
            obj.on_mouse_up(pos, button)

    def on_mouse_move(self, pos):
        if self._on_mouse_move_listener != 0:
            self._on_mouse_move_listener(pos)
        for obj in self.actors:
            obj.on_mouse_move(pos)

    def on_key_down(self, key, mod, unicode):
        if self._on_key_down_listener != 0:
            self._on_key_down_listener(key, mod, unicode)
        for obj in self.actors:
            obj.on_key_down(key, mod, unicode)

    def on_key_up(self, key, mod):
        if self._on_key_up_listener != 0:
            self._on_key_up_listener(key, mod)
        for obj in self.actors:
            obj.on_key_up(key, mod)

    def set_on_key_down_listener(self, func):
        self._on_key_down_listener = func

    def set_on_key_up_listener(self, func):
        self._on_key_up_listener = func

    def remove_on_key_down_listener(self):
        self._on_key_down_listener = 0

    def remove_on_key_up_listener(self):
        self._on_key_up_listener = 0

    def remove_on_mouse_down_listener(self):
        self._on_mouse_down_listener = 0

    def remove_on_mouse_up_listener(self):
        self._on_mouse_up_listener = 0

    def remove_on_mouse_move_listener(self):
        self._on_mouse_move_listener = 0

    def set_on_mouse_down_listener(self, func):
        self._on_mouse_down_listener = func

    def set_on_mouse_up_listener(self, func):
        self._on_mouse_up_listener = func

    def set_on_mouse_move_listener(self, func):
        self._on_mouse_move_listener = func
