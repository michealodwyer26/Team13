import pygame as pg 
from src.globals import * 
from src.enemy import Enemy

class Player(pg.sprite.Sprite):
    def __init__(self, position, groups, collisions):
        super().__init__(groups)
        self._collisions = collisions
        
        self._v = pg.math.Vector2()

        self._animations = {'walk_down': [], 'walk_up': [], 'walk_left': [], 'walk_right': [],
                            'attack_down': [], 'attack_up': [], 'attack_left': [], 'attack_right': [],
                            'idle_down': [], 'idle_up': [], 'idle_left': [], 'idle_right': []}
        self._animation_state = 'walk_down'
        self._prev_animation_state = 'walk_down'
        self._frame_index = 0
        self._animation_timer = 0
        self._in_centre_x = False
        self._in_centre_y = False

        self.load_animations()

        self.image = self._animations[self._animation_state][self._frame_index]
        self.rect = self.image.get_rect(topleft = position)
        self.weapon_attack_sound = pg.mixer.Sound("assets/sounds/sword_swipe_sound.mp3")

        self.stats = {
            'health': 100,
            'strength': 10,
            'speed' : 4
        }
        self.health = self.stats['health']
        self.exp = 0
        self._speed = self.stats['speed']

    def read_key_input(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                    pg.quit()
                    quit()
            if e.type == pg.KEYDOWN and "attack" not in self._animation_state:
                if e.key == pg.K_LEFT or e.key == pg.K_a:
                    self._v.x = -1
                    self._v.y = 0
                    self._animation_state = "walk_left"
                    self._frame_index = 0
                elif e.key == pg.K_RIGHT or e.key == pg.K_d:
                    self._v.x = 1
                    self._v.y = 0
                    self._animation_state = "walk_right"
                    self._frame_index = 0
                elif e.key == pg.K_DOWN or e.key == pg.K_s:
                    self._v.x = 0
                    self._v.y = 1
                    self._animation_state = "walk_down"
                    self._frame_index = 0
                elif e.key == pg.K_UP or e.key == pg.K_w:
                    self._v.x = 0
                    self._v.y = -1
                    self._animation_state = "walk_up"
                    self._frame_index = 0
                elif e.key == pg.K_SPACE:
                    self._animation_state = self._animation_state.replace("walk", "attack")
                    self._animation_state = self._animation_state.replace("idle", "attack")
                    self._frame_index = 0
                    self.weapon_attack_sound.play()

        pressed_keys = pg.key.get_pressed()

        if not pressed_keys[pg.K_UP] and not pressed_keys[pg.K_DOWN] and not pressed_keys[pg.K_RIGHT] and not pressed_keys[pg.K_LEFT] and not pressed_keys[pg.K_w] and not pressed_keys[pg.K_a] and not pressed_keys[pg.K_s] and not pressed_keys[pg.K_d]:
            if "attack" not in self._animation_state:
                self._v.x = 0
                self._v.y = 0
                self._animation_state = self._animation_state.replace("walk", "idle")

    def check_collisions(self):
        for s in self._collisions:
            # pg.draw.rect(pg.display.get_surface(), (255, 0, 0), s.rect)
            if s.rect.colliderect(self.rect.inflate(-100, -100)):
                if isinstance(s, Enemy) and "attack" in self._animation_state:
                    s.damage()
                return True
        return False

    def move(self):
        if self._v.magnitude() != 0:
            self._v = self._v.normalize()
        self.rect.topleft += self._v * self._speed
        if self.check_collisions() or "attack" in self._animation_state:
            self.rect.topleft -= self._v * self._speed

    def update(self):
        self.read_key_input()
        # self.move()
        self.animate() 

    def animate(self):
        self.image = self._animations[self._animation_state][self._frame_index]

        self._animation_timer += 1

        if self._animation_timer > 15:
            self._frame_index += 1
            if self._frame_index == 2 and "attack" in self._animation_state:
                self._animation_state = self._animation_state.replace("attack", "walk")
                self._frame_index = 0
            elif self._frame_index == 5:
                self._frame_index = 0 

            self._animation_timer = 0

    def load_frame(self, rect, sprite_sheet):
        rectangle = pg.Rect(rect)
        frame = pg.Surface(rectangle.size, pg.SRCALPHA)
        frame.blit(sprite_sheet, (0, 0), rectangle)
        return pg.transform.scale(frame, (64, 64))
    
    def load_animations(self):
        for state in self._animations.keys():
            sprite_sheet = pg.image.load("assets/characters/player/{}.png".format(state)).convert_alpha()
            if "walk" in state:
                for x in range(0, 193, 64):
                    self._animations[state].append(pg.transform.scale(self.load_frame((x, 0, 64, 64), sprite_sheet), (128, 128)))
                for x in range(0, 129, 64):
                    self._animations[state].append(pg.transform.scale(self.load_frame((x, 64, 64, 64), sprite_sheet), (128, 128)))
            if "attack" in state:
                self._animations[state].append(pg.transform.scale(self.load_frame((0, 0, 64, 64), sprite_sheet), (128, 128)))
                self._animations[state].append(pg.transform.scale(self.load_frame((64, 0, 64, 64), sprite_sheet), (128, 128)))
                self._animations[state].append(pg.transform.scale(self.load_frame((0, 64, 64, 64), sprite_sheet), (128, 128)))
            if "idle" in state:
                for x in range(0, 193, 64):
                    self._animations[state].append(pg.transform.scale(self.load_frame((x, 0, 64, 64), sprite_sheet), (128, 128)))
                self._animations[state].append(pg.transform.scale(self.load_frame((0, 64, 64, 64), sprite_sheet), (128, 128)))

