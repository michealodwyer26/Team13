import pygame as pg 
import pytmx
from src.player import Player
from src.scene import Scene
from src.globals import *
from src.ui import UI


class Obstacle(pg.sprite.Sprite):
    def __init__(self, groups, rect):
        super().__init__(groups)
        self.rect = rect 

class Intro:
    def __init__(self):
        self._screen = pg.display.get_surface()
        self._scene = Scene()
        self._sprites = pg.sprite.Group()
        self._obstacles = pg.sprite.Group()
        self._player = Player(((S_WIDTH - TILE_SIZE) / 2, (S_HEIGHT - TILE_SIZE) / 2), [self._sprites], self._obstacles, True)

        self._map = pg.transform.scale(pg.image.load("assets/tilemaps/Intro.png").convert(), (320*2, 320*2))
        self._map_rect = self._map.get_rect()
        self.ui = UI()

        self._map_rect.topleft = (S_WIDTH/2 - 320, S_HEIGHT / 2 - 320)
        self._tiled_map = pytmx.TiledMap('assets/tilemaps/Intro.tmx')
        self._tm = pytmx.load_pygame("assets/tilemaps/Intro.tmx", pixelalpha=True)
        self.load_map_objects()
    
        
    def run(self):
        self._screen.blit(self._map, self._map_rect)
        self._sprites.draw(self._screen) 
        self.update()
        self.ui.display(self._player)

    def load_map_objects(self):
        for obj in self._tm.objects:
            Obstacle(self._obstacles, pg.Rect((obj.x*2 + 320, obj.y*2 + 40), (obj.width*2, obj.height*2)))

    def update(self):
        self._sprites.update()
        # self.update_camera()
        self.is_ready()
        self.ui.display_dialogue(self._player)

    def is_ready(self):
        return self._player._ready

    
    # def update_camera(self):
    #     self._map_rect.topleft -= self._player._v * self._player._speed
    #     for obj in self._obstacles:
    #             obj.rect.topleft -= self._player._v * self._player._speed

    #     if self._player.check_collisions():
    #         self._map_rect.topleft += self._player._v * self._player._speed
    #         for obj in self._obstacles:
    #             obj.rect.topleft += self._player._v * self._player._speed

    #     if self._map_rect.x + self._map_rect.width < S_WIDTH:
    #         self._map_rect.x = S_WIDTH - self._map_rect.width
    #         for obj in self._obstacles:
    #             obj.rect.topleft += self._player._v * self._player._speed
    #     if self._map_rect.x > 0:
    #         self._map_rect.x = 0
    #         for obj in self._obstacles:
    #             obj.rect.topleft += self._player._v * self._player._speed
    #     if self._map_rect.y + self._map_rect.height < S_HEIGHT:
    #         self._map_rect.y = S_HEIGHT - self._map_rect.height 
    #         for obj in self._obstacles:
    #             obj.rect.topleft += self._player._v * self._player._speed
    #     if self._map_rect.y > 0:
    #         self._map_rect.y = 0
    #         for obj in self._obstacles:
    #             obj.rect.topleft += self._player._v * self._player._speed
        

        

        
