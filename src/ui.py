import pygame as pg
from src.globals import *

class UI:
    def __init__(self):
        
        self.display_surface = pg.display.get_surface()
        self.font = pg.font.Font(UI_FONT, UI_FONT_SIZE)

        self.health_bar_rect = pg.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.exp_bar_rect = pg.Rect(10, 40, EXP_BAR_WIDTH, BAR_HEIGHT)
        self.counter = 0

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
    
    def display_dialogue(self, player):
        current_rect = pg.Rect(10, 600, 400, 100)
        x = current_rect[0] + 4
        y = current_rect[1] + 8
        if player.counter == 0:
            pg.draw.rect(self.display_surface, '#EEEEEE', current_rect)
            text = self.font.render(str("Welcome to The Legend of Pyda!"), False, '#000000')
            top_left = text.get_rect(topleft = (x,y))
            self.display_surface.blit(text, top_left)
            text = self.font.render(str("Press ENTER to continue."), False, '#000000')
            y += 32
            top_left = text.get_rect(topleft = (x,y))
            self.display_surface.blit(text, top_left)
        if player.counter == 1:
            pg.draw.rect(self.display_surface, '#EEEEEE', current_rect)
            text = self.font.render(str("Gain Experience by Killing Enemies, when the Elders"), False, '#000000')
            top_left = text.get_rect(topleft = (x,y))
            self.display_surface.blit(text, top_left)
            text = self.font.render(str("think you're ready you may fight the boss and"), False, '#000000')
            y += 14
            top_left = text.get_rect(topleft = (x,y))
            self.display_surface.blit(text, top_left)
            text = self.font.render(str("save the world!"), False, '#000000')
            y += 14
            top_left = text.get_rect(topleft = (x,y))
            self.display_surface.blit(text, top_left)
            text = self.font.render(str("Collect Items to boost your stats and give "), False, '#000000')
            y += 18
            top_left = text.get_rect(topleft = (x,y))
            self.display_surface.blit(text, top_left)
            text = self.font.render(str("yourself a better chance against the bosss!"), False, '#000000')
            y += 14
            top_left = text.get_rect(topleft = (x,y))
            self.display_surface.blit(text, top_left)
        if player.counter == 2:
            pg.draw.rect(self.display_surface, '#EEEEEE', current_rect)
            text = self.font.render(str("Use W-A-S-D to move around and SPACE to attack"), False, '#000000')
            top_left = text.get_rect(topleft = (x,y))
            self.display_surface.blit(text, top_left)
        if player.counter == 3:
            pg.draw.rect(self.display_surface, '#EEEEEE', current_rect)
            text = self.font.render(str("Press Y to accept this mission"), False, '#000000')
            top_left = text.get_rect(topleft = (x,y))
            self.display_surface.blit(text, top_left)
        if player.counter == 5:
            player.counter = 0