import pygame.draw as pgd
import pygame as pg
import math as m


def draw_tree(screen, x, y, size_x, size_y, color):
    #the center(x,y) of the tree is the point in the middle of its trunk
    #bottom part of trunk
    pgd.line(screen, color, [x, y + int(size_y/60)], 
                            [x, y + int(size_y/4)], 
                            int(size_x/18))
    pgd.line(screen, color, [x, y + int(17*size_y/60)], 
                            [x, y + int(size_y/2)], 
                            int(size_x/18))
    #right and bottom branch
    pgd.arc(screen, tree_color, [[x, y - int(5*size_y/57)], 
                                 [int(14*size_x/35), int(size_y/2 + 5*size_y/57)]],
                                 6*m.pi/14, 4*m.pi/5, 4)
    #top part of trunk
    pgd.polygon(screen, tree_color, [[x, y], 
                                     [x - int(size_x/22), y - int(size_y/80)], 
                                     [x, y - int(17.5*size_y/116)], 
                                     [x + int(size_x/22), y - int(16*size_y/116)]])
    pgd.polygon(screen, tree_color, [[x + int(size_x/80), y - int(size_y/6 + 0.5*size_y/100)], 
                                     [x - int(size_x/80), y - int(17*size_y/96)], 
                                     [x + int(size_x/18), y - int(size_y/2 + 1*size_y/100 )], 
                                     [x + int(7*size_x/86), y - int(size_y/2 + 0.5*size_y/100)]])
    #leaves on right and bottom branch
    delta_1 = int(5*size_x/37)
    for i in range(3):
        pgd.ellipse(screen, tree_color, [[x + delta_1, y - int(5*size_y/70)], 
                                         [int(size_x/40), int(5*size_y/35)]])
        delta_1 += int(3*size_x/60)
    
    #right and top branch and leaves on it
    pgd.arc(screen, tree_color, [[x + int(5*size_x/80), y - int(size_y/2)], 
                                 [int(size_x - 5*size_x/40), int(30*size_y/35)]],
            m.pi/2, 9*m.pi/10, 4)
    delta_2x = int(8*size_x/24)
    delta_2y = int(32*size_y/70)
    for i in range(5):
        pgd.ellipse(screen, tree_color, [[x + delta_2x, y - delta_2y], 
                                         [int(size_x/40), int(5*size_y/35)]])
        delta_2x += int(3*size_x/80)
        delta_2y += int(size_y/70)
    #left top branch and leaves
    pgd.arc(screen, tree_color, [[x - size_x, y - int(size_y/2)], 
                                 [size_x, size_y]],
            m.pi/10, m.pi/2, 4)
    delta_3x = int(2.5*size_x/8)
    delta_3y = int(3.5*size_y/8)
    for i in range(5):
        pgd.ellipse(screen, tree_color, [[x - delta_3x, y - delta_3y], 
                                         [int(size_x/40), int(5*size_y/35)]])
        delta_3x += int(3*size_x/80)
        delta_3y += int(size_y/70)
        #left top branch and leaves
    pgd.arc(screen, tree_color, [[x - int(22*size_x/48), y], 
                                 [int(22*size_x/48), int(size_y/2)]],
            m.pi/6, 2.5*m.pi/4, 4)
    delta_4 = int(size_x/6)
    for i in range(3):
        pgd.ellipse(screen, tree_color, [[x - delta_4, y], 
                                         [int(size_x/40), int(5*size_y/35)]])
        delta_4 += int(3*size_x/60)


