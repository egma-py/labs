import pygame
import pygame.draw as pgd
from math import sqrt
from random import randint

pygame.init()
pygame.font.init()

FPS = 60
size = (567, 496)
screen = pygame.display.set_mode(size)

BLUE = (0, 191, 255)
PINK = (255, 20, 147)
PURPLE = (128, 0, 128)
BACKGROUND = (218, 165, 32)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND_1 = (220, 20, 60)
BACKGROUND_2 = (0, 128, 0)
COLORS = [BLUE, PINK, PURPLE, BACKGROUND, BLACK, WHITE, BACKGROUND_2, BACKGROUND_1, BACKGROUND_2]

#font to write a text on screen
font = pygame.font.Font(None, 36)
font_1 = pygame.font.Font(None, 30)
#max_x is the maximum velocity of a ball
max_v = 3
max_r = 20

#info about each ball contains in lists
def new_figs(n, m):
    global x, y, r, v_x, v_y, color
    x = []
    y = []
    r = []
    v_x = [] 
    v_y = []
    color = []  
    for i in range(n):
        x.append(randint(max_r, size[0]-max_r))
        y.append(randint(max_r, size[1]-max_r))
        r.append(randint(10, max_r))
        v_x.append(randint(-max_v, max_v))
        v_y.append(randint(-max_v, max_v))
        color.append(COLORS[randint(0, 2)])
    if m != 3:
        for i in range(n):
            pgd.circle(screen, color[i], (x[i], y[i]), r[i])
    else:
        for i in range(n):
            pgd.polygon(screen, color[i], [(x[i], y[i]),
                                           (x[i]+r[i], y[i]),
                                           (x[i]+r[i], y[i]+r[i]),
                                           (x[i], y[i]+r[i])])

#it is useful for drawing the motion of each ball
def draw_fig(new_x, new_y, r, color, m):
    if m != 3:
        pgd.circle(screen, color, (new_x, new_y), r)
    else:
        pgd.polygon(screen, color, [(new_x, new_y),
                                    (new_x+r, new_y),
                                    (new_x+r, new_y+r),
                                    (new_x, new_y+r)])


screen.fill(BACKGROUND)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
points = 0
FPS_counter = 0
time = randint(300, 500)
amount_of_figs = randint(1, 3)
batch_points = 0
batch_errors = 0
errors = 0
combos = 0
mode = randint(1, 3)
points_1 = font_1.render('+1', True, BLACK)
points_2 = font_1.render('+2', True, BLACK)
points_4 = font_1.render('+4', True, BLACK)
points_0 = font_1.render('+0', True, BLACK)
points_wait_time = 300
a = randint(7, 8) #define where is a green half of the screen


while not finished:
    clock.tick(FPS)
    if mode != 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(amount_of_figs): #counting points
                    if (sqrt((x[i]-event.pos[0])**2 + 
                        (y[i]-event.pos[1])**2))<= r[i]: #is ball found or not
                        points += 1
                        batch_points += 1
                        x[i], y[i], r[i], v_x[i], v_y[i]=0, 0, 0, 0, 0 #hide fig
                        screen.blit(points_1, (5, 5))
                        pygame.display.update()
                        pygame.time.wait(points_wait_time)
                    if batch_points == amount_of_figs: #if all balls are found
                        batch_points = 0
                        combos += 1
                        points += 2
                        screen.blit(points_2, (5, 25))
                        pygame.display.update()
                        pygame.time.wait(points_wait_time)
                        FPS_counter = time
                        break
        if FPS_counter % time != 0: #if time isn't over, continue the motion
            for i in range(amount_of_figs): #new coordinates
                x[i] = x[i] + v_x[i]
                y[i] = y[i] + v_y[i]
            for i in range(amount_of_figs): #if a ball is on border of screen
                if x[i]<0 or x[i]>size[0]:
                    x[i] = x[i] - v_x[i]
                    v_x[i] = randint(-max_v, max_v) #new velocity x
                    if v_x[i] == 0:
                        v_x[i] = 1
                if y[i]<0 or y[i]>size[1]:
                    y[i] = y[i] - v_y[i]
                    v_y[i] = randint(-max_v, max_v) #new velocity y
                    if v_y[i] == 0:
                        v_y[i] = 1
            for i in range(amount_of_figs): #drawing motion
                draw_fig(x[i], y[i], r[i], color[i], mode)
                pygame.display.update()
            screen.fill(BACKGROUND)
        else: #if time is over, drawing new balls
            new_figs(amount_of_figs, mode)
            pygame.display.update()
            screen.fill(BACKGROUND)
        if FPS_counter == time: #when time is over, reset FPS counter
            FPS_counter = 0
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(amount_of_figs): #counting points
                    d_x = event.pos[0] - x[i]
                    d_y = event.pos[1] - y[i]
                    if a == 7:    
                        if d_x>=0 and d_y>=0 and d_x<=r[i] and d_y<=r[i] and event.pos[1]<=(size[1]//2): #if square isn't found
                            points += 0
                            errors += 1
                            batch_errors += 1
                            batch_points += 1
                            x[i], y[i], r[i], v_x[i], v_y[i]=0, 0, 0, 0, 0 #hide fig
                            screen.blit(points_0, (5, 5))
                            pygame.display.update()
                            pygame.time.wait(points_wait_time)
                        elif d_x>=0 and d_y>=0 and d_x<=r[i] and d_y<=r[i] and event.pos[1]>(size[1]//2): #if square is found
                            points += 2
                            batch_points += 1
                            x[i], y[i], r[i], v_x[i], v_y[i]=0, 0, 0, 0, 0 #hide fig
                            screen.blit(points_2, (5, 5))
                            pygame.display.update()
                            pygame.time.wait(points_wait_time)
                    else:
                        if d_x>=0 and d_y>=0 and d_x<=r[i] and d_y<=r[i] and event.pos[1]>(size[1]//2): #if square isn't found
                            points += 0
                            errors += 1
                            batch_errors += 1
                            batch_points += 1
                            x[i], y[i], r[i], v_x[i], v_y[i]=0, 0, 0, 0, 0 #hide fig
                            screen.blit(points_0, (5, 5))
                            pygame.display.update()
                            pygame.time.wait(points_wait_time)
                        elif d_x>=0 and d_y>=0 and d_x<=r[i] and d_y<=r[i] and event.pos[1]<=(size[1]//2): #if square is found
                            points += 2
                            batch_points += 1
                            x[i], y[i], r[i], v_x[i], v_y[i]=0, 0, 0, 0, 0 #hide fig
                            screen.blit(points_2, (5, 5))                        
                            pygame.time.wait(points_wait_time)
                            pygame.display.update()
                    if batch_points==amount_of_figs and batch_errors==0: #if all squares are found and no errors
                        batch_points = 0
                        batch_errors = 0
                        combos += 1
                        points += 4
                        screen.blit(points_4, (5, 25))
                        pygame.display.update()                        
                        pygame.time.wait(points_wait_time)
                        FPS_counter = time
                        break
                    if batch_points==amount_of_figs: #if all squares are found
                        batch_points = 0
                        batch_errors = 0
                        FPS_counter = time
                        break
        if FPS_counter % time != 0: #if time isn't over, continue the motion
            for i in range(amount_of_figs): #new coordinates
                x[i] = x[i] + v_x[i]
                y[i] = y[i] + v_y[i]
            for i in range(amount_of_figs): #if a square is on border of screen
                if x[i]<0 or x[i]>size[0]:
                    x[i] = x[i] - v_x[i]
                    v_x[i] = randint(-max_v, max_v) #new velocity y
                    if v_x[i] == 0:
                        v_x[i] = 1
                if y[i]<0 or y[i]>size[1]:
                    if y[i]<0:
                        y[i] = size[1]
                    else:
                        y[i] = 0                    
            for i in range(amount_of_figs): #drawing motion
                draw_fig(x[i], y[i], r[i], color[i], mode)
                pygame.display.update()
            pgd.rect(screen, COLORS[a], (0, 0, size[0], size[1]//2)) #drawing halfs
            pgd.rect(screen, COLORS[abs(1-a)], (0, size[1]//2, size[0], size[1]))
        else: #if time is over, drawing new figs
            new_figs(amount_of_figs, mode)
            pygame.display.update()
        if FPS_counter == time: #when time is over, reset FPS counter
            FPS_counter = 0
            batch_errors = 0
            batch_points = 0
    FPS_counter += 1
    if FPS_counter == 1:
        mode = randint(1, 3) #new mode
        time = randint(300, 500) #new time of motion
        a = randint(7, 8) #new order of rects
    
    
# drawing results
screen.fill(BACKGROUND)
result_1 = font.render(' Your points: '+str(points)+' ', True, WHITE, BLACK)
result_2 = font.render(' Errors: '+str(errors)+' ', True, WHITE, BLACK)
result_3 = font.render(' Combos: '+str(combos)+' ', True, WHITE, BLACK)
screen.blit(result_1, (size[0]//2-100, size[1]//2-40))
screen.blit(result_2, (size[0]//2-100, size[1]//2))
screen.blit(result_3, (size[0]//2-100, size[1]//2+40))
pygame.display.update()
pygame.time.wait(550)
pygame.quit()