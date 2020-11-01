from random import randrange as rnd, choice
from light_theme import *
from dark_theme import *

import pygame as pg
import pygame.draw as pgd
import math as m

"""
What to do:
    Time bar (DONE)
    Menu:
        settings
        background
        main menu (DONE)
    Objects:
        gun
        target
        bullet
    colors
"""

class Main_menu:
    size_y = 600
    def __init__(self, size_x):
        self.size_x = menu_size
        
    def appear(self, size_x):
        pgd.rect(screen, MENU_COLOR_l, [(800-int(self.size_x), 0), (int(self.size_x), Main_menu.size_y)])
        #begin button
        pgd.rect(screen, RED_l, [(800-int(1.5*self.size_x-210), Main_menu.size_y//2), (100, 35)])
        screen.blit(begin, (800-int(1.5*self.size_x-210)+8, Main_menu.size_y//2+8))
        #settings button
        pgd.rect(screen, RED_l, [(800-int(1.5*self.size_x-210), Main_menu.size_y//2+50), (100, 35)])
        screen.blit(settings, (800-int(1.5*self.size_x-210)+8, Main_menu.size_y//2+58))
        #Exit button
        pgd.rect(screen, RED_l, [(800-int(1.5*self.size_x-210), Main_menu.size_y//2+100), (100, 35)])
        screen.blit(exitt, (800-int(1.5*self.size_x-210)+8, Main_menu.size_y//2+108))
        
    def disappear(self, size_x):
        pgd.rect(screen, BACKGROUND_l, [(800-int(self.size_x), 0), (int(self.size_x), Main_menu.size_y)])
    
    def change_size_a(self, size_x):
        self.size_x += 800/(2*FPS)
        if self.size_x > 300:
            self.size_x = 300
            
    def change_size_d(self, size_x):
        self.size_x -= 800/(2*FPS)
        if self.size_x < 0:
            self.size_x = 0
            
    def button_b_check(self, size_x, event):
        if event.pos[0]>(800-int(1.5*self.size_x-210)) and event.pos[0]<(800-int(1.5*self.size_x-210)+100) and event.pos[1]>(Main_menu.size_y//2) and event.pos[1]<(Main_menu.size_y//2+35):
            return True
        else:
            return False
        
    def button_e_check(self, size_x, event):
        if event.pos[0]>(800-int(1.5*self.size_x-210)) and event.pos[0]<(800-int(1.5*self.size_x-210)+100) and event.pos[1]>(Main_menu.size_y//2+100) and event.pos[1]<(Main_menu.size_y//2+135):
            return True
        else:
            return False
        
    def button_s_check(self, size_x, event):
        if event.pos[0]>(800-int(1.5*self.size_x-210)) and event.pos[0]<(800-int(1.5*self.size_x-210)+100) and event.pos[1]>(Main_menu.size_y//2+50) and event.pos[1]<(Main_menu.size_y//2+85):
            return True
        else:
            return False                   
        

class Settings:
    size_y = 600
    def __init__(self, size_x):
        self.size_x = menu_size
    
    def appear(self, size_x):
        pgd.rect(screen, MENU_COLOR_l, [(800-int(self.size_x), 0), (int(self.size_x), Main_menu.size_y)])
        #game time button
        pgd.rect(screen, RED_l, [(800-int(1.5*self.size_x-210), Main_menu.size_y//2-100), (100, 35)])
        screen.blit(begin, (800-int(1.5*self.size_x-210)+8, Main_menu.size_y//2-92))
        #difficulty button
        pgd.rect(screen, RED_l, [(800-int(1.5*self.size_x-210), Main_menu.size_y//2-50), (100, 35)])
        screen.blit(settings, (800-int(1.5*self.size_x-210)+8, Main_menu.size_y//2-42))
        #theme button
        pgd.rect(screen, RED_l, [(800-int(1.5*self.size_x-210), Main_menu.size_y//2), (100, 35)])
        screen.blit(settings, (800-int(1.5*self.size_x-210)+8, Main_menu.size_y//2+8))
        #location button
        pgd.rect(screen, RED_l, [(800-int(1.5*self.size_x-210), Main_menu.size_y//2+50), (100, 35)])
        screen.blit(settings, (800-int(1.5*self.size_x-210)+8, Main_menu.size_y//2+58))
        #return button
        pgd.rect(screen, RED_l, [(800-int(1.5*self.size_x-210), Main_menu.size_y//2+100), (100, 35)])
        screen.blit(returnn, (800-int(1.5*self.size_x-210)+8, Main_menu.size_y//2+108))
        
    def disappear(self, size_x):
        pgd.rect(screen, BACKGROUND_l, [(800-int(self.size_x), 0), (int(self.size_x), Main_menu.size_y)])
    
    def change_size_a(self, size_x):
        self.size_x += 800/(2*FPS)
        if self.size_x > 300:
            self.size_x = 300
            
    def change_size_d(self, size_x):
        self.size_x -= 800/(2*FPS)
        if self.size_x < 0:
            self.size_x = 0
            
    def button_r_check(self, size_x, event):
        if event.pos[0]>(800-int(1.5*self.size_x-210)) and event.pos[0]<(800-int(1.5*self.size_x-210)+100) and event.pos[1]>(Settings.size_y//2+100) and event.pos[1]<(Settings.size_y//2+135):
            return True
        else:
            return False

    
class Background_of_menu:
    pass



class Time_bar: #FIXME include theme
    color_factor = 255
    color = ((255 - color_factor), color_factor, 50)
    def __init__(self, sec, length, background_color):
        self.background_color = BACKGROUND_l
        self.sec = FPS * game_time
        self.length = size[0]
            
    def appear(self, length):
        pgd.rect(screen, Time_bar.color, [(0, 0), (int(self.length), 5)])
        
    def disappear(self, length):
        pgd.rect(screen, self.background_color, [(0, 0), (int(self.length), 5)])
        
    def shorten(self, sec, length):
        self.length -= (size[0])/self.sec 
        if self.length < 0:
            self.length = 0
        
    def change_color(self, sec):
        Time_bar.color_factor -= (255)/self.sec
        if Time_bar.color_factor < 0:
            Time_bar.color_factor = 0
        Time_bar.color = ((255 - int(Time_bar.color_factor)), int(Time_bar.color_factor), 50)
        

def menu_appear(obj, x):
    obj.disappear(x)
    obj.change_size_a(x)
    obj.appear(x)

def menu_disappear(obj, x):
    obj.disappear(x)
    obj.change_size_d(x)
    obj.appear(x)
    
def settings_appear(obj, x):
    obj.disappear(x)
    obj.change_size_a(x)
    obj.appear(x)

def settings_disappear(obj, x):
    obj.disappear(x)
    obj.change_size_d(x)
    obj.appear(x)
    
def time_bar_begin(obj, x, t):
    obj.disappear(x)
    obj.shorten(t, x)
    obj.change_color(t)
    obj.appear(x)
    
def s_buttons_activated(statement):
    if statement:
        return True
    else:
        return False
    
def m_buttons_activated(statement):
    if statement:
        return True
    else:
        return False
    
       
pg.init()
pg.font.init()

FPS = 30
size = (800, 600)
screen = pg.display.set_mode(size)
font = pg.font.Font(None, 25)
begin = font.render('New game', True, (255, 255, 255))
settings = font.render('Settings', True, (255, 255, 255))
exitt = font.render('Exit', True, (255, 255, 255))
returnn = font.render('Return', True, (255, 255, 255))

pg.display.update()
clock = pg.time.Clock()

#defining additional constants  
game_time = 5
time_counter = 0
menu_size = 0
menu_time = 2*FPS
settings_time = 2*FPS

#defining objects in the game
time_bar = Time_bar(game_time, size[0], BACKGROUND_l)
main_menu = Main_menu(menu_size)
settings_menu = Settings(menu_size)

#defining default modes
finished = False
dark_theme_mode = False
main_menu_mode = True
settings_mode = False
time_bar_mode = False
game_mode = False

screen.fill(BACKGROUND_l)

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.MOUSEBUTTONDOWN:
            if m_buttons_activated(main_menu_mode):
                if event.button == 1 and main_menu.button_b_check(menu_size, event):
                    main_menu_mode = not main_menu_mode
                    time_bar_mode = not time_bar_mode
                    game_mode = not game_mode
                elif event.button == 1 and main_menu.button_e_check(menu_size, event):
                    finished = True
                elif event.button == 1 and main_menu.button_s_check(menu_size, event):
                    main_menu_mode = not main_menu_mode
                    settings_mode = not settings_mode
            elif s_buttons_activated(settings_mode):
                if event.button == 1 and settings_menu.button_r_check(menu_size, event):
                    settings_mode = not settings_mode
                    main_menu_mode = not main_menu_mode
    if main_menu_mode:
        menu_appear(main_menu, menu_size)
        pg.display.update()
    if not main_menu_mode and menu_time != 0 and settings_mode:
        menu_disappear(main_menu, menu_size)
        pg.display.update()
        menu_time -= 1
    if not main_menu_mode and settings_mode and not time_bar_mode:
        settings_appear(settings_menu, menu_size)
        pg.display.update()
    if not settings_mode and main_menu_mode and not time_bar_mode and settings_time != 0:
        settings_disappear(settings_menu, menu_size)
        pg.display.update()
        settings_time -= 1
    if menu_time == 0 and not main_menu_mode and not settings_mode:
        if time_bar_mode:
            time_bar_begin(time_bar, size[0], game_time)
            pg.display.update()
    if time_bar.length == 0:
        finished = True
    

pg.time.wait(500)
pg.quit()
        
    
    
