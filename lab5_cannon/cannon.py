from colors import *
from objects import *
from menus import *

import random as rnd
import pygame as pg
import pygame.draw as pgd
import math as m


"""
class TimeBar visualises how many time left
def appear to update pos of timebar
def disappear to clear screen without screen.fill()
def shorten shortens length depending on amount of game time left
def change_color changes color depending on length
"""
class TimeBar:
    color_factor = 255
    color = ((255 - color_factor), color_factor, 50)
    def __init__(self, sec, length, background_color):
        self.background_color = background_color
        self.sec = FPS * sec
        self.length = length
        self.theme = 0
            
    def appear(self):
        pgd.rect(screen, TimeBar.color, [(0, 0), (int(self.length), 5)])
        
    def disappear(self):
        pgd.rect(screen, self.background_color, [(0, 0), (int(self.length), 5)])
        
    def shorten(self):
        self.length -= (size[0])/self.sec 
        if self.length < 0:
            self.length = 0
        
    def change_color(self):
        TimeBar.color_factor -= (255)/self.sec
        if TimeBar.color_factor < 0:
            TimeBar.color_factor = 0
        TimeBar.color = ((255 - int(TimeBar.color_factor)), int(TimeBar.color_factor), 50)


#menu show
def menu_appear(menu, size, screen, FPS):
    menu.disappear(size, screen)
    menu.change_size_a(size, FPS)
    menu.appear(size, screen)

#removing menu before the game starts
def menu_disappear(menu, size, screen, FPS):
    menu.disappear(size, screen)
    menu.change_size_d(size, FPS)
    menu.appear(size, screen)   

#motion of timebar
def time_bar_begin(tb):
    tb.disappear()
    tb.shorten()
    tb.change_color()
    tb.appear()

#checking if menu activated(if active - activate its buttons)
def buttons_activated(statement):
    if statement:
        return True
    else:
        return False
    
#hittest to reduce hp or kill
def hittest(bullett, targett):
    s = m.sqrt((bullett.x-targett.x)**2+(bullett.y-targett.y)**2)
    if s < (bullett.r + targett.r):
        return True
    else:
        return False

#hittest of minibullets
def spec_hittest(bullet, target):
    s = m.sqrt((bullet.x[i]-target.x)**2+(bullet.y[i]-target.y)**2)
    if s < (bullet.r + target.r):
        return True
    else:
        return False    
    
    
pg.init()

FPS = 30
size = (800, 600)
screen = pg.display.set_mode(size)

pg.display.update()
clock = pg.time.Clock()

#defining additional constants  
game_time = 20
time_counter = 0
menu_time = 2*FPS
settings_time = 2*FPS
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
time_bar = TimeBar(game_time, size[0], BACKGROUND)
main_menu = MainMenu()
set_menu = Settings()
gt_menu = GtMenu()
d_menu = DMenu()
l_menu = LMenu()
t_menu = TMenu()
gun = Gun(heart_points, size)
enemy_gun = Enemy(size)
bullets = []
enemy_bullets = []
bombs = []
targets = []
sp_targets = []
spec_bullets = []
mini_bullets = []
for i in range(tg_amounts):
    targets.append(Target(size))
for i in range(tg_amounts):
    sp_targets.append(Target(size))
bombs = []
loc = Location(loc_mode, size)
game_objects = [time_bar, main_menu, set_menu, gt_menu, d_menu, l_menu,
                t_menu, enemy_gun, loc]
screen.fill(BACKGROUND)

