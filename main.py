import pygame as pg 
import sys 

from src.globals import *
from src.Intro import Intro
from src.scene import Scene
from src.Dungeon import Dungeon

pg.init()
pg.mixer.init()
pg.display.set_caption("The Legend of Pyda")
icon = pg.image.load('assets/sword_logo.png')
pg.display.set_icon(icon)

class Main:
    def __init__(self):
        self._screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
        self._clock = pg.time.Clock()
        self._scene = Dungeon()
        self.counter = 0
        self._background_music = pg.mixer.Sound("assets/sounds/intro.mp3")
        self._background_music.play(loops = -1)


    def run(self):
        running = True 
        while running:
            self._screen.fill((0, 0, 0))
            self._scene.run()
            if (isinstance(self._scene, Intro)):
                if (self._scene.is_ready() == True):
                    self._scene = Scene()
                    self._background_music.stop()
                    self._background_music = pg.mixer.Sound("assets/sounds/main_scene.mp3")
                    self._background_music.play(loops = -1)
            if (isinstance(self._scene, Scene)):
                if (self._scene.check_exp() >= 1000):
                    self._scene = Dungeon()
                    self._background_music.stop()
                    self._background_music = pg.mixer.Sound("assets/sounds/dungeon.mp3")
                    self._background_music.play(loops = -1)
            pg.display.update()
            self._clock.tick(FPS)

if __name__ == "__main__":
    main = Main() 
    main.run()