import pygame as pg 
import pytmx
from src.player import Player 
from src.enemy import Enemy
from src.globals import *
from src.ui import UI
import main
from src.scene import Scene


class Obstacle(pg.sprite.Sprite):
    def __init__(self, groups, rect):
        super().__init__(groups)
        self.rect = rect 

class Intro:
    def __init__(self):
        self._screen = pg.display.get_surface()
        self._sprites = pg.sprite.Group()
        self._obstacles = pg.sprite.Group()
        self._player = Player(((S_WIDTH - TILE_SIZE) / 2, (S_HEIGHT - TILE_SIZE) / 2), [self._sprites], self._obstacles)

        self._map = pg.transform.scale(pg.image.load("assets/tilemaps/Intro.png").convert(), (1280, 768))
        self._map_rect = self._map.get_rect()

        self._map_rect.topleft = (-800, -300)
        self._tiled_map = pytmx.TiledMap('assets/tilemaps/Intro.tmx')
        self._tm = pytmx.load_pygame("assets/tilemaps/Intro.tmx", pixelalpha=True)
        self.load_map_objects()
    
        
    def run(self):
        self._screen.blit(self._map, self._map_rect)
        self._sprites.draw(self._screen) 
        self.update()

    def load_map_objects(self):
        for obj in self._tm.objects:
            Obstacle(self._obstacles, pg.Rect((obj.x*2 - 800, obj.y*2 - 300), (obj.width*2, obj.height*2)))

    def read_key_input(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                    pg.quit()
                    quit()
            if e.type == pg.KEYDOWN :
                if e.key == pg.K_y:
                    main._scene = Scene()
                    print("Hello")

    def update(self):
        self._sprites.update()
        self.update_camera()
        self.read_key_input()

    def update_camera(self):
        self._map_rect.topleft -= self._player._v * self._player._speed
        for obj in self._obstacles:
                obj.rect.topleft -= self._player._v * self._player._speed

        if self._player.check_collisions():
            self._map_rect.topleft += self._player._v * self._player._speed
            for obj in self._obstacles:
                obj.rect.topleft += self._player._v * self._player._speed

        if self._map_rect.x + self._map_rect.width < S_WIDTH:
            self._map_rect.x = S_WIDTH - self._map_rect.width
            for obj in self._obstacles:
                obj.rect.topleft += self._player._v * self._player._speed
        if self._map_rect.x > 0:
            self._map_rect.x = 0
            for obj in self._obstacles:
                obj.rect.topleft += self._player._v * self._player._speed
        if self._map_rect.y + self._map_rect.height < S_HEIGHT:
            self._map_rect.y = S_HEIGHT - self._map_rect.height 
            for obj in self._obstacles:
                obj.rect.topleft += self._player._v * self._player._speed
        if self._map_rect.y > 0:
            self._map_rect.y = 0
            for obj in self._obstacles:
                obj.rect.topleft += self._player._v * self._player._speed
        

        

        