def draw_panda(screen, x, y, size_x, size_y, color_1, color_2, background_color):
    #the center(x,y) of the panda is its nose
    #body of the panda
    pgd.ellipse(screen, color_2, [[x - int(5*size_x/53), y - int(25*size_y/60)],
                                  [int(47*size_x/53), int(27*size_y/60)]])
    #legs
    pgd.polygon(screen, color_1, [[x + int(28*size_x/53), y - int(23*size_y/60)],
                                  [x + int(28*size_x/53), y + int(4*size_y/60)],
                                  [x + int(23*size_x/53), y + int(20*size_y/60)],
                                  [x + int(18*size_x/53), y + int(27*size_y/60)],
                                  [x + int(4*size_x/53), y + int(20*size_y/60)],
                                  [x + int(13*size_x/53), y + int(12*size_y/60)]])
    pgd.polygon(screen, color_1, [[x - int(4*size_x/53), y - int(9*size_y/60)],
                                  [x + int(8*size_x/53), y - int(3*size_y/60)],
                                  [x + int(10*size_x/53), y + int(10*size_y/60)],
                                  [x + int(3*size_x/53), y + int(20*size_y/60)],
                                  [x - int(6*size_x/53), y + int(15*size_y/60)]])
    pgd.polygon(screen , background_color, [[x + int(18*size_x/53), y + int(27*size_y/60)],
                                            [x + int(12*size_x/53), y + int(25*size_y/60)],
                                            [x + int(20*size_x/53), y + int(25*size_y/60)]])
    pgd.polygon(screen , background_color, [[x + int(4*size_x/53), y + int(20*size_y/60)],
                                            [x + int(6*size_x/53), y + int(18*size_y/60)],
                                            [x + int(6*size_x/53), y + int(24*size_y/60)]])
    pgd.polygon(screen, color_1, [[x + int(40*size_x/53), y - int(10*size_y/60)],
                                  [x + int(40*size_x/53), y + int(8*size_y/60)],
                                  [x + int(30*size_x/53), y + int(21*size_y/60)],
                                  [x + int(20*size_x/53), y + int(15*size_y/60)]])
    pgd.polygon(screen , color_2, [[x + int(40*size_x/53), y - int(10*size_y/60)],
                                   [x + int(41*size_x/53), y - int(8*size_y/60)],
                                   [x + int(37*size_x/53), y - int(8*size_y/60)]])
    pgd.polygon(screen , background_color, [[x + int(42*size_x/53), y + int(8*size_y/60)],
                                            [x + int(38*size_x/53), y + int(13*size_y/60)],
                                            [x + int(40*size_x/53), y + int(6*size_y/60)]])
    pgd.polygon(screen , background_color, [[x + int(30*size_x/53), y + int(21*size_y/60)],
                                            [x + int(32*size_x/53), y + int(19*size_y/60)],
                                            [x + int(26*size_x/53), y + int(19*size_y/60)]])
    #ears 1
    pgd.ellipse(screen, color_1, [[x + int(15*size_x/53), y - int(30*size_y/60)],
                                  [int(12*size_x/53), int(20*size_y/60)]])
    pgd.ellipse(screen, color_1, [[x - int(6*size_x/53), y - int(32*size_y/60)],
                                  [int(16*size_x/53), int(15*size_y/60)]])
    #head
    pgd.polygon(screen, color_2, [[x, y],
                                  [x + int(25*size_x/55), y - int(7*size_y/65)],
                                  [x + int(25*size_x/55), y- int(25*size_y)/65],
                                  [x + int(25*size_x/110), y - int(35*size_y/65)],
                                  [x, y - int(30*size_y/65)],
                                  [x - int(5*size_x/55), y - int(30*size_y/130)]])
    pgd.polygon(screen, background_color, [[x + int(25*size_x/110), y - int(35*size_y/63)],
                                           [x + int(9*size_x/53), y - int(31*size_y/60)],
                                           [x + int(15*size_x/53), y - int(30*size_y/60)]]) 
    pgd.polygon(screen, color_1, [[x + int(25*size_x/55), y - int(7*size_y/65)],
                                  [x + int(21*size_x/53), y - int(5*size_y/60)],
                                  [x + int(24*size_x/53), y - int(9*size_y/60)]])
    #eyes, nose and ears 2
    pgd.ellipse(screen, color_1, [[x - int(3*size_x/50), y - int(3*size_y/55)], 
                                  [int(3*size_x/25), int(4*size_y/55)]])
    pgd.ellipse(screen, color_1, [[x - int(5*size_x/53), y - int(15*size_y/60)],
                                  [int(6*size_x/53), int(7*size_y/60)]])
    pgd.circle(screen, color_1, (x + int(10*size_x/53), y - int(10*size_y/60)), int(4*size_x/53))
    pgd.polygon(screen, color_1, [[x - int(3*size_x/53), y - int(19*size_y/60)],
                                  [x + int(6*size_x/53), y - int(30*size_y/60)],
                                  [x - int(1*size_x/53), y - int(29*size_y/60)]])
    pgd.polygon(screen, color_1, [[x + int(24*size_x/53), y - int(12*size_y/60)],
                                  [x + int(20*size_x/53), y - int(30*size_y/60)],
                                  [x + int(26*size_x/53), y - int(25*size_y/60)]])    


pg.init()

#define variables
FPS = 30
background_color = (255, 184, 135)
display_size = (1300, 700)
tree_color = (0, 80, 31)
panda_color_black = (0, 0, 0)
panda_color_white = (255, 255, 255)

#set surface
screen = pg.display.set_mode(display_size)
screen.fill(background_color)

#body
draw_tree(screen, 550, 225, 600, 430, tree_color)
draw_tree(screen, 370, 300, 230, 325, tree_color)
draw_tree(screen, 160, 310, 300, 300, tree_color)
draw_tree(screen, 1120, 225, 270, 410, tree_color)
draw_panda(screen, 600, 400, 250, 270, panda_color_black, panda_color_white, background_color)
draw_panda(screen, 480, 500, 100, 110, panda_color_black, panda_color_white, background_color)

pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()