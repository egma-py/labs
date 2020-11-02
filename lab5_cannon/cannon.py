from light_theme import *
from dark_theme import *

import random as rnd
import pygame as pg
import pygame.draw as pgd
import math as m

"""
What to do:
    Time bar (DONE)
    Menu:
        settings (DONE except diff, theme and loc)
        background(will be done when all will be done)
        main menu (DONE)
    Objects:
        gun (DONE wxcept power)
        gun health
        target(DONE except making bombs)
        bullet(DONE)
    colors
"""

class Main_menu:
    def __init__(self, size_x):
        self.size_x = size_x
        
    def appear(self, size_x):
        pgd.rect(screen, MENU_COLOR_l, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
        #begin button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2), (100, 35)])
        screen.blit(begin, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+8))
        #settings button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2+50), (100, 35)])
        screen.blit(settings, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+58))
        #Exit button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2+100), (100, 35)])
        screen.blit(exitt, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+108))
        
    def disappear(self, size_x):
        pgd.rect(screen, BACKGROUND_l, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
    
    def change_size_a(self, size_x):
        self.size_x += size[0]/(2*FPS)
        if self.size_x > int(size[0]*0.375):
            self.size_x = int(size[0]*0.375)
            
    def change_size_d(self, size_x):
        self.size_x -= size[0]/(2*FPS)
        if self.size_x < 0:
            self.size_x = 0
            
    def button_b_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2) and event.pos[1]<(size[1]//2+35):
            return True
        else:
            return False
        
    def button_e_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2+100) and event.pos[1]<(size[1]//2+135):
            return True
        else:
            return False
        
    def button_s_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2+50) and event.pos[1]<(size[1]//2+85):
            return True
        else:
            return False                   
        

class Settings:
    def __init__(self, size_x):
        self.size_x = size_x
    
    def appear(self, size_x):
        pgd.rect(screen, MENU_COLOR_l, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
        #game time button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2-100), (100, 35)])
        screen.blit(game_duration, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-92))
        #difficulty button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2-50), (100, 35)])
        screen.blit(difficulty, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-42))
        #theme button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2), (100, 35)])
        screen.blit(theme, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+8))
        #location button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2+50), (100, 35)])
        screen.blit(location, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+58))
        #return button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2+100), (100, 35)])
        screen.blit(returnn, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+108))
        
    def disappear(self, size_x):
        pgd.rect(screen, BACKGROUND_l, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
    
    def change_size_a(self, size_x):
        self.size_x += size[0]/(2*FPS)
        if self.size_x > int(size[0]*0.375):
            self.size_x = int(size[0]*0.375)
            
    def change_size_d(self, size_x):
        self.size_x -= size[0]/(2*FPS)
        if self.size_x < 0:
            self.size_x = 0
            
    def button_r_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2+100) and event.pos[1]<(size[1]//2+135):
            return True
        else:
            return False
    
    def button_gt_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2-100) and event.pos[1]<(size[1]//2-65):
            return True
        else:
            return False
    
    def button_d_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2-50) and event.pos[1]<(size[1]//2-15):
            return True
        else:
            return False
    
    def button_t_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2) and event.pos[1]<(size[1]//2+35):
            return True
        else:
            return False
    
    def button_l_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2+50) and event.pos[1]<(size[1]//2+85):
            return True
        else:
            return False

    
class Gt_menu:
    def __init__(self, size_x):
        self.size_x = size_x
    
    def appear(self, size_x):
        pgd.rect(screen, MENU_COLOR_l, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
        #10s button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2-100), (100, 35)])
        screen.blit(sec10, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-92))
        #20s button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2-50), (100, 35)])
        screen.blit(sec20, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-42))
        #30s button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2), (100, 35)])
        screen.blit(sec30, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+8))
        #60s button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2+50), (100, 35)])
        screen.blit(sec60, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+58))
        
    def disappear(self, size_x):
        pgd.rect(screen, BACKGROUND_l, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
    
    def change_size_a(self, size_x):
        self.size_x += size[0]/(2*FPS)
        if self.size_x > int(size[0]*0.375):
            self.size_x = int(size[0]*0.375)
            
    def button_10_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2-100) and event.pos[1]<(size[1]//2-65):
            return True
        else:
            return False
        
    def button_20_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2-50) and event.pos[1]<(size[1]//2-15):
            return True
        else:
            return False

    def button_30_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2) and event.pos[1]<(size[1]//2+35):
            return True
        else:
            return False
        
    def button_60_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2+50) and event.pos[1]<(size[1]//2+85):
            return True
        else:
            return False
        
        
class D_menu:
    def __init__(self, size_x):
        self.size_x = size_x
    
    def appear(self, size_x):
        pgd.rect(screen, MENU_COLOR_l, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
        #easy button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2-100), (100, 35)])
        screen.blit(easy, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-92))
        #medium button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2-50), (100, 35)])
        screen.blit(medium, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-42))
        #hard button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2), (100, 35)])
        screen.blit(hard, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+8))
        
    def disappear(self, size_x):
        pgd.rect(screen, BACKGROUND_l, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
    
    def change_size_a(self, size_x):
        self.size_x += size[0]/(2*FPS)
        if self.size_x > int(size[0]*0.375):
            self.size_x = int(size[0]*0.375)
            
    def button_e_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2-100) and event.pos[1]<(size[1]//2-65):
            return True
        else:
            return False
        
    def button_m_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2-50) and event.pos[1]<(size[1]//2-15):
            return True
        else:
            return False

    def button_h_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2) and event.pos[1]<(size[1]//2+35):
            return True
        else:
            return False
        
        
class L_menu:
    def __init__(self, size_x):
        self.size_x = size_x
    
    def appear(self, size_x):
        pgd.rect(screen, MENU_COLOR_l, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
        #plains button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2-100), (100, 35)])
        screen.blit(plain, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-92))
        #hills button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2-50), (100, 35)])
        screen.blit(hills, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-42))
        
    def disappear(self, size_x):
        pgd.rect(screen, BACKGROUND_l, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
    
    def change_size_a(self, size_x):
        self.size_x += size[0]/(2*FPS)
        if self.size_x > int(size[0]*0.375):
            self.size_x = int(size[0]*0.375)
            
    def button_plain_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2-100) and event.pos[1]<(size[1]//2-65):
            return True
        else:
            return False
        
    def button_hills_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2-50) and event.pos[1]<(size[1]//2-15):
            return True
        else:
            return False
        
        
class T_menu:
    def __init__(self, size_x):
        self.size_x = size_x
    
    def appear(self, size_x):
        pgd.rect(screen, MENU_COLOR_l, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
        #dark button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2-100), (100, 35)])
        screen.blit(dark, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-92))
        #light button
        pgd.rect(screen, RED_l, [(size[0]-int(1.5*self.size_x-210), size[1]//2-50), (100, 35)])
        screen.blit(light, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-42))
        
    def disappear(self, size_x):
        pgd.rect(screen, BACKGROUND_l, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
    
    def change_size_a(self, size_x):
        self.size_x += size[0]/(2*FPS)
        if self.size_x > int(size[0]*0.375):
            self.size_x = int(size[0]*0.375)
            
    def button_dark_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2-100) and event.pos[1]<(size[1]//2-65):
            return True
        else:
            return False
        
    def button_light_check(self, size_x, event):
        if event.pos[0]>(size[0]-int(1.5*self.size_x-210)) and event.pos[0]<(size[0]-int(1.5*self.size_x-210)+100) and event.pos[1]>(size[1]//2-50) and event.pos[1]<(size[1]//2-15):
            return True
        else:
            return False


class Time_bar:
    color_factor = 255
    color = ((255 - color_factor), color_factor, 50)
    def __init__(self, sec, length, background_color):
        self.background_color = background_color
        self.sec = FPS * sec
        self.length = length
            
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
        
        
class Gun:
    def __init__(self, v, x, y, cannon_l, cannon_w):
        self.v = v
        self.x = x
        self.y = y
        self.cannon_l = cannon_l
        self.cannon_w = cannon_w

    def app(self, x, y, cannon_l, cannon_w, pos):
        if (self.y-pos[1]) <= 0:
            arctg = 0
            x2 = self.x
            y2 = self.y - self.cannon_l
        else:
            arctg = m.atan((pos[0]-self.x)/(self.y-pos[1]))
            x2 = int(self.x + self.cannon_l*m.sin(arctg))
            y2 = int(self.y - self.cannon_l*m.cos(arctg))
        pgd.rect(screen, GUN_l, [(self.x-21, self.y-5), (42, 10)])
        pgd.line(screen, GUN_l, (self.x, self.y), (x2, y2), self.cannon_w)
    def disapp(self, x, y, cannon_l, cannon_w, pos):
        if (self.y-pos[1]) <= 0:
            arctg = 0
            x2 = self.x
            y2 = self.y - self.cannon_l
        else:
            arctg = m.atan((pos[0]-self.x)/(self.y-pos[1]))
            x2 = int(self.x + self.cannon_l*m.sin(arctg))
            y2 = int(self.y - self.cannon_l*m.cos(arctg))
        pgd.rect(screen, BACKGROUND_l, [(self.x-30, self.y-30), (60, 35)])
        
    def right(self, x, y, v):
        self.x += self.v
        
    def left(self, x, y, v):
        self.x -= self.v
        
    def shoot(self, obj):
        obj.app(obj.x, obj.y)
        
        
class Target:
    def __init__(self):
        self.x = rnd.randint(30, size[0]-30)
        self.y = rnd.randint(30, int(size[1]*0.45))
        self.r = rnd.randint(10, 20)
        self.v = rnd.randint(5, 10)
        self.alive = True
        self.color = TARGET_COLORS_l[5-rnd.randint(1, 5)]
        
    def app(self, x, y, r):
        pgd.circle(screen, self.color, (self.x, self.y), self.r)
        
    def disapp(self, x, y, r):
        pgd.circle(screen, BACKGROUND_l, (self.x, self.y), self.r)
        
    def change(self, x, v, r):
        self.x += self.v
        if self.x >= size[0]-self.r or self.x <= self.r:
            self.v = -self.v
            self.x += self.v


class Bullet:
    def __init__(self, obj, pos, t):
        if (obj.y-pos[1]) <= 0:
            arctg = 0
            self.x = obj.x
            self.y = obj.y - obj.cannon_l
        else:
            arctg = m.atan((pos[0]-obj.x)/(obj.y-pos[1]))
            self.x = int(obj.x + obj.cannon_l*m.sin(arctg))
            self.y = int(obj.y - obj.cannon_l*m.cos(arctg))
        self.vx = -int(20*m.sin(arctg))
        self.vy = int(20*m.cos(arctg))
        self.t = t
        self.r = bullet_radius
        

    def app(self, x, y):
        pgd.circle(screen, RED_l, (self.x, self.y), self.r)

    def disapp(self, x, y):
        pgd.circle(screen, BACKGROUND_l, (self.x, self.y), self.r)
        
    def change(self, x, y, vx, vy, obj):
        self.x -= self.vx
        self.y -= self.vy
        self.vy -= g
        if self.y >= obj.size*obj.k:
            self.vy = -int(0.8 * self.vy)
            self.y -= self.vy
           

class Bomb:
    pass


class Location:
    def __init__(self, plain_type):
        self.plain_type = plain_type
        self.k = 0.75
        self.size = size[1]
        
    def appear(self, plain_type):
        if self.plain_type:
            pgd.rect(screen, LOC_COLOR_l, [(0, int(self.size*self.k)), (size[0], int(self.size*(1-self.k)))])
        else:
            pass
            
    def disappear(self, plain_type):
        if self.plain_type:
            pgd.rect(screen, BACKGROUND_l, [(0, int(self.size*self.k)), (size[0], int(self.size*(1-self.k)))])
        else:
            pass      
        

class Background_menu:
    pass


def menu_appear(obj, x):
    obj.disappear(x)
    obj.change_size_a(x)
    obj.appear(x)


def menu_disappear(obj, x):
    obj.disappear(x)
    obj.change_size_d(x)
    obj.appear(x)   


def time_bar_begin(obj, x, t):
    obj.disappear(x)
    obj.shorten(t, x)
    obj.change_color(t)
    obj.appear(x)

    
def buttons_activated(statement):
    if statement:
        return True
    else:
        return False


def target_move(obj):
    obj.disapp(obj.x, obj.y, obj.r)
    obj.change(obj.x, obj.y, obj.r)
    obj.app(obj.x, obj.y, obj.r)
    

def bullet_move(obj, obj1):
    obj.disapp(obj.x, obj.y)
    obj.change(obj.x, obj.y, obj.vx, obj.vy, obj1)
    obj.app(obj.x, obj.y)
    
    
def hittest(bullett, targett):
    s = m.sqrt((bullett.x-targett.x)**2+(bullett.y-targett.y)**2)
    if s < (bullett.r + targett.r):
        return True
    else:
        return False
    
    
pg.init()
pg.font.init()

FPS = 30
global size
size = (683, 557)
screen = pg.display.set_mode(size)
font = pg.font.Font(None, 25)
begin = font.render('New game', True, (255, 255, 255))
settings = font.render('Settings', True, (255, 255, 255))
exitt = font.render('Exit', True, (255, 255, 255))
returnn = font.render('Return', True, (255, 255, 255))
difficulty = font.render('Difficulty', True, (255, 255, 255))
theme = font.render('Theme', True, (255, 255, 255))
location = font.render('Location', True, (255, 255, 255))
game_duration = font.render('Game time', True, (255, 255, 255)) 
sec10 = font.render('10 s', True, (255, 255, 255))
sec20 = font.render('20 s', True, (255, 255, 255))
sec30 = font.render('30 s', True, (255, 255, 255))
sec60 = font.render('60 s', True, (255, 255, 255))
hard = font.render('Hard', True, (255, 255, 255))
medium = font.render('Medium', True, (255, 255, 255))
easy = font.render('Easy', True, (255, 255, 255))
hills = font.render('Hills', True, (255, 255, 255))
plain = font.render('Plain', True, (255, 255, 255))
dark = font.render('Dark', True, (255, 255, 255))
light = font.render('Light', True, (255, 255, 255))

pg.display.update()
clock = pg.time.Clock()

#defining additional constants  
game_time = 10
time_counter = 0
main_menu_size = 0
settings_size = 0
gt_menu_size = 0
d_menu_size = 0
l_menu_size = 0
t_menu_size = 0
bullet_radius = 7
menu_time = 2*FPS
settings_time = 2*FPS
v_gun = 5
x_gun = size[0]//2
y_gun = int(size[1]*0.75)-5
l_gun = 30
w_gun = 8
g = 1
tg_amounts = 5

#defining default modes
finished = False
dark_theme_mode = False
main_menu_mode = True
settings_mode = False
time_bar_mode = False
game_mode = False
gt_menu_mode = False
d_menu_mode = False
l_menu_mode = False
t_menu_mode = False
loc_mode = True

#defining objects in the game
time_bar = Time_bar(game_time, size[0], BACKGROUND_l)
main_menu = Main_menu(main_menu_size)
settings_menu = Settings(settings_size)
gt_menu = Gt_menu(gt_menu_size)
d_menu = D_menu(d_menu_size)
l_menu = L_menu(l_menu_size)
t_menu = T_menu(t_menu_size)
gun = Gun(v_gun, x_gun, y_gun, l_gun, w_gun)
bullets = []
targets = []
for i in range(tg_amounts):
    targets.append(Target())
bombs = []
loc = Location(loc_mode)
screen.fill(BACKGROUND_l)

while not finished:
    clock.tick(FPS)
    keys = pg.key.get_pressed()
    mouse_pos = pg.mouse.get_pos()
    if game_mode:
        if keys[pg.K_RIGHT]:
            gun.disapp(gun.x, gun.y, gun.cannon_l, gun.cannon_w, mouse_pos)
            if gun.x >= size[0]-21:
                gun.x = size[0]-21
            else:
                gun.right(gun.x, gun.y, gun.v)
        elif keys[pg.K_LEFT]:
            gun.disapp(gun.x, gun.y, gun.cannon_l, gun.cannon_w, mouse_pos)
            if gun.x <= 21:
                gun.x = 21
            else:
                gun.left(gun.x, gun.y, gun.v)
        elif pg.mouse.get_focused():
            gun.disapp(gun.x, gun.y, gun.cannon_l, gun.cannon_w, mouse_pos)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.MOUSEBUTTONDOWN and game_mode and event.button==1:
            bullets.append(Bullet(gun, mouse_pos, 180))
            new_bullet = Bullet(gun, mouse_pos, 180)
        if event.type == pg.MOUSEBUTTONUP and game_mode and event.button==1 and main_menu.size_x==0:
            gun.shoot(new_bullet)
            new_bullet.disapp(new_bullet.x, new_bullet.y)
        if event.type == pg.MOUSEBUTTONDOWN:
            if buttons_activated(main_menu_mode):
                if event.button == 1 and main_menu.button_e_check(main_menu_size, event):
                    finished = True
                if event.button == 1 and main_menu.button_s_check(main_menu_size, event):
                    settings_mode = True
                    main_menu_mode = False
                if event.button == 1 and main_menu.button_b_check(main_menu_size, event):
                    game_mode = True
                    main_menu_mode = False
            elif buttons_activated(settings_mode):
                if event.button == 1 and settings_menu.button_r_check(settings_size, event):
                    settings_mode = False
                    main_menu_mode = True
                if event.button == 1 and settings_menu.button_d_check(settings_size, event):
                    settings_mode = False
                    d_menu_mode = True
                if event.button == 1 and settings_menu.button_l_check(settings_size, event):
                    settings_mode = False
                    l_menu_mode = True
                if event.button == 1 and settings_menu.button_gt_check(settings_size, event):
                    settings_mode = False
                    gt_menu_mode = True
                if event.button == 1 and settings_menu.button_t_check(settings_size, event):
                    settings_mode = False
                    t_menu_mode = True
            elif buttons_activated(gt_menu_mode):
                if event.button == 1 and gt_menu.button_10_check(gt_menu_size, event):
                    settings_mode = True
                    gt_menu_mode = False
                    game_time = 10
                    time_bar.sec = 10*FPS
                if event.button == 1 and gt_menu.button_20_check(gt_menu_size, event):
                    settings_mode = True
                    gt_menu_mode = False
                    game_time = 20
                    time_bar.sec = 20*FPS
                if event.button == 1 and gt_menu.button_30_check(gt_menu_size, event):
                    settings_mode = True
                    gt_menu_mode = False
                    game_time = 30
                    time_bar.sec = 30*FPS
                if event.button == 1 and gt_menu.button_60_check(gt_menu_size, event):
                    settings_mode = True
                    gt_menu_mode = False
                    game_time = 60
                    time_bar.sec = 60*FPS
            elif buttons_activated(d_menu_mode):
                if event.button == 1 and d_menu.button_e_check(d_menu_size, event):
                    settings_mode = True
                    d_menu_mode = False
                if event.button == 1 and d_menu.button_m_check(d_menu_size, event):
                    settings_mode = True
                    d_menu_mode = False
                if event.button == 1 and d_menu.button_h_check(d_menu_size, event):
                    settings_mode = True
                    d_menu_mode = False
            elif buttons_activated(l_menu_mode):
                if event.button == 1 and l_menu.button_hills_check(d_menu_size, event):
                    settings_mode = True
                    l_menu_mode = False
                if event.button == 1 and l_menu.button_plain_check(d_menu_size, event):
                    settings_mode = True
                    l_menu_mode = False
            elif buttons_activated(t_menu_mode):
                if event.button == 1 and t_menu.button_dark_check(t_menu_size, event):
                    settings_mode = True
                    t_menu_mode = False
                if event.button == 1 and t_menu.button_light_check(t_menu_size, event):
                    settings_mode = True
                    t_menu_mode = False
    if main_menu_mode:
        menu_appear(main_menu, main_menu_size)
        pg.display.update()
    if settings_mode:
        menu_appear(settings_menu, settings_size)
        pg.display.update()
    if gt_menu_mode:
        menu_appear(gt_menu, gt_menu_size)
        pg.display.update()
    if d_menu_mode:
        menu_appear(d_menu, d_menu_size)
        pg.display.update()
    if l_menu_mode:
        menu_appear(l_menu, l_menu_size)
        pg.display.update()
    if t_menu_mode:
        menu_appear(t_menu, t_menu_size)
        pg.display.update()
    if game_mode and not main_menu_mode: 
        menu_disappear(main_menu, main_menu_size)
        pg.display.update()
    if game_mode and main_menu.size_x == 0: #game
        time_bar_begin(time_bar, size[0], game_time)
        gun.app(gun.x, gun.y, gun.cannon_l, gun.cannon_w, mouse_pos)
        for elem in targets:
            target_move(elem)
            if not elem.alive:
                elem.disapp(elem.x, elem.y, elem.r)
                targets.remove(elem)
                targets.append(Target())
        for elem in bullets:
            if elem.t > 0:
                elem.t -= 1
                bullet_move(elem, loc)
            elif elem.t == 0:
                elem.t = -1
                elem.disapp(elem.x, elem.y)
            else:
                bullets.remove(elem)
            for targett in targets:
                if hittest(targett, elem):
                    targett.alive = False
                    elem.t = 0
        loc.appear(loc_mode)
        pg.display.update()
    if time_bar.length == 0 and not main_menu_mode:
        game_mode = False
        loc.disappear(loc_mode)
        for elem in bullets:
            elem.disapp(elem.x, elem.y)
            elem.t = 0
        for elem in targets:
            elem.disapp(elem.x, elem.y, elem.r)
            elem.alive = False
        gun.disapp(gun.x, gun.y, gun.cannon_l, gun.cannon_w, mouse_pos)
        gun.x, gun.y, gun.v = x_gun, y_gun, v_gun
        time_bar.length = size[0]
        Time_bar.color_factor = 255
        time_bar.color = (255-Time_bar.color_factor, Time_bar.color_factor, 50)
        main_menu_mode = True
    
pg.time.wait(500)
pg.quit()