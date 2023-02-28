import pygame as pg 
import sys 

from src.globals import *
from src.scene import Scene

pg.init()
pg.display.set_caption("The Legend of Pyda")
icon = pg.image.load('assets/characters/player.png')
pg.display.set_icon(icon)

class Main:
    def __init__(self):
        self._screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
        self._clock = pg.time.Clock()
        self._scene = Scene()

    def run(self):
        running = True 
        while running:
            self._screen.fill((0, 0, 0))
            self._scene.run()
            pg.display.update()
            self._clock.tick(FPS)

if __name__ == "__main__":
    main = Main() 
    main.run()