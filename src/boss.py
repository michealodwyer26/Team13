import pygame as pg
import random
from src.globals import *

class Boss(pg.sprite.Sprite):
    def __init__(self, position, groups, collisions, player):
        super().__init__(groups)
        self._collisions = collisions
        self._player = player

        self._v = pg.math.Vector2(0, 0)
        self._speed = 25
        self._health = 1000
        self._damage_filter = 0

        self._idle_animation = []
        self._left_attack = []
        self._right_attack = []
        self._frame_index = 0
        self._animation_timer = 0

        self.load_animations()
        
        self.image = self._idle_animation[0]
        self.rect = self.image.get_rect(topleft = position)

    def update(self):
        self.update_direction()
        self.animate()  

    def check_collisions(self):
        for s in self._collisions:
            if s.rect.colliderect(self.rect):
                if isinstance(s, Boss):
                    pass
                else: 
                    return True
        return False
    
    def damage(self):
        self._health -= random.randint(5, 10) 
        self.rect.x -= self._v.x * 5 
        self.rect.y -= self._v.y * 5

        if self._health <= 0:
            self.kill()

    
    def load_frame(self, rect, sprite_sheet):
        rectangle = pg.Rect(rect)
        frame = pg.Surface(rectangle.size, pg.SRCALPHA)
        frame.blit(sprite_sheet, (0, 0), rectangle)
        return pg.transform.scale(frame, (64, 64))

    def update_direction(self):
        # if self._v.magnitude() != 0:
        #     self._v = self._v.normalize()
        if self.check_collisions():
            self.rect.topleft -= self._v * self._speed

        if self._player.rect.x >= self.rect.x:
            self._v.x = 1
        else:
            self._v.x = -1

        if self._player.rect.y >= self.rect.y:
            self._v.y = 1 
        else:
            self._v.y = -1

        
    def move(self):
        self.rect.topleft += self._v * self._speed
        if self.check_collisions():
            self.rect.topleft -= self._v * self._speed       
        

    def animate(self):
        self.image = self._idle_animation[self._frame_index]
        if self._v.x == -1:
            self.image = pg.transform.flip(self._idle_animation[self._frame_index], True, False)
        self._animation_timer += 1

        if self._animation_timer > 15:
            self._frame_index += 1
            if self._frame_index == 3:
                self._frame_index = 0
            self._animation_timer = 0
            self.move()

    def load_animations(self):
        sprite_sheet = pg.image.load("assets/characters/boss/attacking.png").convert_alpha()
        for x in range(0, 501, 100):
            self._idle_animation.append(pg.transform.scale(self.load_frame((x, 0, 100, 100), sprite_sheet), (128*1.5, 128*1.5)))
        for x in range(0, 501, 100):
            self._idle_animation.append(pg.transform.scale(self.load_frame((x, 100, 100, 100), sprite_sheet), (128*1.5, 128*1.5)))
        for _ in range(0, 5):
            self._idle_animation.append(pg.transform.scale(self.load_frame((0, 200, 100, 100), sprite_sheet), (128*1.5, 128*1.5)))