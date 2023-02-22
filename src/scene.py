import pygame as pg 
from src.player import Player 
from src.globals import *

class Scene:
    def __init__(self):
        self._screen = pg.display.get_surface()
        self._sprites = pg.sprite.Group()
        self._obstacles = pg.sprite.Group()
        self._player = Player((0, 0), [self._sprites], self._obstacles)

        self._map = pg.transform.scale(pg.image.load("assets/tilemaps/map.png").convert(), (1280*2, 720*2))
        self._map_rect = self._map.get_rect()

    def run(self):
        self._screen.blit(self._map, self._map_rect)
        self._sprites.draw(self._screen) 
        self.update()

    def update(self):
        self._sprites.update()

        if self._player.rect.x > S_WIDTH / 2:
            self._player._in_centre = True 
            self._map_rect.topleft -= self._player._v * self._player._speed