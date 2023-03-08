import pygame as pg 
import sys 

from src.globals import *
from src.Intro import Intro
from src.scene import Scene

pg.init()
pg.display.set_caption("The Legend of Pyda")
icon = pg.image.load('assets/sword_logo.png')
pg.display.set_icon(icon)

class Main:
    def __init__(self):
        self._screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
        self._clock = pg.time.Clock()
        self._scene = Intro()
        self.counter = 0

    def run(self):
        running = True 
        while running:
            self._screen.fill((0, 0, 0))
            self._scene.run()
            if self.counter == 0:
                for e in pg.event.get():
                    if e.type == pg.QUIT:
                            pg.quit()
                            quit()
                    if e.type == pg.KEYDOWN :
                        if e.key == pg.K_y:
                            main._scene = Scene()
                            self.counter += 1
                            print("Good luck on your journey!")
            pg.display.update()
            self._clock.tick(FPS)

if __name__ == "__main__":
    main = Main() 
    main.run()