while not finished:
    clock.tick(FPS)
    keys = pg.key.get_pressed()
    mouse_pos = pg.mouse.get_pos()
    m1 = pg.mouse.get_pressed()[0]
    if game_mode and main_menu.size_x==0: #defining power of gun's shot
        if m1 == 1:
            if v != 40:
                v += 1
                gun.lc += 0.5
                gun.color[0] += 6
    if game_mode and main_menu.size_x==0: #controlling
        if keys[pg.K_RIGHT]:
            gun.disapp(mouse_pos, screen)
            if gun.x >= size[0]-21:
                gun.x = size[0]-21
            else:
                gun.right()
        elif keys[pg.K_LEFT]:
            gun.disapp(mouse_pos, screen)
            if gun.x <= 21:
                gun.x = 21
            else:
                gun.left()
        elif pg.mouse.get_focused():
            gun.disapp(mouse_pos, screen)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        #checking if spec bul buttons is pushed
        if event.type == pg.MOUSEBUTTONDOWN and game_mode and event.button==3 and main_menu.size_x==0 and super_shots > 0:
            spec_bullets.append(Spec_Bullet(gun, spec_v))
            super_shots -= 1
        #checking if the gun shots
        if event.type == pg.MOUSEBUTTONUP and game_mode and event.button==1 and main_menu.size_x==0:
            bullets.append(Bullet(gun, mouse_pos, v))
            new_bullet = Bullet(gun, mouse_pos, v)
            gun.shoot(new_bullet, screen)
            new_bullet.disapp(screen)
            v = 1
            gun.lc = 15
            gun.color[0] = 0
        if event.type == pg.MOUSEBUTTONDOWN: #checking buttons' pushes
            if buttons_activated(main_menu_mode):
                if event.button == 1 and main_menu.button_e_check(event, size):
                    finished = True
                if event.button == 1 and main_menu.button_s_check(event, size):
                    settings_mode = True
                    main_menu_mode = False
                if event.button == 1 and main_menu.button_b_check(event, size):
                    game_mode = True
                    main_menu_mode = False
            elif buttons_activated(settings_mode):
                if event.button == 1 and set_menu.button_r_check(event, size):
                    settings_mode = False
                    main_menu_mode = True
                if event.button == 1 and set_menu.button_d_check(event, size):
                    settings_mode = False
                    d_menu_mode = True
                if event.button == 1 and set_menu.button_l_check(event, size):
                    settings_mode = False
                    l_menu_mode = True
                if event.button == 1 and set_menu.button_gt_check(event, size):
                    settings_mode = False
                    gt_menu_mode = True
                if event.button == 1 and set_menu.button_t_check(event, size):
                    settings_mode = False
                    t_menu_mode = True
            elif buttons_activated(gt_menu_mode):
                if event.button == 1 and gt_menu.button_10_check(event, size):
                    settings_mode = True
                    gt_menu_mode = False
                    game_time = 10
                    time_bar.sec = 10*FPS
                if event.button == 1 and gt_menu.button_20_check(event, size):
                    settings_mode = True
                    gt_menu_mode = False
                    game_time = 20
                    time_bar.sec = 20*FPS
                if event.button == 1 and gt_menu.button_30_check(event, size):
                    settings_mode = True
                    gt_menu_mode = False
                    game_time = 30
                    time_bar.sec = 30*FPS
                if event.button == 1 and gt_menu.button_60_check(event, size):
                    settings_mode = True
                    gt_menu_mode = False
                    game_time = 60
                    time_bar.sec = 60*FPS
            elif buttons_activated(d_menu_mode):
                if event.button == 1 and d_menu.button_e_check(event, size):
                    settings_mode = True
                    d_menu_mode = False
                    difficulty = 0
                    super_shots = 2
                    gun.hp = 5
                    for target in targets:
                        target.maxv = 5
                    freq = 60
                if event.button == 1 and d_menu.button_m_check(event, size):
                    settings_mode = True
                    d_menu_mode = False
                    difficulty = 1
                    super_shots = 1
                    gun.hp = 3
                    for target in targets:
                        target.maxv = 7
                    freq = 40
                if event.button == 1 and d_menu.button_h_check(event, size):
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
                if event.button == 1 and l_menu.button_hills_check(event, size):
                    settings_mode = True
                    l_menu_mode = False
                if event.button == 1 and l_menu.button_plain_check(event, size):
                    settings_mode = True
                    l_menu_mode = False
            elif buttons_activated(t_menu_mode):
                if event.button == 1 and t_menu.button_dark_check(event, size):
                    settings_mode = True
                    t_menu_mode = False
                    for elem in game_objects:
                        elem.theme = 1
                if event.button == 1 and t_menu.button_light_check(event, size):
                    settings_mode = True
                    t_menu_mode = False
                    for elem in game_objects:
                        elem.theme = 0
    if main_menu_mode: #appearing menus depending in menus' statuses
        menu_appear(main_menu, size, screen, FPS)
        pg.display.update()
    if settings_mode:
        menu_appear(set_menu, size, screen, FPS)
        pg.display.update()
    if gt_menu_mode:
        menu_appear(gt_menu, size, screen, FPS)
        pg.display.update()
    if d_menu_mode:
        menu_appear(d_menu, size, screen, FPS)
        pg.display.update()
    if l_menu_mode:
        menu_appear(l_menu, size, screen, FPS)
        pg.display.update()
    if t_menu_mode:
        menu_appear(t_menu, size, screen, FPS)
        pg.display.update()
    if game_mode and not main_menu_mode: 
        menu_disappear(main_menu, size, screen, FPS)
        pg.display.update()
    if game_mode and main_menu.size_x == 0: #game
        time_bar_begin(time_bar)
        gun.app(mouse_pos, screen)
        gun.hp_app(20, screen)
        for elem in spec_bullets: #spec bul motion & checking alive
            if elem.t != 0:
                elem.move(screen)
            if elem.v == 0:
                elem.t = 0
                elem.disapp(screen)
                mini_bullets.append(Mini_Bullets(elem))
        for elem in mini_bullets: #mini bul motion $ checking alive
            for i in range(8):
                if elem.t[i] > 0:
                    elem.move(screen, i)
                for target in targets:
                    if spec_hittest(elem, target) and elem.t[i] > 0:
                        target.alive = False
                        elem.t[i] = 0
                for targett in sp_targets:
                    if spec_hittest(elem, targett) and elem.t[i] > 0:
                        targett.alive = False
                        elem.t[i] = 0
        for elem in spec_bullets: #removing not active spec bul
            if elem.t == 0:
                elem.disapp(screen)
                spec_bullets.remove(elem)
        for elem in mini_bullets: #shorten lifetime of mini bul
            for i in range(8):
                if elem.t[i] > 0:
                    elem.t[i] -= 1
                elif elem.t[i] == 0:
                    elem.t[i] = -1
                    elem.disapp(i, screen)
        for bomb in bombs: #bombs motion
            bomb.move(screen)
        for elem in targets: #creating bombs
            if elem.bomb == 1:
                bombs.append(Bomb(elem))                
        for elem in targets: #targets' motion
            elem.move(size, screen)
            if not elem.alive:
                elem.disapp(screen)
                targets.remove(elem)
                targets.append(Target(size))
        for elem in sp_targets: #spec targets' motion
            elem.special_move(size, screen)
            if not elem.alive:
                elem.disapp(screen)
                sp_targets.remove(elem)
                sp_targets.append(Target(size))
        for elem in bullets: #bul motion & checking alive
            if elem.t > 0:
                elem.t -= 1
                elem.move(loc, screen)
            elif elem.t == 0:
                elem.t = -1
                elem.disapp(screen)
            else:
                bullets.remove(elem)
            for targett in targets: #hittest target & bul
                if hittest(targett, elem):
                    targett.alive = False
                    elem.t = 0
            for sp_targett in sp_targets: #hittest sp target & bul
                if hittest(sp_targett, elem):
                    sp_targett.alive = False
                    elem.t = 0
        for bomb in bombs: #hittest bomb & gun
            l = gun.l+bomb.r
            w = gun.w+bomb.r
            if abs(gun.x-bomb.x) <= l and abs(bomb.y-gun.y) <= w and bomb.act:
                gun.hp -= 1
                bomb.act = False
            if bomb.y >= (int(loc.size*loc.k)):
                bomb.disapp(screen)
                bombs.remove(bomb)
        if gun.hp == 0: #if gun is dead
            time_bar.disappear()
            time_bar.length = 0
            screen.fill(BACKGROUND)
            screen.blit(lost, (size[0]//2-40, size[1]//2))
            pg.display.update()
            pg.time.wait(500)
        loc.appear(loc_mode, screen, size)
        pg.display.update()
        for target in targets: #creating bombs randomly
            target.bomb = rnd.randint(1, freq)
        if enemy_gun_active: #enemy gun motion
            enemy_gun.disapp(screen)
            enemy_gun.hp_app(size[0]-200, screen)
            enemy_gun.app(gun, screen)
            if enemy_gun.hp == 0:
                enemy_gun.color = RED
            for elem in bullets: #hittest bul & enemy
                l = enemy_gun.l+elem.r
                w = enemy_gun.w+elem.r
                if abs(enemy_gun.x-elem.x) <= l and abs(elem.y-enemy_gun.y) <= w and elem.t > 0:
                    elem.t = 0
                    enemy_gun.hp -= 1
            if enemy_gun.shoot == 1 and enemy_gun.hp > 0: # if enemy shots
                enemy_bullets.append(EBullet(enemy_gun, gun, size))
            for elem in enemy_bullets: #hittest gun & ebul
                l = gun.l+elem.r
                w = gun.w+elem.r
                if abs(gun.x-elem.x) <= l and abs(elem.y-gun.y) <= w and elem.t > 0:
                    elem.t = 0
                    gun.hp -= 1
                if elem.t > 0:
                    elem.t -= 1
                    elem.move(loc, screen)
                elif elem.t == 0:
                    elem.t = -1
                    elem.disapp(screen)
                else:
                    enemy_bullets.remove(elem)
            enemy_gun.shoot = rnd.randint(1, 80)
    if time_bar.length == 0 and not main_menu_mode: #screen update and clear
        game_mode = False
        gun.hp_disapp(20, screen)
        enemy_gun.hp_disapp(size[0]-200, screen)
        enemy_gun.hp = 10
        enemy_gun.color = GUN_COLOR
        loc.disappear(loc_mode, screen, size)
        for elem in spec_bullets: #clearing screen & refreshing obj lists
            elem.disapp(screen)
            elem.t = 0
            spec_bullets.remove(elem)
        for elem in mini_bullets:
            for i in range(8):
                elem.disapp(i, screen)
                elem.t[i] = 0
            mini_bullets.remove(elem)
        for elem in bullets:
            elem.disapp(screen)
            elem.t = 0
        for elem in enemy_bullets:
            elem.disapp(screen)
            elem.t = 0
        for elem in bombs:
            elem.disapp(screen)
            elem.y = int(loc.size*loc.k)
            elem.x = 0
        for elem in targets:
            elem.disapp(screen)
            elem.alive = False
        for elem in sp_targets:
            elem.disapp(screen)
            elem.alive = False
        gun.disapp(mouse_pos, screen)
        gun.x, gun.y, gun.v = size[0]//2, int(size[1]*0.75)-5, 5
        time_bar.length = size[0]
        TimeBar.color_factor = 255
        time_bar.color = (255-TimeBar.color_factor, TimeBar.color_factor, 50)
        main_menu_mode = True
        if difficulty == 0: #updating data depending on diff
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
        screen.fill(BACKGROUND)

pg.quit()