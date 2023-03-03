import pygame as pg 
from src.player import Player 
from src.globals import *
from src.ui import UI

class Scene:
    def __init__(self):
        self._screen = pg.display.get_surface()
        self._sprites = pg.sprite.Group()
        self._obstacles = pg.sprite.Group()
        self._player = Player(((S_WIDTH - TILE_SIZE) / 2, (S_HEIGHT - TILE_SIZE) / 2), [self._sprites], self._obstacles)

        self._map = pg.transform.scale(pg.image.load("assets/tilemaps/map.png").convert(), (1280*2, 720*2))
        self._map_rect = self._map.get_rect()

        self.ui = UI()

        background_music = pg.mixer.Sound("assets/sounds/356_Adventure_Begins.mp3")
        background_music.play(loops = -1)
        
    def run(self):
        self._screen.blit(self._map, self._map_rect)
        self._sprites.draw(self._screen) 
        self.update()
        self.ui.display(self._player)

    def update(self):
        self._sprites.update()

        if (self._player.rect.x < (S_WIDTH / 2) - 64) or (self._player.rect.x > (S_WIDTH / 2) + 64):
            self._player._in_centre = True
            self._map_rect.topleft -= self._player._v * self._player._speed

        if (self._player.rect.y < (S_HEIGHT / 2) - 64) or (self._player.rect.y > (S_HEIGHT / 2) + 64):
            self._player._in_centre = True
            self._map_rect.topleft -= self._player._v * self._player._speed

        if (self._player.rect.x < (S_WIDTH / 2) + 64) or (self._player.rect.x > (S_WIDTH / 2) - 64):
            self._player._in_centre = False

        if (self._player.rect.y < (S_HEIGHT / 2) + 64) or (self._player.rect.y > (S_HEIGHT / 2) - 64):
            self._player._in_centre = False
