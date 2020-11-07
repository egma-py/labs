from colors import *

import random as rnd
import math as m
import pygame.draw as pgd

"""
class Gun is us
def app to draw gun in a new pos
def disapp to update screen without screen.fill
def hp_app to show hp
def hp_disapp to update screen, without screen.fill
defs right and left are to move
def shoot to shoot
"""
class Gun:
    def __init__(self, hp, size):
        self.v = 5
        self.x = size[0]//2
        self.y = int(size[1]*0.75)-5
        self.l = 21
        self.w = 10
        self.lc = 15
        self.wc = 4
        self.hp = hp
        self.color = list(GUN_COLOR)

    def app(self, pos, screen):
        if (self.y-pos[1]) <= 0:
            arctg = 0
            x2 = self.x
            y2 = self.y - int(self.lc)
        else:
            arctg = m.atan((pos[0]-self.x)/(self.y-pos[1]))
            x2 = int(self.x + self.lc*m.sin(arctg))
            y2 = int(self.y - self.lc*m.cos(arctg))
        pgd.rect(screen, GUN_COLOR, [(self.x-self.l, self.y-self.w//2), (int(2*self.l), self.w)])
        pgd.rect(screen, GUN_COLOR, [(self.x-self.l, self.y-self.w//2-self.w), (3, self.w)])
        pgd.line(screen, self.color, (self.x, self.y-self.w//2), (x2, y2), self.wc)
        
    def disapp(self, pos, screen):
        pgd.rect(screen, BACKGROUND, [(self.x-35, self.y-35), (70, 40)])
        
    def hp_app(self, x, screen):
        pgd.rect(screen, BACKGROUND, ((x, 20), (120, 15)))
        hpx = x
        for i in range(self.hp):
            pgd.rect(screen, RED, ((hpx, 20), (20, 15)))
            hpx += 25
    
    def hp_disapp(self, x, screen):
        pgd.rect(screen, BACKGROUND, ((x, 20), (120, 15)))
    
    def right(self):
        self.x += self.v
        
    def left(self):
        self.x -= self.v
        
    def shoot(self, bullet, screen):
        bullet.app(screen)
        
    
"""
class Enemy is our enemy
def app to draw gun in a new pos
def disapp to update screen without screen.fill
def hp_app to show hp
def hp_disapp to update screen, without screen.fill
"""
class Enemy:
    def __init__(self, size):
        self.x = size[0]-15
        self.y = size[1]-400
        self.hp = 10
        self.shoot = 0
        self.l = 20
        self.w = 10
        self.hp = 10
        
    def app(self, obj, screen):
        arctg = m.atan((obj.y-self.y)/(obj.x-self.x))
        if obj.x-self.x == 0:
            x2 = self.x
            y2 = self.y + self.l
        else:
            x2 = -int(self.l*m.cos(arctg))+self.x
            y2 = int(self.l*m.sin(-arctg))+self.y
        pgd.rect(screen, GUN_COLOR, ((self.x-20, self.y-2), (70, 2)))
        pgd.rect(screen, GUN_COLOR, ((self.x-10, self.y), (20, 10)))
        pgd.line(screen, GUN_COLOR, (self.x, self.y+10), (x2, y2), 5)
        
    def disapp(self, screen):
        pgd.rect(screen, BACKGROUND, ((self.x-20, self.y-2), (70, 2)))
        pgd.rect(screen, BACKGROUND, ((self.x-10, self.y), (20, 10)))
        pgd.rect(screen, BACKGROUND, ((self.x-20, self.y+10), (40, 30)))
        
    def hp_app(self, x, screen):
        pgd.rect(screen, BACKGROUND, ((x, 20), (150, 15)))
        hpx = x
        for i in range(self.hp):
            pgd.rect(screen, BLUE, ((hpx, 20), (10, 15)))
            hpx += 15
    
    def hp_disapp(self, x, screen):
        pgd.rect(screen, BACKGROUND, ((x, 20), (150, 15)))
        
  
"""
class EBullet is enemy's bullet
defs app, disapp are described in Gun description
def change to move it according to gravity
def move includes app, disapp, change
"""    
class EBullet:
    def __init__(self, gun, obj, size):
        self.x = gun.x
        self.y = gun.y
        self.vy = 0
        self.vx = -int(((size[0]-obj.x)/size[0])*30)
        self.t = 100
        self.r = 7
        self.theme = 0
        
    def app(self, screen):
        pgd.circle(screen, GUN_COLOR[self.theme], (self.x, self.y), self.r)

    def disapp(self, screen):
        pgd.circle(screen, BACKGROUND, (self.x, self.y), self.r)
        
    def change(self, loc):
        self.x += self.vx
        self.y += self.vy
        self.vy += 1
        if self.y >= loc.size*loc.k:
            self.vy = -int(0.8 * self.vy)
            self.y += self.vy
            
    def move(self, loc, screen):
        self.disapp(screen)
        self.change(loc)
        self.app(screen)
        

"""
class Target is an enemy which can't kill us
defs app, disapp are described in Gun description
def change to move it according to gravity
def move includes app, disapp, change
defs with 'special' are for spec targets
"""            
class Target:
    def __init__(self, size):
        self.x = rnd.randint(30, size[0]-30)
        self.y = rnd.randint(30, int(size[1]*0.45))
        self.r = rnd.randint(10, 20)
        self.maxv = 5
        self.vx = rnd.randint(3, self.maxv)
        self.vy = rnd.randint(3, self.maxv)
        self.alive = True
        self.color = TARGET_COLORS[5-rnd.randint(1, 5)]
        self.s1_color = S_COLORS1[3-rnd.randint(1, 3)]
        self.s2_color = S_COLORS2[3-rnd.randint(1, 3)]
        self.bomb = 0
        self.theme = 0
        
        
    def app(self, screen):
        pgd.circle(screen, self.color, (self.x, self.y), self.r)
        
        
    def disapp(self, screen):
        pgd.circle(screen, BACKGROUND, (self.x, self.y), self.r)
    
        
    def change(self, size):
        self.x += self.vx
        if self.x >= size[0]-self.r or self.x <= self.r:
            self.vx = -self.vx
            self.x += self.vx
    
    
    def special_app(self, screen):
        pgd.circle(screen, self.s1_color, (self.x, self.y), self.r)
        pgd.circle(screen, self.s2_color, (self.x, self.y), self.r//2)
        
        
    def special_change(self, size):
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
            
            
    def move(self, size, screen):
            self.disapp(screen)
            self.change(size)
            self.app(screen)
            
            
    def special_move(self, size, screen):
            self.disapp(screen)
            self.special_change(size)
            self.special_app(screen)
            
        
"""
class Bullet is our bul which can kill targets & enemy
defs app, disapp are described in Gun description
def change to move it according to gravity
def move includes app, disapp, change
"""    
class Bullet:
    def __init__(self, gun, pos, v):
        if (gun.y-pos[1]) <= 0:
            arctg = 0
            self.x = gun.x
            self.y = gun.y - gun.l
        else:
            arctg = m.atan((pos[0]-gun.x)/(gun.y-pos[1]))
            self.x = int(gun.x + gun.l*m.sin(arctg))
            self.y = int(gun.y - gun.l*m.cos(arctg))
        self.v = v
        self.vx = -int(self.v*m.sin(arctg))
        self.vy = int(self.v*m.cos(arctg))
        self.t = 100
        self.r = 7
        self.active = False
        self.color = RED
        self.theme = 0
        

    def app(self, screen):
        pgd.circle(screen, self.color, (self.x, self.y), self.r)

    def disapp(self, screen):
        pgd.circle(screen, BACKGROUND, (self.x, self.y), self.r)
        
    def change(self, loc):
        self.x -= self.vx
        self.y -= self.vy
        self.vy -= 1
        if self.y >= loc.size*loc.k:
            self.vy = -int(0.8 * self.vy)
            self.y -= self.vy
    
    def move(self, loc, screen):
        self.disapp(screen)
        self.change(loc)
        self.app(screen)
        
        
"""
class SpecBullet is ea bullet which creates mini bullets
defs app, disapp are described in Gun description
def change to move it according to gravity
def move includes app, disapp, change
"""    
class SpecBullet:
    def __init__(self, gun, v):
        self.x = gun.x - gun.l
        self.y = gun.y - gun.w
        self.v = v
        self.color = TARGET_COLORS[5-rnd.randint(1, 5)]
        self.r = 10
        self.t = 10
        self.theme = 0
        
    def app(self, screen):
        pgd.circle(screen, self.color, (self.x, self.y), self.r)
        
    def disapp(self, screen):
        pgd.circle(screen, BACKGROUND, (self.x, self.y), self.r)
        
    def change(self):
        self.y -= self.v
        self.v -= 1
        
    def move(self, screen):
        self.disapp(screen)
        self.change()
        self.app(screen)

        
"""
class MiniBullet is a bullet which can kill targets
defs app, disapp are described in Gun description
def change to move it according to gravity
def move includes app, disapp, change
"""    
class MiniBullets:
    def __init__(self, obj): #obj is spec target
        self.vx = [13, 9, 0, -9, -13, -9, 0, 9]
        self.vy = [0, 9, 13, 9, 0, -9, -13, -9]
        self.x = [obj.x, obj.x, obj.x, obj.x, obj.x, obj.x, obj.x, obj.x]
        self.y = [obj.y, obj.y, obj.y, obj.y, obj.y, obj.y, obj.y, obj.y]
        self.r = 7
        self.t = [60, 60, 60, 60, 60, 60, 60, 60]
        self.color = []
        self.theme = 0
        for i in range(8):
            self.color.append(TARGET_COLORS[5-rnd.randint(1, 5)])
        
    def app(self, k, screen):
        pgd.circle(screen, self.color[k], (self.x[k], self.y[k]), self.r)
            
    def disapp(self, k, screen):
        pgd.circle(screen, BACKGROUND, (self.x[k], self.y[k]), self.r)
    
    def change(self, k):
        self.x[k] += self.vx[k]
        self.y[k] += self.vy[k]
        self.vy[k] += 1
        
    def move(self, screen, k):
        self.disapp(k, screen)
        self.change(k)
        self.app(k, screen)


"""
class Bomb is targets' bullet which can kill us
defs app, disapp are described in Gun description
def change to move it according to gravity
def move includes app, disapp, change
"""    
class Bomb:
    def __init__(self, target):
        self.x = target.x
        self.y = target.y
        self.v = 1
        self.color = TARGET_COLORS[5-rnd.randint(1, 5)]
        self.r = 7
        self.act = True
        self.theme = 0
        
    def app(self, screen):
        pgd.circle(screen, self.color, (self.x, self.y), self.r)
        pgd.circle(screen, (0, 0, 0), (self.x, self.y), self.r, 2)
        
    def disapp(self, screen):
        pgd.circle(screen, BACKGROUND, (self.x, self.y), self.r+1)
        
    def change(self):
        self.y += self.v
        self.v += 1
    
    def move(self, screen):
        self.disapp(screen)
        self.change()
        self.app(screen)


"""
class Location is a game location
defs app, disapp are described in Gun description
"""
class Location:
    def __init__(self, plain_type, size):
        self.plain_type = plain_type
        self.k = 0.75
        self.size = size[1]
        self.theme = 0
        
    def appear(self, plain_type, screen, size):
        if self.plain_type:
            pgd.rect(screen, LOC_COLOR[self.theme], [(0, int(self.size*self.k)), (size[0], int(self.size*(1-self.k)))])
        else:
            pass
            
    def disappear(self, plain_type, screen, size):
        if self.plain_type:
            pgd.rect(screen, BACKGROUND, [(0, int(self.size*self.k)), (size[0], int(self.size*(1-self.k)))])
        else:
            pass      
        