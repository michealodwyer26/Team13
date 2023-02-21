import pygame as pg 
from src.player import Player 

class Scene:
    def __init__(self):
        self._screen = pg.display.get_surface()
        self._sprites = pg.sprite.Group()
        self._obstacles = pg.sprite.Group()
        self._player = Player((100, 100), [self._sprites], self._obstacles)

    def run(self):
        pass 

    def update(self):
        self._sprites.draw(self._screen)
        self._sprites.update()