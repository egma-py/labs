#рефакторинг проекта норайра геворгяна
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
    sky(screen, BLUE)
    grass(screen, GREEN)
    fences = (
    (75, 25, 700, 300),
    (50, 100, 225, 300),
    (185, 150, 500, 325),
    (-50, 200, 175, 350),
    )
    for elem in fences:
        fence(screen, BLACK, FENCE_COLOR, elem[0], elem[1], elem[2], elem[3])
    dogs = (
    (-0.75, 400, 300),
    (-0.9, 200, 450),
    (1, 50, 300),
    )
    for elem in dogs:
        dog(screen, GRAY, DARK_GRAY, elem[0], elem[1], elem[2])
    dog_house(screen, WALL_COLOR, ROOF_COLOR, BLACK)
    dog(screen, GRAY, DARK_GRAY, 2, 250, 450)


def grass(screen, color):
    pgd.rect(screen, color, (0, 250, 600, 450))


def fence(screen, line_color, fence_color, x1, y1, x2, y2):
    '''
    (x1, y1) is the pair of coordinates of left top corner
    (x2, y2) is the pair of coordinates of right bottom corner
    So (x2 - x1) is height and (y2 - y1) is width
    '''
    fence_parameters = (x1, y1, x2 - x1, y2 - y1)
    pgd.rect(screen, fence_color, fence_parameters)
    pgd.line(screen, line_color, (x1, y2), (x2, y2))
    N = 19
    h = (x2 - x1) / (N + 1)
    x = x1 + h
    for i in range(N):
        pgd.line(screen, line_color, (x, y1), (x, y2))
        x += h

def sky(screen, color):
    pgd.rect(screen, color, (0, 0, 600, 100))
    

def dog(screen, dog_color, box_color, n, x, y, wh_color=(255, 255, 255), bl_color=(0, 0, 0)):
    def body() :
        body_parameters = (
        (x+75*n-55*abs(n), y+25*abs(n), 110*abs(n), 60*abs(n)),
        (x+115*n-35*abs(n), y+18*abs(n), 70*abs(n), 40*abs(n)),
        (x+65*n-15*abs(n), y+45*abs(n), 30*abs(n), 70*abs(n)),
        (x+25*n-15*abs(n), y+35*abs(n), 30*abs(n), 70*abs(n)),
        (x+118*n-8*abs(n), y+45*abs(n), 16*abs(n), 50*abs(n)),
        (x+158*n-8*abs(n), y+70*abs(n), 16*abs(n), 40*abs(n)),
        (x+55*n-15*abs(n), y+110*abs(n), 30*abs(n), 15*abs(n)),
        (x+15*n-15*abs(n), y+100*abs(n), 30*abs(n), 15*abs(n)),
        (x+110*n-10*abs(n), y+90*abs(n), 20*abs(n), 10*abs(n)),
        (x+150*n-10*abs(n), y+105*abs(n), 20*abs(n), 10*abs(n)),
        (x+int(100*n), y+int(35*abs(n)), int(20*abs(n)), 0),
        (x+int(145*n), y+int(60*abs(n)), int(20*abs(n)), 0),
        )
        '''
        the sequence of drawing
        the body is:
        chest, back, 4 legs, 4 feet , 2 thighs 
        each part except thighs is drawn with the only ellipse
        thighs are drawn with circles
        '''
        k = 1
        for elem in body_parameters:
            if k > 10:
                pgd.circle(screen, dog_color, (elem[0], elem[1]), elem[2])
            else:
                pgd.ellipse(screen, dog_color, elem)
            k = k + 1
    body()
    def head():
        s = 56
        head_parameters = (
        (dog_color, (x+s//2*n-s//2*abs(n), y, s*abs(n), s*abs(n)), (0, 0)),
        (box_color, (x+s//2*n-s//2*abs(n), y, s*abs(n), s*abs(n)), (2, 2)),
        (dog_color, (x-s//16*abs(n), y, s//8*abs(n), s//4*abs(n)), (0, 0)),
        (box_color, (x-s//16*abs(n), y, s//8*abs(n), s//4*abs(n)), (2, 2)),
        (dog_color, (x+s*n-s//16*abs(n), y, s//8*abs(n), s//4*abs(n)), (0, 0)),
        (box_color, (x+s*n-s//16*abs(n), y, s//8*abs(n), s//4*abs(n)), (2, 2)),
        (wh_color, (x+(s//8+s//8)*n-s//8*abs(n), y + s//4*abs(n), s//4*abs(n), s//8*abs(n)), (0, 0)),
        (box_color, (x+(s//8+s//8)*n-s//8*abs(n), y + s//4*abs(n), s//4*abs(n), s//8*abs(n)), (1, 1)),
        (bl_color, (x+int((s//4)*n), y+int((5*s//16)*abs(n)), int((s//16)*abs(n)), 0), (0, 0)),
        (wh_color, (x+(5*s//8+s//8)*n-s//8*abs(n), y + s//4*abs(n), s//4*abs(n), s//8*abs(n)), (0, 0)),
        (box_color, (x+(5*s//8+s//8)*n-s//8*abs(n), y + s//4*abs(n), s//4*abs(n), s//8*abs(n)), (1, 1)),
        (bl_color, (x+int((3*s//4)*n), y+int((5*s//16)*abs(n)), int((s//16)*abs(n)), 0), (0, 0)),
        (bl_color, (x+(s//4+0.75*s//3)*n-0.75*s//3*abs(n), y+3*s//4*abs(n), 1.5*s//3*abs(n), s//3*abs(n)), (m.pi//16, m.pi)),
        (wh_color, [(x+s//3*n,y+4*s//5*abs(n)),(x+s//3*n,y+7*s//10*abs(n)),(x+7*s//18*n, y+15*s//20*abs(n))],(0, 0)),
        (wh_color, [(x+(s-s//3)*n,y+4*s//5*abs(n)),(x+(s-s//3)*n,y+7*s//10*abs(n)),(x+(s-7*s//18)*n,y+15*s//20*abs(n))], (0, 0)),
        )
        '''
        the sequence of drawing
        the head is:
        head(2 rects), 2 ears(each ear - 2 ellipses), 2 eyes(each eye - 2 ellipses and 1 circle), 
        mouth(1 arc), teeth(each tooth - 1 polygon)
        '''
        k = 1
        for elem in head_parameters:
            if k < 3:
                pgd.rect(screen, elem[0], elem[1], elem[2][0])
            elif k == 9 or k == 12:
                pgd.circle(screen, elem[0], (elem[1][0], elem[1][1]), elem[1][2], elem[2][0])
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
        k = 1
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
