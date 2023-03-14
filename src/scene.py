import pygame as pg 
import pytmx
from src.player import Player 
from src.enemy import Enemy
from src.globals import *
from src.ui import UI
from src.object import Health_Item, Strength_Item


class Obstacle(pg.sprite.Sprite):
    def __init__(self, groups, rect):
        super().__init__(groups)
        self.rect = rect 

class Scene:
    def __init__(self):
        self._screen = pg.display.get_surface()
        self._sprites = pg.sprite.Group()
        self._obstacles = pg.sprite.Group()
        self._player = Player(((S_WIDTH - TILE_SIZE) / 2, (S_HEIGHT - TILE_SIZE) / 2), [self._sprites], self._obstacles, False)

        for id, pos in enumerate(enemy_tile_positions):
            Enemy((pos[0]*16*1.5 - 676, pos[1]*16*1.5 - 3132), [self._sprites, self._obstacles], self._obstacles, self.add_exp, self._player, id)

        self._health_item = Health_Item((400, 600), [self._sprites, self._obstacles], self.add_health)
        self._strength_item = Strength_Item((400, 500), [self._sprites, self._obstacles], self.add_strength)

        self._map = pg.transform.scale(pg.image.load("assets/tilemaps/map2.png").convert(), (200*16*1.5, 200*16*1.5))
        self._map_rect = self._map.get_rect()

        self.ui = UI()
        self._map_rect.topleft = (-676, -3132)
        self._tiled_map = pytmx.TiledMap('assets/tilemaps/map2.tmx')
        self._tm = pytmx.load_pygame("assets/tilemaps/map2.tmx", pixelalpha=True)
        self.load_map_objects()
    
        background_music = pg.mixer.Sound("assets/sounds/356_Adventure_Begins.mp3")
        background_music.play(loops = -1)
        
    def run(self):
        self._screen.blit(self._map, self._map_rect)
        self._sprites.draw(self._screen) 
        self.update()
        self.ui.display(self._player)

    def load_map_objects(self):
        for obj in self._tm.objects:
            Obstacle(self._obstacles, pg.Rect((obj.x*1.5 - 676, obj.y*1.5 - 3132), (obj.width*1.5, obj.height*1.5)))

    def add_exp(self, amount):
        self._player.exp += amount
    
    def add_health(self, amount):
        self._player.health += amount
    
    def add_strength(self, amount):
        self._player.strength += amount
    
    def check_exp(self):
        return self._player.exp

    def update(self):
        self._sprites.update()
        self.update_camera()
        print(self._map_rect.x, self._map_rect.y)

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
        

        

        
