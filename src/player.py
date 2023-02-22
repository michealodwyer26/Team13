import pygame as pg 
from src.globals import * 

class Player(pg.sprite.Sprite):
    def __init__(self, position, groups, collisions):
        super().__init__(groups)
        self.image = pg.image.load("assets/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        self._collisions = collisions

        self._v = pg.math.Vector2()
        self._speed = 3
        self._in_centre = False

    def read_key_input(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                    pg.quit()
                    quit()
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT:
                    self._v.x = -1
                elif e.key == pg.K_RIGHT:
                    self._v.x = 1
                elif e.key == pg.K_DOWN:
                    self._v.y = 1
                elif e.key == pg.K_UP:
                    self._v.y = -1

        pressed_keys = pg.key.get_pressed()
        if not pressed_keys[pg.K_UP] and not pressed_keys[pg.K_DOWN] and not pressed_keys[pg.K_RIGHT] and not pressed_keys[pg.K_LEFT]:
            self._v.x = 0
            self._v.y = 0

    def check_collisions(self):
        for s in self._collisions:
            if s.rect.colliderect(self.rect):
                return True
        return False

    def move(self):
        self.rect.topleft += self._v * self._speed
        if self.check_collisions() or self._in_centre:
            self.rect.topleft -= self._v * self._speed

    def update(self):
        self.read_key_input()
        self.move()