import pygame as pg
from src.globals import *

class UI:
    def __init__(self):
        
        self.display_surface = pg.display.get_surface()
        self.font = pg.font.Font(UI_FONT, UI_FONT_SIZE)

        self.health_bar_rect = pg.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.exp_bar_rect = pg.Rect(10, 40, EXP_BAR_WIDTH, BAR_HEIGHT)

    def load_bar(self, current, max_amount, bg_rect, colour):
        pg.draw.rect(self.display_surface, '#222222', bg_rect)

        current_rect = bg_rect.copy()
        current_rect.width = bg_rect.width * (current / max_amount)
        
        pg.draw.rect(self.display_surface, HEALTH_COLOUR, current_rect)

    def display(self, player):

        self.load_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOUR)