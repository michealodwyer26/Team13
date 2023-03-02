import pygame as pg
from globals import *

class Enemy(pg.sprite.Sprite):
    def __init__(self,enemy_name,position,groups,collisions):
        super().__init__(groups)
        self.image = pg.image.load("assets/zombie.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        self._collisions = collisions

        self._v = pg.math.Vector2()
        self._speed = 3

    def check_collisions(self):
        for s in self._collisions:
            if s.rect.colliderect(self.rect):
                return True
        return False

    def move(self):
        if self._v.magnitude() != 0:
            self._v = self._v.normalize()
        self.rect.topleft += self._v * self._speed
        if self.check_collisions():
            self.rect.topleft -= self._v * self._speed