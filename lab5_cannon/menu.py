import pygame as pg
import pygame.draw as pgd

from light_theme import *
from dark_theme import *
from cannon import screen, menu_size

class Main_menu:
    size_y = 600
    def __init__(self, size_x):
        self.size_x = 300
        
    def appear(self, size_x):
        pgd.rect(screen, MENU_COLOR_l, [(800-int(self.size_x), 0), (int(self.size_x), Main_menu.size_y)])
        
    def disappear(self, size_x):
        pgd.rect(screen, BACKGROUND_l, [(800-int(self.size_x), 0), (int(self.size_x), Main_menu.size_y)])
    
    def change_size(self, size_x):
        self.size_x += 800/(game_time*FPS)
        if self.size_x > 300:
            self.size_x = 300


class Settings:
    pass

    
class Background_of_menu:
    pass

main_menu = Main_menu(menu_size)