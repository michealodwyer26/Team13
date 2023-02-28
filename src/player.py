import pygame as pg 
from src.globals import * 

class Player(pg.sprite.Sprite):
    def __init__(self, position, groups, collisions):
        super().__init__(groups)
        self._collisions = collisions
        
        self._v = pg.math.Vector2()
        self._speed = 3
        self._in_centre = False

        self._animations = {'walk_down': [], 'walk_up': [], 'walk_left': [], 'walk_right': [],
                            'attack_down': [], 'attack_up': [], 'attack_left': [], 'attack_right': []}
        self._animation_state = 'walk_down'
        self._frame_index = 0
        self._animation_timer = 0

        self.load_animations()

        self.image = self._animations[self._animation_state][self._frame_index]
        self.rect = self.image.get_rect(topleft = position)

    def read_key_input(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                    pg.quit()
                    quit()
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT:
                    self._v.x = -1
                    self._animation_state = "walk_left"
                elif e.key == pg.K_RIGHT:
                    self._v.x = 1
                    self._animation_state = "walk_right"
                elif e.key == pg.K_DOWN:
                    self._v.y = 1
                    self._animation_state = "walk_down"
                elif e.key == pg.K_UP:
                    self._v.y = -1
                    self._animation_state = "walk_up"

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
        if self._v.magnitude() != 0:
            self._v = self._v.normalize()
        self.rect.topleft += self._v * self._speed
        if self.check_collisions() or self._in_centre:
            self.rect.topleft -= self._v * self._speed

    def update(self):
        self.read_key_input()
        self.move()
        self.animate() 

    def animate(self):
        self.image = self._animations[self._animation_state][self._frame_index]

        self._animation_timer += 1

        if self._animation_timer > 15:
            self._frame_index += 1
            if self._frame_index == 5:
                self._frame_index = 0 
            self._animation_timer = 0

    def load_frame(self, rect, sprite_sheet):
        rectangle = pg.Rect(rect)
        frame = pg.Surface(rectangle.size, pg.SRCALPHA)
        frame.blit(sprite_sheet, (0, 0), rectangle)
        return pg.transform.scale(frame, (64, 64))
    
    def load_animations(self):
        for state in self._animations.keys():
            if "walk" in state:
                sprite_sheet = pg.image.load("assets/characters/player/{}.png".format(state)).convert_alpha()
                for x in range(0, 193, 64):
                    self._animations[state].append(pg.transform.scale(self.load_frame((x, 0, 64, 64), sprite_sheet), (128, 128)))
                for x in range(0, 129, 64):
                    self._animations[state].append(pg.transform.scale(self.load_frame((x, 64, 64, 64), sprite_sheet), (128, 128)))
