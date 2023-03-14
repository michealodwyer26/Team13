import pygame as pg
import random
from src.globals import *

class Health_Item(pg.sprite.Sprite):
    def __init__(self, position, groups, add_health):
        super().__init__(groups)

        self._v = pg.math.Vector2(0, -1)
        self.add_health = add_health

        self.image = pg.image.load("assets/objects/heart.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (self.image.get_rect().width / 1.5, self.image.get_rect().height / 1.5))
        
        self.rect = self.image.get_rect(topleft = position)
    
    def heal(self):
        self.add_health(10)
        self.kill()
        pg.mixer.Sound("assets/sounds/heartbeat.mp3").play()

class Strength_Item(pg.sprite.Sprite):
    def __init__(self, position, groups, add_strength):
        super().__init__(groups)

        self._v = pg.math.Vector2(0, -1)
        self.add_strength = add_strength

        self.image = pg.image.load("assets/objects/strength.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (self.image.get_rect().width / 37, self.image.get_rect().height / 37))
        
        self.rect = self.image.get_rect(topleft = position)
    
    def buff(self):
        self.add_strength(2)
        self.kill()
        pg.mixer.Sound("assets/sounds/heartbeat.mp3").play()
    

