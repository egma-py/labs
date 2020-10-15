import pygame
import pygame.draw as pgd
from math import sqrt
from random import randint

pygame.init()
pygame.font.init()

FPS = 30
size = (400, 400)
screen = pygame.display.set_mode(size)

RED = (220, 20, 60)
GREEN = (0, 128, 0)
BLUE = (0, 191, 255)
PINK = (255, 20, 147)
PURPLE = (128, 0, 128)
BACKGROUND = (218, 165, 32)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, GREEN, BLUE, PINK, PURPLE, BACKGROUND, BLACK, WHITE]

#font to write a text on screen
font = pygame.font.Font(None, 36)
#max_x is the maximum velocity of a ball
max_v = 3

#info about each ball contains in lists
def new_balls(n):
    global x, y, r, v_x, v_y, color
    x = []
    y = []
    r = []
    v_x = [] 
    v_y = []
    color = []  
    for i in range(n):
        x.append(randint(20, 380))
        y.append(randint(20, 380))
        r.append(randint(10, 20))
        v_x.append(randint(-max_v, max_v))
        v_y.append(randint(-max_v, max_v))
        color.append(COLORS[randint(0, 4)])
    for i in range(n):
        pgd.circle(screen, color[i], (x[i], y[i]), r[i])

#it is useful for drawing the motion of each ball
def draw_ball(new_x, new_y, r, color):
    pgd.circle(screen, color, (new_x, new_y), r)


screen.fill(BACKGROUND)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
points = 0
FPS_counter = 0
time = randint(100, 500)
amount_of_balls=5
batch_points = 0


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(amount_of_balls): #counting points
                if (sqrt((x[i]-event.pos[0])**2 + 
                    (y[i]-event.pos[1])**2))<= r[i]: #is ball found or not
                    points += 1
                    batch_points += 1
                    color[i] = BACKGROUND #finded ball is hidden then
                if batch_points == amount_of_balls: #if all balls are found
                    batch_points = 0
                    FPS_counter = time
                    break
    if FPS_counter % time != 0: #if time isn't over, continue the motion
        for i in range(amount_of_balls): #changing velocity randomly
            x[i] = x[i] + v_x[i]
            y[i] = y[i] + v_y[i]
        for i in range(amount_of_balls): #if a ball is on border of screen
            if x[i]<0 or x[i]>400:
                x[i] = x[i] - v_x[i]
                v_x[i] = randint(-max_v, max_v)
                if v_x[i] == 0:
                    v_x[i] = 1
            if y[i]<0 or y[i]>400:
                y[i] = y[i] - v_y[i]
                v_y[i] = randint(-max_v, max_v)
                if v_y[i] == 0:
                    v_y[i] = 1
        for i in range(amount_of_balls): #drawing motion
            draw_ball(x[i], y[i], r[i], color[i])
            pygame.display.update()
        screen.fill(BACKGROUND)
    else: #if time is over, drawing new balls
        new_balls(amount_of_balls)
        pygame.display.update()
        screen.fill(BACKGROUND)
    if FPS_counter == time: #when time is over, reset FPS counter
        FPS_counter = 0
    FPS_counter += 1
    time = randint(100, 500) #new time of motion
   
    
# drawing results
result = font.render(' Your points: '+str(points)+' ', True, WHITE, BLACK)
screen.blit(result, (100, 200))
pygame.display.update()
pygame.time.wait(550)
pygame.quit()