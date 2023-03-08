import pygame as pg
import random
from src.globals import *

class Object(pg.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)

        self._v = pg.math.Vector2(0, -1)

        self.image = pg.image.load("assets/objects/heart.png")
        
        self.rect = self.image.get_rect(topleft = position)

    def check_collisions(self):
        for s in self._collisions:
            if s.rect.colliderect(self.rect):
                return True
        return False