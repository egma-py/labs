#рефакторинг проекта Норайра Геворгяна
import pygame as pg
import pygame.draw as pgd
import math as m


pg.init()

#colors
GREEN = (55, 200, 113)
BLACK = (0,0,0)
FENCE_COLOR = (200, 171, 55)
WALL_COLOR = (200, 171, 55)
ROOF_COLOR = (212, 170, 0)
GRAY = (108, 103, 83)
DARK_GRAY = (40, 39, 31)
BLUE = (95, 188, 211)

FPS = 30
screen = pg.display.set_mode((400, 600))


def main():
    grass(screen, GREEN)
    fence(screen, BLACK, FENCE_COLOR)
    sky(screen, BLUE)
    dog(screen, GRAY, DARK_GRAY)
    dog_house(screen, WALL_COLOR, ROOF_COLOR, BLACK)
     

def grass(screen, color):
    pgd.rect(screen, color, (0, 350, 600, 250))


def fence(screen, line_color, fence_color):
    x1 = 0; y1 = 100
    x2 = 500; y2 = 350
    fence_parameters = (x1, y1, x2 - x1, y2 - y1)
    #draws fence's background
    pgd.rect(screen, fence_color, fence_parameters)
    #draws lines on background
    pgd.line(screen, line_color, (0, y2), (x2, y2))
    N = 19
    h = (x2 - x1) // (N + 1)
    x = x1 + h
    for i in range(N):
        pgd.line(screen, line_color, (x, y1), (x, y2))
        x += h


def sky(screen, color):
    pgd.rect(screen, color, (0, 0, 600, 100))
    
    
def dog(screen, dog_color, box_color, x=50, y=400, wh_color=(255, 255, 255), bl_color=(0, 0, 0)):
    '''
    the center(x, y) of the dog is its right ear
    '''
    def body() :
        body_parameters = (
        (x+20, y+25, 110, 60),
        (x+80, y+18, 70, 40),
        (x+50, y+45, 30, 70),
        (x+10, y+35, 30, 70),
        (x+110, y+45, 15, 50),
        (x+150, y+70, 15, 40),
        (x+40, y+110, 30, 15),
        (x, y+100, 30, 15),
        (x+100, y+90, 20, 10),
        (x+140, y+105, 20, 10),
        (x+80, y+15, 40, 40),
        (x+125, y+40, 40, 40),
        )
        '''
        the sequence of drawing
        the body is:
        chest, back, 4 legs, 4 feet , 2 thighs 
        each part is drawn with the only ellipse
        '''
        for elem in body_parameters:
            pgd.ellipse(screen, dog_color, elem)
    body()
    def head():
        s = 56
        head_parameters = (
        (dog_color, (x, y, s, s), (0, 0)),
        (box_color, (x, y, s, s), (2, 2)),
        (dog_color, (x - s//10, y, s//5, s//3 ), (0, 0)),
        (box_color, (x - s//10, y, s//5, s//3 ), (2, 2)),
        (dog_color, (x + s - s//10, y, s//5, s//3 ), (0, 0)),
        (box_color, (x + s - s//10, y, s//5, s//3 ), (2, 2)),
        (wh_color, (x + s//8, y + s//4, s//4, s//8), (0, 0)),
        (box_color, (x + s//8, y + s//4, s//4, s//8), (1, 1)),
        (bl_color, (x + 3*s//16, y + 4*s//16, s//8, s//8), (0, 0)),
        (wh_color, (x + 5*s//8, y + s//4, s//4, s//8), (0, 0)),
        (box_color, (x + 5*s//8, y + s//4, s//4, s//8), (1, 1)),
        (bl_color, (x + 11*s//16, y + 4*s//16, s//8, s//8), (0, 0)),
        (bl_color, (x + s//4, y + 3*s//4, s//2, s//3), (m.pi//16, m.pi)),
        (wh_color, [(x+s//3, y+4*s//5), (x+s//3, y+7*s//10), (x+7*s//18, y+15*s//20)], (0, 0)),
        (wh_color, [(x+s-s//3, y+4*s//5), (x+s-s//3, y+7*s//10), (x+s-7*s//18, y+15*s//20)], (0, 0)),
        )
        '''
        the sequence of drawing
        the head is:
        head(2 rects), 2 ears(each ear - 2 ellipses), 2 eyes(each eye - 3 ellipses), 
        mouth(1 arc), teeth(each tooth - 1 polygon)
        '''
        k = 1
        for elem in head_parameters:
            if k < 3:
                pgd.rect(screen, elem[0], elem[1], elem[2][0])
            elif k == 13:
                pgd.arc(screen, elem[0], elem[1], elem[2][0], elem[2][1])
            elif k > 13:
                pgd.polygon(screen, elem[0], elem[1], elem[2][0])
            else:
                pgd.ellipse(screen, elem[0], elem[1], elem[2][0])
            k = k + 1
    head()

def dog_house(screen, wall_color, roof_color, chain_color, x=275, y=375, bl_color=(0, 0, 0)):
    def house(): 
        house_parameters = (
        (wall_color, ((x, y), (x+75, y+30), (x+100, y), (x+100, y+80), (x+75, y+110), (x, y+80)), 0),
        (roof_color, ((x, y), (x+75, y+30), (x+100, y), (x+70, y-70), (x+40, y-55)), 0),
        (bl_color, ((x, y), (x+75, y+30), (x+75, y+110), (x, y+80)), 1),
        (bl_color, ((x+75, y+30), (x+100, y), (x+100, y+80), (x+75, y+110)), 1),
        (bl_color, ((x, y), (x+75, y+30), (x+40, y-55)), 1),
        (bl_color, ((x+75, y+30), (x+100, y), (x+70, y-70), (x+40, y-55)), 1),
        (bl_color, (x+17, y+32, 40, 45), 0)
        ) 
        '''
        the sequence of drawing
        the house is:
        walls(1 polygon), roof(1 polygon),
        2 walls' contours(each contour - 1 polygon),
        2 roof's contours(each contour - 1 polygon),
        hole(1 ellipse)
        '''
        k = 1
        for elem in house_parameters:
            if k == 1:
                pgd.polygon(screen, elem[0], (elem[1][0], elem[1][1], elem[1][2], elem[1][3], elem[1][4], elem[1][5]), elem[2])
            elif k == 2:
                pgd.polygon(screen, elem[0], (elem[1][0], elem[1][1], elem[1][2], elem[1][3], elem[1][4]), elem[2])
            elif k == 5:
                pgd.polygon(screen, elem[0], (elem[1][0], elem[1][1], elem[1][2]), elem[2])
            elif k == 7:
                pgd.ellipse(screen, elem[0], elem[1], elem[2])
            else:
                pgd.polygon(screen, elem[0], (elem[1][0], elem[1][1], elem[1][2], elem[1][3]), elem[2])
            k = k + 1
    house()
    def chain():
        chains = (
        (x+10, y+70, 25, 10),
        (x+5, y+70, 15, 20),
        (x-5, y+80, 20, 15),
        (x-15, y+90, 25, 10),
        (x-20, y+93, 15, 15),
        (x-35, y+101, 25, 10),
        (x-45, y+105, 20, 10),
        (x-55, y+105, 15, 8),
        ) 
        '''
        the sequence of drawing
        the chain is:
        each link - one ellipse
        '''
        for elem in chains:
            pgd.ellipse(screen, chain_color, elem, 1)   
    chain()
    
        
main()


pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()
