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
        settings (DONE except theme and location)
        background(will be done when all will be done)
        main menu (DONE)
        points(aver. +1, spec +2, enemy kill +5)
    Objects:
        gun (DONE)
        gun health(DONE)
        target(DONE)
        bullet(DONE)
        enemy (DONE)
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
        screen.blit(difficulty_txt, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-42))
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
    def __init__(self, v, x, y, cannon_l, cannon_w, hp):
        self.v = v
        self.x = x
        self.y = y
        self.l = 21
        self.w = 10
        self.lc = cannon_l
        self.wc = cannon_w
        self.hp = hp
        self.color = list(GUN_l)

    def app(self, x, y, cannon_l, cannon_w, pos):
        if (self.y-pos[1]) <= 0:
            arctg = 0
            x2 = self.x
            y2 = self.y - int(self.lc)
        else:
            arctg = m.atan((pos[0]-self.x)/(self.y-pos[1]))
            x2 = int(self.x + self.lc*m.sin(arctg))
            y2 = int(self.y - self.lc*m.cos(arctg))
        pgd.rect(screen, GUN_l, [(self.x-self.l, self.y-self.w//2), (int(2*self.l), self.w)])
        pgd.rect(screen, GUN_l, [(self.x-self.l, self.y-self.w//2-self.w), (3, self.w)])
        pgd.line(screen, self.color, (self.x, self.y-self.w//2), (x2, y2), self.wc)
        
    def disapp(self, x, y, cannon_l, cannon_w, pos):
        if (self.y-pos[1]) <= 0:
            arctg = 0
            x2 = self.x
            y2 = self.y - self.lc
        else:
            arctg = m.atan((pos[0]-self.x)/(self.y-pos[1]))
            x2 = int(self.x + self.lc*m.sin(arctg))
            y2 = int(self.y - self.lc*m.cos(arctg))
        pgd.rect(screen, BACKGROUND_l, [(self.x-35, self.y-35), (70, 40)])
        
    def hp_app(self, x):
        pgd.rect(screen, BACKGROUND_l, ((x, 20), (120, 15)))
        hpx = x
        for i in range(self.hp):
            pgd.rect(screen, RED_l, ((hpx, 20), (20, 15)))
            hpx += 25
    
    def hp_disapp(self, x):
        pgd.rect(screen, BACKGROUND_l, ((x, 20), (120, 15)))
    
    def right(self, x, y, v):
        self.x += self.v
        
    def left(self, x, y, v):
        self.x -= self.v
        
    def shoot(self, obj):
        obj.app(obj.x, obj.y)
        
    def power(self):
        pass
        
        
class Enemy:
    def __init__(self):
        self.x = size[0]-15
        self.y = size[1]-400
        self.hp = 10
        self.shoot = 0
        self.l = 20
        self.w = 10
        self.hp = 5
        self.color = GUN_l
        
    def app(self, obj):
        arctg = m.atan((obj.y-self.y)/(obj.x-self.x))
        if obj.x-self.x == 0:
            x2 = self.x
            y2 = self.y + self.l
        else:
            x2 = -int(self.l*m.cos(arctg))+self.x
            y2 = int(self.l*m.sin(-arctg))+self.y
        pgd.rect(screen, self.color, ((self.x-20, self.y-2), (70, 2)))
        pgd.rect(screen, self.color, ((self.x-10, self.y), (20, 10)))
        pgd.line(screen, self.color, (self.x, self.y+10), (x2, y2), 5)
        
    def disapp(self):
        pgd.rect(screen, BACKGROUND_l, ((self.x-20, self.y-2), (70, 2)))
        pgd.rect(screen, BACKGROUND_l, ((self.x-10, self.y), (20, 10)))
        pgd.rect(screen, BACKGROUND_l, ((self.x-20, self.y+10), (40, 30)))
        
    def hp_app(self, x):
        pgd.rect(screen, BACKGROUND_l, ((x, 20), (150, 15)))
        hpx = x
        for i in range(self.hp):
            pgd.rect(screen, BLUE_l, ((hpx, 20), (10, 15)))
            hpx += 15
    
    def hp_disapp(self, x):
        pgd.rect(screen, BACKGROUND_l, ((x, 20), (150, 15)))
    
    
class E_Bullet:
    def __init__(self, gun, obj):
        self.x = gun.x
        self.y = gun.y
        self.vy = 0
        self.vx = -int(((size[0]-obj.x)/size[0])*30)
        self.t = 100
        self.r = 7
        
    def app(self):
        pgd.circle(screen, (0, 0, 0), (self.x, self.y), self.r)

    def disapp(self):
        pgd.circle(screen, BACKGROUND_l, (self.x, self.y), self.r)
        
    def change(self, obj):
        self.x += self.vx
        self.y += self.vy
        self.vy += g
        if self.y >= obj.size*obj.k:
            self.vy = -int(0.8 * self.vy)
            self.y += self.vy
    
    
class Target:
    def __init__(self):
        self.x = rnd.randint(30, size[0]-30)
        self.y = rnd.randint(30, int(size[1]*0.45))
        self.r = rnd.randint(10, 20)
        self.maxv = 5
        self.vx = rnd.randint(3, self.maxv)
        self.vy = rnd.randint(3, self.maxv)
        self.alive = True
        self.color = TARGET_COLORS_l[5-rnd.randint(1, 5)]
        self.s1_color = S_COLORS1_l[3-rnd.randint(1, 3)]
        self.s2_color = S_COLORS2_l[3-rnd.randint(1, 3)]
        self.bomb = 0
        
    def app(self, x, y, r):
        pgd.circle(screen, self.color, (self.x, self.y), self.r)
        
    def disapp(self, x, y, r):
        pgd.circle(screen, BACKGROUND_l, (self.x, self.y), self.r)
        
    def change(self, x, v, r):
        self.x += self.vx
        if self.x >= size[0]-self.r or self.x <= self.r:
            self.vx = -self.vx
            self.x += self.vx
    
    def s_app(self, x, y, r):
        pgd.circle(screen, self.s1_color, (self.x, self.y), self.r)
        pgd.circle(screen, self.s2_color, (self.x, self.y), self.r//2)
        
    def special_change(self, x, y, r):
        self.x += self.vx
        self.y += self.vy
        t = rnd.randint(1, 40)
        if t == 1:
            self.vx = rnd.randint(3, 6)
        if t == 2:
            self.vy = rnd.randint(3, 6)
        if self.x >= size[0]-self.r or self.x <= self.r:
            self.vx = -self.vx
            self.x += self.vx
        if self.y <= 30 or self.y >= int(size[1]*0.45):
            self.vy = -self.vy
            self.y += self.vy
        


class Bullet:
    def __init__(self, obj, pos, v):
        if (obj.y-pos[1]) <= 0:
            arctg = 0
            self.x = obj.x
            self.y = obj.y - obj.l
        else:
            arctg = m.atan((pos[0]-obj.x)/(obj.y-pos[1]))
            self.x = int(obj.x + obj.l*m.sin(arctg))
            self.y = int(obj.y - obj.l*m.cos(arctg))
        self.v = v
        self.vx = -int(self.v*m.sin(arctg))
        self.vy = int(self.v*m.cos(arctg))
        self.t = 100
        self.r = bullet_radius
        self.active = False
        self.color = RED_l
        

    def app(self, x, y):
        pgd.circle(screen, self.color, (self.x, self.y), self.r)

    def disapp(self, x, y):
        pgd.circle(screen, BACKGROUND_l, (self.x, self.y), self.r)
        
    def change(self, x, y, vx, vy, obj):
        self.x -= self.vx
        self.y -= self.vy
        self.vy -= g
        if self.y >= obj.size*obj.k:
            self.vy = -int(0.8 * self.vy)
            self.y -= self.vy
           

class Spec_Bullet:
    def __init__(self, obj, v):
        self.x = obj.x - obj.l
        self.y = obj.y - obj.w
        self.v = v
        self.color = TARGET_COLORS_l[5-rnd.randint(1, 5)]
        self.r = 10
        self.t = 10
        
    def app(self):
        pgd.circle(screen, self.color, (self.x, self.y), self.r)
        
    def disapp(self):
        pgd.circle(screen, BACKGROUND_l, (self.x, self.y), self.r)
        
    def change(self):
        self.y -= self.v
        self.v -= 1
        

class Mini_Bullets:
    def __init__(self, obj):
        self.vx = [13, 9, 0, -9, -13, -9, 0, 9]
        self.vy = [0, 9, 13, 9, 0, -9, -13, -9]
        self.x = [obj.x, obj.x, obj.x, obj.x, obj.x, obj.x, obj.x, obj.x]
        self.y = [obj.y, obj.y, obj.y, obj.y, obj.y, obj.y, obj.y, obj.y]
        self.r = 7
        self.t = [60, 60, 60, 60, 60, 60, 60, 60]
        self.color = []
        for i in range(8):
            self.color.append(TARGET_COLORS_l[5-rnd.randint(1, 5)])
        
    def app(self, k):
        pgd.circle(screen, self.color[k], (self.x[k], self.y[k]), self.r)
            
    def disapp(self, k):
        pgd.circle(screen, BACKGROUND_l, (self.x[k], self.y[k]), self.r)
    
    def change(self, k):
        self.x[k] += self.vx[k]
        self.y[k] += self.vy[k]
        self.vy[k] += 1


class Bomb:
    def __init__(self, obj):
        self.x = obj.x
        self.y = obj.y
        self.v = 1
        self.color = TARGET_COLORS_l[5-rnd.randint(1, 5)]
        self.r = 7
        self.act = True
        
    def app(self):
        pgd.circle(screen, self.color, (self.x, self.y), self.r)
        pgd.circle(screen, (0, 0, 0), (self.x, self.y), self.r, 2)
        
    def disapp(self):
        pgd.circle(screen, BACKGROUND_l, (self.x, self.y), self.r+1)
        
    def change_coords(self):
        self.y += self.v
        self.v += 1


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


def ebullet_move(obj, obj1):
    obj.disapp()
    obj.change(obj1)
    obj.app()
    
def buttons_activated(statement):
    if statement:
        return True
    else:
        return False


def specbul_move(obj):
    obj.disapp()
    obj.change()
    obj.app()


def minib_move(obj, k):
    obj.disapp(k)
    obj.change(k)
    obj.app(k)


def bomb_move(obj):
    obj.disapp()
    obj.change_coords()
    obj.app()


def target_move(obj):
    obj.disapp(obj.x, obj.y, obj.r)
    obj.change(obj.x, obj.y, obj.r)
    obj.app(obj.x, obj.y, obj.r)
    
    
def spec_target_move(obj):
    obj.disapp(obj.x, obj.y, obj.r)
    obj.special_change(obj.x, obj.y, obj.r)
    obj.s_app(obj.x, obj.y, obj.r)
    

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


def spec_hittest(bullett, targett):
    s = m.sqrt((bullett.x[i]-targett.x)**2+(bullett.y[i]-targett.y)**2)
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
difficulty_txt = font.render('Difficulty', True, (255, 255, 255))
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
lost = font.render('YOU LOST', True, (0, 0, 0))

pg.display.update()
clock = pg.time.Clock()

#defining additional constants  
game_time = 20
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
lc_gun = 15
wc_gun = 4
g = 1
v = 1
spec_v = 23
minib_amount = 8
tg_amounts = 3

#difficulty parameters
super_shots = 2
heart_points = 5
freq = 60
enemy_gun_active = False

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
difficulty = 0

#defining objects in the game
time_bar = Time_bar(game_time, size[0], BACKGROUND_l)
main_menu = Main_menu(main_menu_size)
settings_menu = Settings(settings_size)
gt_menu = Gt_menu(gt_menu_size)
d_menu = D_menu(d_menu_size)
l_menu = L_menu(l_menu_size)
t_menu = T_menu(t_menu_size)
gun = Gun(v_gun, x_gun, y_gun, lc_gun, wc_gun, heart_points)
enemy_gun = Enemy()
bullets = []
enemy_bullets = []
bombs = []
targets = []
sp_targets = []
spec_bullets = []
mini_bullets = []
for i in range(tg_amounts):
    targets.append(Target())
for i in range(tg_amounts):
    sp_targets.append(Target())
bombs = []
loc = Location(loc_mode)
screen.fill(BACKGROUND_l)

while not finished:
    clock.tick(FPS)
    keys = pg.key.get_pressed()
    mouse_pos = pg.mouse.get_pos()
    m1 = pg.mouse.get_pressed()[0]
    if game_mode and main_menu.size_x==0:
        if m1 == 1:
            if v != 40:
                v += 1
                gun.lc += 0.5
                gun.color[0] += 6
    if game_mode and main_menu.size_x==0:
        if keys[pg.K_RIGHT]:
            gun.disapp(gun.x, gun.y, gun.l, gun.w, mouse_pos)
            if gun.x >= size[0]-21:
                gun.x = size[0]-21
            else:
                gun.right(gun.x, gun.y, gun.v)
        elif keys[pg.K_LEFT]:
            gun.disapp(gun.x, gun.y, gun.l, gun.w, mouse_pos)
            if gun.x <= 21:
                gun.x = 21
            else:
                gun.left(gun.x, gun.y, gun.v)
        elif pg.mouse.get_focused():
            gun.disapp(gun.x, gun.y, gun.l, gun.w, mouse_pos)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.MOUSEBUTTONDOWN and game_mode and event.button==3 and main_menu.size_x==0 and super_shots > 0:
            spec_bullets.append(Spec_Bullet(gun, spec_v))
            super_shots -= 1
        if event.type == pg.MOUSEBUTTONUP and game_mode and event.button==1 and main_menu.size_x==0:
            bullets.append(Bullet(gun, mouse_pos, v))
            new_bullet = Bullet(gun, mouse_pos, v)
            gun.shoot(new_bullet)
            new_bullet.disapp(new_bullet.x, new_bullet.y)
            v = 1
            gun.lc = lc_gun
            gun.color[0] = 0
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
                    difficulty = 0
                    super_shots = 2
                    gun.hp = 5
                    for target in targets:
                        target.maxv = 5
                    freq = 60
                if event.button == 1 and d_menu.button_m_check(d_menu_size, event):
                    settings_mode = True
                    d_menu_mode = False
                    difficulty = 1
                    super_shots = 1
                    gun.hp = 3
                    for target in targets:
                        target.maxv = 7
                    freq = 40
                if event.button == 1 and d_menu.button_h_check(d_menu_size, event):
                    settings_mode = True
                    d_menu_mode = False
                    difficulty = 2
                    super_shots = 1
                    gun.hp = 3
                    for target in targets:
                        target.maxv = 9
                    freq = 30
                    enemy_gun_active = True
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
        gun.app(gun.x, gun.y, gun.l, gun.w, mouse_pos)
        gun.hp_app(20)
        for elem in spec_bullets:
            if elem.t != 0:
                specbul_move(elem)
            if elem.v == 0:
                elem.t = 0
                elem.disapp()
                mini_bullets.append(Mini_Bullets(elem))
        for elem in mini_bullets:
            for i in range(8):
                if elem.t[i] > 0:
                    minib_move(elem, i)
                for target in targets:
                    if spec_hittest(elem, target) and elem.t[i] > 0:
                        target.alive = False
                        elem.t[i] = 0
                for targett in sp_targets:
                    if spec_hittest(elem, targett) and elem.t[i] > 0:
                        targett.alive = False
                        elem.t[i] = 0
        for elem in spec_bullets:
            if elem.t == 0:
                elem.disapp()
                spec_bullets.remove(elem)
        for elem in mini_bullets:
            for i in range(8):
                if elem.t[i] > 0:
                    elem.t[i] -= 1
                elif elem.t[i] == 0:
                    elem.t[i] = -1
                    elem.disapp(i)
        for bomb in bombs:
            bomb_move(bomb)
        for elem in targets:
            if elem.bomb == 1:
                bombs.append(Bomb(elem))                
        for elem in targets:
            target_move(elem)
            if not elem.alive:
                elem.disapp(elem.x, elem.y, elem.r)
                targets.remove(elem)
                targets.append(Target())
        for elem in sp_targets:
            spec_target_move(elem)
            if not elem.alive:
                elem.disapp(elem.x, elem.y, elem.r)
                sp_targets.remove(elem)
                sp_targets.append(Target())
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
            for sp_targett in sp_targets:
                if hittest(sp_targett, elem):
                    sp_targett.alive = False
                    elem.t = 0
        for bomb in bombs:
            l = gun.l+bomb.r
            w = gun.w+bomb.r
            if abs(gun.x-bomb.x) <= l and abs(bomb.y-gun.y) <= w and bomb.act:
                gun.hp -= 1
                bomb.act = False
            if bomb.y >= (int(loc.size*loc.k)):
                bomb.disapp()
                bombs.remove(bomb)
        if gun.hp == 0:
            time_bar.disappear(size[0])
            time_bar.length = 0
            screen.fill(BACKGROUND_l)
            screen.blit(lost, (size[0]//2-40, size[1]//2))
            pg.display.update()
            pg.time.wait(500)
        loc.appear(loc_mode)
        pg.display.update()
        for target in targets:
            target.bomb = rnd.randint(1, freq)
        if enemy_gun_active:
            enemy_gun.disapp()
            enemy_gun.hp_app(size[0]-200)
            enemy_gun.app(gun)
            if enemy_gun.hp == 0:
                enemy_gun.color = RED_l
            for elem in bullets:
                l = enemy_gun.l+elem.r
                w = enemy_gun.w+elem.r
                if abs(enemy_gun.x-elem.x) <= l and abs(elem.y-enemy_gun.y) <= w and elem.t > 0:
                    elem.t = 0
                    enemy_gun.hp -= 1
            if enemy_gun.shoot == 1 and enemy_gun.hp > 0:
                enemy_bullets.append(E_Bullet(enemy_gun, gun))
            for elem in enemy_bullets:
                l = gun.l+elem.r
                w = gun.w+elem.r
                if abs(gun.x-elem.x) <= l and abs(elem.y-gun.y) <= w and elem.t > 0:
                    elem.t = 0
                    gun.hp -= 1
                if elem.t > 0:
                    elem.t -= 1
                    ebullet_move(elem, loc)
                elif elem.t == 0:
                    elem.t = -1
                    elem.disapp()
                else:
                    enemy_bullets.remove(elem)
            enemy_gun.shoot = rnd.randint(1, 80)
    if time_bar.length == 0 and not main_menu_mode: #screen update and clear
        game_mode = False
        gun.hp_disapp(20)
        enemy_gun.hp_disapp(size[0]-200)
        enemy_gun.hp = 10
        enemy_gun.color = GUN_l
        loc.disappear(loc_mode)
        for elem in spec_bullets:
            elem.disapp()
            elem.t = 0
            spec_bullets.remove(elem)
        for elem in mini_bullets:
            for i in range(8):
                elem.disapp(i)
                elem.t[i] = 0
            mini_bullets.remove(elem)
        for elem in bullets:
            elem.disapp(elem.x, elem.y)
            elem.t = 0
        for elem in enemy_bullets:
            elem.disapp()
            elem.t = 0
        for elem in bombs:
            elem.disapp()
            elem.y = int(loc.size*loc.k)
            elem.x = 0
        for elem in targets:
            elem.disapp(elem.x, elem.y, elem.r)
            elem.alive = False
        for elem in sp_targets:
            elem.disapp(elem.x, elem.y, elem.r)
            elem.alive = False
        gun.disapp(gun.x, gun.y, gun.l, gun.w, mouse_pos)
        gun.x, gun.y, gun.v = x_gun, y_gun, v_gun
        time_bar.length = size[0]
        Time_bar.color_factor = 255
        time_bar.color = (255-Time_bar.color_factor, Time_bar.color_factor, 50)
        main_menu_mode = True
        if difficulty == 0:
            super_shots = 2
            gun.hp = 5
            for target in targets:
                target.maxv = 5
            freq = 60
        elif difficulty == 1:
            super_shots = 1
            gun.hp = 3
            for target in targets:
                target.maxv = 7
            freq = 40
        elif difficulty == 2:
            super_shots = 1
            gun.hp = 3
            for target in targets:
                target.maxv = 9
            freq = 30
            enemy_gun_active = True
        screen.fill(BACKGROUND_l)
    
pg.time.wait(500)
pg.quit()