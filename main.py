import pygame as pg 
import sys 

from src.scene import Scene

pg.init()
pg.display.set_caption("Team 13")

class Main:
    def __init__(self):
        self._screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
        self._clock = pg.time.Clock()

    def run(self):
        running = True 
        while running:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()
                    quit()
                
            self._screen.fill((0, 0, 0))
            pg.display.update()
            self._clock.tick(FPS)

if __name__ == "__main__":
    main = Main() 
    main.run()