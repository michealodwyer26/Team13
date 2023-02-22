import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self,enemy_name,pos,groups):
        super().__init__(groups)

        self.sprite_type = 'enemy'
