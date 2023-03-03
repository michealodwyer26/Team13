import pygame as pg
import random
from src.globals import *
class Enemy(pg.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        # self._collisions = collisions

        self._v = pg.math.Vector2(0, -1)
        self._speed = 0.5
        self._health = 100
        self._damage_filter = 0

        self._animation = []
        self._die_animation = []
        self._frame_index = 0
        self._animation_timer = 0

        self.load_animations()
        
        self.image = self._animation[0]
        self.rect = self.image.get_rect(topleft = position)

    def update(self):
        self.move()
        self.animate()  

    def check_collisions(self):
        for s in self._collisions:
            if s.rect.colliderect(self.rect):
                return True
        return False
    
    def damage(self):
        self._health -= 10 
        if self._health < 0:
            self.kill()
    
    def load_frame(self, rect, sprite_sheet):
        rectangle = pg.Rect(rect)
        frame = pg.Surface(rectangle.size, pg.SRCALPHA)
        frame.blit(sprite_sheet, (0, 0), rectangle)
        return pg.transform.scale(frame, (64, 64))

    def move(self):
        if self._v.magnitude() != 0:
            self._v = self._v.normalize()
        self.rect.topleft += self._v * self._speed
        # if self.check_collisions():
        #     self.rect.topleft -= self._v * self._speed

        rand = random.randint(0, 20)
        if rand == 0:
            self._v.x = -1
        if rand == 1:
            self._v.y = -1
        if rand == 2:
            self._v.x = 1
        if rand == 3:
            self._v.y = 1
        if self._damage_filter > 0:
            self._damage_filter -= 1
        
        

    def animate(self):
        self.image = self._animation[self._frame_index]
        self._animation_timer += 1

        if self._animation_timer > 15:
            self._frame_index += 1
            if self._frame_index == 6:
                self._frame_index = 0
            self._animation_timer = 0

    def load_animations(self):
        sprite_sheet = pg.image.load("assets/characters/slime.png").convert_alpha()
        for x in range(0, 193, 32):
            self._animation.append(pg.transform.scale(self.load_frame((x, 64, 32, 32), sprite_sheet), (64, 64)))
        for x in range(0, 129, 32):
            self._die_animation.append(pg.transform.scale(self.load_frame((x, 128, 32, 32), sprite_sheet), (64, 64)))