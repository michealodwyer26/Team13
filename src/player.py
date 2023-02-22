import pygame as pg 
from src.globals import * 

class Player(pg.sprite.Sprite):
    def __init__(self, position, groups, collisions):
        super().__init__(groups)
        self._sprite_sheet = pg.image.load("assets/characters/player.png").convert_alpha()
        # # self.image = pg.image.load("assets/player.png").convert_alpha()
        self.image = pg.transform.scale(self.load_frame((9, 17, 32, 32)), (64, 64))
        self.rect = self.image.get_rect(topleft = position)
        self._collisions = collisions
        

        self._v = pg.math.Vector2()
        self._speed = 3
        self._in_centre = False

        # self._animations = {'down': [], 'up': [], 'left': [], 'right': []}
        self._frame_index = 0
        self._animation_timer = 0
        self.down_animation = []
        self.load_animations()
        self.image = self.down_animation[self._frame_index]

    def read_key_input(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                    pg.quit()
                    quit()
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT:
                    self._v.x = -1
                elif e.key == pg.K_RIGHT:
                    self._v.x = 1
                elif e.key == pg.K_DOWN:
                    self._v.y = 1
                elif e.key == pg.K_UP:
                    self._v.y = -1

        pressed_keys = pg.key.get_pressed()

        if not pressed_keys[pg.K_UP] and not pressed_keys[pg.K_DOWN] and not pressed_keys[pg.K_RIGHT] and not pressed_keys[pg.K_LEFT]:
            self._v.x = 0
            self._v.y = 0

    def check_collisions(self):
        for s in self._collisions:
            if s.rect.colliderect(self.rect):
                return True
        return False

    def move(self):
        self.rect.topleft += self._v * self._speed
        if self.check_collisions() or self._in_centre:
            self.rect.topleft -= self._v * self._speed

    def update(self):
        self.read_key_input()
        self.move()
        self.image = self.down_animation[self._frame_index]
        if self._v.x > 0 or self._v.y > 0: 
            self._animation_timer += 1
        if self._animation_timer > 20:
            self._frame_index += 1
            if self._frame_index == 5:
                self._frame_index = 0 
            self._animation_timer = 0

    def load_frame(self, rect):
        rectangle = pg.Rect(rect)
        frame = pg.Surface(rectangle.size, pg.SRCALPHA)
        frame.blit(self._sprite_sheet, (0, 0), rectangle)
        return pg.transform.scale(frame, (64, 64))
    
    def load_animations(self):
        for x in range(9, 249, 48): 
            self.down_animation.append(self.load_frame((x, 160, 32, 32)))
        for x in range(9, 249, 48): 
            self.down_animation.append(self.load_frame((x, 160, 32, 32)))
        
