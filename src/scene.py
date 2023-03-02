import pygame as pg 
from src.player import Player 
from src.globals import *

class Scene:
    def __init__(self):
        self._screen = pg.display.get_surface()
        self._sprites = pg.sprite.Group()
        self._obstacles = pg.sprite.Group()
        self._player = Player(((S_WIDTH - TILE_SIZE) / 2, (S_HEIGHT - TILE_SIZE) / 2), [self._sprites], self._obstacles)

        self._map = pg.transform.scale(pg.image.load("assets/tilemaps/map.png").convert(), (1280*2, 720*2))
        self._map_rect = self._map.get_rect()
        
    def run(self):
        self._screen.blit(self._map, self._map_rect)
        self._sprites.draw(self._screen) 
        self.update()

    def update(self):
        self._sprites.update()
        self.update_camera()

    def update_camera(self):
        # if (self._player.rect.x < (S_WIDTH / 2) - 64) or (self._player.rect.x > (S_WIDTH / 2) + 64):
        #     self._player._in_centre = True
        #     self._map_rect.topleft -= self._player._v * self._player._speed

        # if (self._player.rect.y < (S_HEIGHT / 2) - 64) or (self._player.rect.y > (S_HEIGHT / 2) + 64):
        #     self._player._in_centre = True
        #     self._map_rect.topleft -= self._player._v * self._player._speed

        # if (self._player.rect.x < (S_WIDTH / 2) + 64) or (self._player.rect.x > (S_WIDTH / 2) - 64):
        #     self._player._in_centre = False

        # if (self._player.rect.y < (S_HEIGHT / 2) + 64) or (self._player.rect.y > (S_HEIGHT / 2) - 64):
        #     self._player._in_centre = False

        # if self._player.rect.x - 128/2 > S_WIDTH / 2:
        #     self._player._in_centre_x = True
        #     self._map_rect.x -= self._player._v.x * self._player._speed
        # if self._player.rect.y - 128/2 > S_HEIGHT / 2: 
        #     self._player._in_centre_y = True
        #     self._map_rect.x -= self._player._v.x * self._player._speed

        self._map_rect.topleft -= self._player._v * self._player._speed

        if self._map_rect.x + self._map_rect.width < S_WIDTH:
            self._map_rect.x = S_WIDTH - self._map_rect.width
        if self._map_rect.x > 0:
            self._map_rect.x = 0 
        if self._map_rect.y + self._map_rect.height < S_HEIGHT:
            self._map_rect.y = S_HEIGHT - self._map_rect.height 
        if self._map_rect.y > 0:
            self._map_rect.y = 0

        

        
