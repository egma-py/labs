from colors import *
from texts import *

import pygame.draw as pgd


"""
all classes here are menus
def appear to draw a menu in a new pos
def disappear to update screen without screen.fill()
def change_size_a to move a menu while appearing
def change_size_d to move a menu while disappearing
button check defs check if button is pushed depending on menu mode
"""
class MainMenu:
    def __init__(self):
        self.size_x = 0
        self.theme = 0
        
    def appear(self, size, screen):
        pgd.rect(screen, MENU_COLOR[self.theme], [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
        #begin button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2), (100, 35)])
        screen.blit(begin, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+8))
        #settings button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2+50), (100, 35)])
        screen.blit(settings, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+58))
        #Exit button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2+100), (100, 35)])
        screen.blit(exitt, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+108))
        
    def disappear(self, size, screen):
        pgd.rect(screen, BACKGROUND, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
    
    def change_size_a(self, size, FPS):
        self.size_x += size[0]/(2*FPS)
        if self.size_x > int(size[0]*0.375):
            self.size_x = int(size[0]*0.375)
            
    def change_size_d(self, size, FPS):
        self.size_x -= size[0]/(2*FPS)
        if self.size_x < 0:
            self.size_x = 0
            
    def button_b_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2)
        b_down = (size[1]//2+35)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False
        
    def button_e_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2+100)
        b_down = (size[1]//2+135)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False
        
    def button_s_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2+50)
        b_down = (size[1]//2+85)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False                   
        

class Settings:
    def __init__(self):
        self.size_x = 0
        self.theme = 0
    
    def appear(self, size, screen):
        pgd.rect(screen, MENU_COLOR[self.theme], [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
        #game time button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2-100), (100, 35)])
        screen.blit(game_duration, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-92))
        #difficulty button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2-50), (100, 35)])
        screen.blit(difficulty_txt, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-42))
        #theme button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2), (100, 35)])
        screen.blit(theme, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+8))
        #location button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2+50), (100, 35)])
        screen.blit(location, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+58))
        #return button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2+100), (100, 35)])
        screen.blit(returnn, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+108))
        
    def disappear(self, size, screen):
        pgd.rect(screen, BACKGROUND, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
    
    def change_size_a(self, size, FPS):
        self.size_x += size[0]/(2*FPS)
        if self.size_x > int(size[0]*0.375):
            self.size_x = int(size[0]*0.375)
            
    def change_size_d(self, size, FPS):
        self.size_x -= size[0]/(2*FPS)
        if self.size_x < 0:
            self.size_x = 0
            
    def button_r_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2+100)
        b_down = (size[1]//2+135)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False
    
    def button_gt_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2-100)
        b_down = (size[1]//2-65)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False
    
    def button_d_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2-50)
        b_down = (size[1]//2-15)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False
    
    def button_t_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2)
        b_down = (size[1]//2+35)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False
    
    def button_l_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2+50)
        b_down = (size[1]//2+85)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False

    
class GtMenu:
    def __init__(self):
        self.size_x = 0
        self.theme = 0
    
    def appear(self, size, screen):
        pgd.rect(screen, MENU_COLOR[self.theme], [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
        #10s button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2-100), (100, 35)])
        screen.blit(sec10, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-92))
        #20s button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2-50), (100, 35)])
        screen.blit(sec20, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-42))
        #30s button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2), (100, 35)])
        screen.blit(sec30, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+8))
        #60s button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2+50), (100, 35)])
        screen.blit(sec60, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+58))
        
    def disappear(self, size, screen):
        pgd.rect(screen, BACKGROUND, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
    
    def change_size_a(self, size, FPS):
        self.size_x += size[0]/(2*FPS)
        if self.size_x > int(size[0]*0.375):
            self.size_x = int(size[0]*0.375)
            
    def button_10_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2-100)
        b_down = (size[1]//2-65)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False
        
    def button_20_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2-50)
        b_down = (size[1]//2-15)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False

    def button_30_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2)
        b_down = (size[1]//2+35)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False
        
    def button_60_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2+50)
        b_down = (size[1]//2+85)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False
        
        
class DMenu:
    def __init__(self):
        self.size_x = 0
        self.theme = 0
    
    def appear(self, size, screen):
        pgd.rect(screen, MENU_COLOR[self.theme], [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
        #easy button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2-100), (100, 35)])
        screen.blit(easy, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-92))
        #medium button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2-50), (100, 35)])
        screen.blit(medium, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-42))
        #hard button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2), (100, 35)])
        screen.blit(hard, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2+8))
        
    def disappear(self, size, screen):
        pgd.rect(screen, BACKGROUND, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
    
    def change_size_a(self, size, FPS):
        self.size_x += size[0]/(2*FPS)
        if self.size_x > int(size[0]*0.375):
            self.size_x = int(size[0]*0.375)
            
    def button_e_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2-100)
        b_down = (size[1]//2-65)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False
        
    def button_m_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2-50)
        b_down = (size[1]//2-15)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False

    def button_h_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2)
        b_down = (size[1]//2+35)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False
        
        
class LMenu:
    def __init__(self):
        self.size_x = 0
        self.theme = 0
    
    def appear(self, size, screen):
        pgd.rect(screen, MENU_COLOR[self.theme], [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
        #plains button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2-100), (100, 35)])
        screen.blit(plain, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-92))
        #hills button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2-50), (100, 35)])
        screen.blit(hills, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-42))
        
    def disappear(self, size, screen):
        pgd.rect(screen, BACKGROUND, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
    
    def change_size_a(self, size, FPS):
        self.size_x += size[0]/(2*FPS)
        if self.size_x > int(size[0]*0.375):
            self.size_x = int(size[0]*0.375)
            
    def button_plain_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2-100)
        b_down = (size[1]//2-65)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False
        
    def button_hills_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2-50)
        b_down = (size[1]//2-15)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False
        
        
class TMenu:
    def __init__(self):
        self.size_x = 0
        self.theme = 0
    
    def appear(self, size, screen):
        pgd.rect(screen, MENU_COLOR[self.theme], [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
        #dark button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2-100), (100, 35)])
        screen.blit(dark, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-92))
        #light button
        pgd.rect(screen, BUTTON_COLOR[self.theme], [(size[0]-int(1.5*self.size_x-210), size[1]//2-50), (100, 35)])
        screen.blit(light, (size[0]-int(1.5*self.size_x-210)+8, size[1]//2-42))
        
    def disappear(self, size, screen):
        pgd.rect(screen, BACKGROUND, [(size[0]-int(self.size_x), 0), (int(self.size_x), size[1])])
    
    def change_size_a(self, size, FPS):
        self.size_x += size[0]/(2*FPS)
        if self.size_x > int(size[0]*0.375):
            self.size_x = int(size[0]*0.375)
            
    def button_dark_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2-100)
        b_down = (size[1]//2-65)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False
        
    def button_light_check(self, event, size):
        pos_x = event.pos[0]
        pos_y = event.pos[1]
        b_left = (size[0]-int(1.5*self.size_x-210))
        b_right = (size[0]-int(1.5*self.size_x-210)+100)
        b_up = (size[1]//2-50)
        b_down = (size[1]//2-15)
        if b_right > pos_x > b_left and  b_down > pos_y > b_up:
            return True
        else:
            return False