import pygame as pg
from src.globals import *

class UI:
    def __init__(self):
        
        self.display_surface = pg.display.get_surface()
        self.font = pg.font.Font(UI_FONT, UI_FONT_SIZE)

        self.health_bar_rect = pg.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.exp_bar_rect = pg.Rect(10, 40, EXP_BAR_WIDTH, BAR_HEIGHT)

    def show_health_bar(self, current, max_amount, bg_rect, colour):
        pg.draw.rect(self.display_surface, '#222222', bg_rect)

        current_rect = bg_rect.copy()
        current_rect.width = bg_rect.width * (current / max_amount)

        pg.draw.rect(self.display_surface, HEALTH_COLOUR, current_rect)

        health_text = self.font.render(str(int(current)), False, '#EEEEEE')
        x = current_rect[0] + 4
        y = current_rect[1] + 5
        health_bar_center = health_text.get_rect(topleft = (x,y))
        self.display_surface.blit(health_text, health_bar_center)

    def show_exp_bar(self, current, max_amount, bg_rect, colour):
        pg.draw.rect(self.display_surface, '#222222', bg_rect)

        current_rect = bg_rect.copy()
        current_rect.width = bg_rect.width * (current / max_amount)

        pg.draw.rect(self.display_surface, EXP_CLOUR, current_rect)

        exp_text = self.font.render(str(int(current)), False, '#EEEEEE')
        x = current_rect[0] + 4
        y = current_rect[1] + 5
        exp_bar_center = exp_text.get_rect(topleft = (x,y))
        self.display_surface.blit(exp_text, exp_bar_center)

    def display(self, player):

        self.show_health_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOUR)
        self.show_exp_bar(player.exp, 1000, self.exp_bar_rect, HEALTH_COLOUR)