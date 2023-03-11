import pygame as pg
import random
from src.globals import *

class Enemy(pg.sprite.Sprite):
    def __init__(self, position, groups, collisions, attack, scene, player):
        super().__init__(groups)
        self._collisions = collisions

        self.enemy_v = pg.math.Vector2(0, -1)
        self._speed = 0.5
        self._health = 250
        self._damage_filter = 0

        self._animation = []
        self._die_animation = []
        self._frame_index = 0
        self._animation_timer = 0
        self.add_exp = scene.add_exp
        self.spawn_wave = scene.spawn_wave
        self.player = player
        self.attack = attack

        self.load_animations()
        
        self.image = self._animation[0]
        self.rect = self.image.get_rect(topleft = position)

    def update(self):
        self.move()
        self.animate()  
        self.attack()

    def check_collisions(self):
        for s in self._collisions:
            if isinstance(s, Enemy):
                return True
        return False
    
    def damage(self, damage):
        self._health -= damage
        if self._health <= 0:
            self.kill()
            self.spawn_wave()
            self.add_exp(random.randint(10,40))
            pg.mixer.Sound("assets/sounds/slime_pop.mp3").play()
    
    def load_frame(self, rect, sprite_sheet):
        rectangle = pg.Rect(rect)
        frame = pg.Surface(rectangle.size, pg.SRCALPHA)
        frame.blit(sprite_sheet, (0, 0), rectangle)
        return pg.transform.scale(frame, (64, 64))

    def move(self):
        if self.enemy_v.magnitude() != 0:
            self.enemy_v = self.enemy_v.normalize() 
        rand = random.randint(0, 3)
        if rand == 0:
            self.enemy_v.x = -1
        elif rand == 1:
            self.enemy_v.y = -1
        elif rand == 2:
            self.enemy_v.x = 1
        elif rand == 3:
            self.enemy_v.y = 1
        if self._damage_filter > 0:
            self._damage_filter -= 1
        if self.check_collisions():
            self.rect.topleft += self.enemy_v * self._speed
    

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