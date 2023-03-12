import pygame as pg 
import pytmx
from src.player import Player 
from src.enemy import Enemy
from src.globals import *
from src.ui import UI
from src.boss import Boss


class Obstacle(pg.sprite.Sprite):
    def __init__(self, groups, rect):
        super().__init__(groups)
        self.rect = rect 

class Dungeon:
    def __init__(self):
        self._screen = pg.display.get_surface()
        self._sprites = pg.sprite.Group()
        self._obstacles = pg.sprite.Group()
        self._player = Player(((S_WIDTH - TILE_SIZE) / 2, (S_HEIGHT - TILE_SIZE) / 2), [self._sprites], self._obstacles, True)
        self._boss = Boss((300, 210), [self._sprites, self._obstacles], self._obstacles, self._player)

        self._map = pg.transform.scale(pg.image.load("assets/tilemaps/dungeon2.png").convert(), (1280, 768))
        self._map_rect = self._map.get_rect()
        self.ui = UI()
        self.font = pg.font.Font(UI_FONT, 26)
        


        self._map_rect.topleft = (0, -50)
        self._tiled_map = pytmx.TiledMap('assets/tilemaps/dungeon.tmx')
        self._tm = pytmx.load_pygame("assets/tilemaps/dungeon.tmx", pixelalpha=True)
        self.load_map_objects()

        background_music = pg.mixer.Sound("assets/sounds/dungeon.mp3")
        background_music.play(loops = -1)
    
        
    def run(self):
        self._screen.blit(self._map, self._map_rect)
        self._sprites.draw(self._screen) 
        self.update()
        self.ui.display(self._player)
        if self._boss._health < 0:
            self._screen.fill((0, 0, 0))
            text = self.font.render("Congratulations!", False, (255, 255, 255))
            text2 = self.font.render("You completed the mission...", False, (255, 255, 255))
            self._screen.blit(text, (S_WIDTH / 2 - text.get_rect().width / 2, 300))
            self._screen.blit(text2, (S_WIDTH / 2 - text2.get_rect().width / 2, 400))



    def load_map_objects(self):
        for obj in self._tm.objects:
            Obstacle(self._obstacles, pg.Rect((obj.x*2, obj.y*2 - 50), (obj.width*2, obj.height*2)))

    def update(self):
        self._sprites.update()
        self.update_camera()

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
        

        

        
