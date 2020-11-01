from random import randint
import turtle as t


number_of_molecules = 60
turtle_size = 0.4
steps_of_time_number = 10000
dt = 1
border = 105
maxspeed = 5
t.penup()
t.speed(2000)
t.width(4)
t.goto(-border, -border)
t.pendown()
t.forward(border*2); t.left(90)
t.forward(border*2); t.left(90)
t.forward(border*2); t.left(90)
t.forward(border*2); t.left(90)
t.penup()
t.goto(500,500)


pool = [t.Turtle(shape='circle') for i in range(number_of_molecules)]
pool_xy = []
pool_vx_vy = []

for i in range(number_of_molecules):
    pool_xy.append([randint(-border+5, border-5), randint(-border+5, border-5)])
    
for i in range(number_of_molecules):
    pool_vx_vy.append([randint(-maxspeed, maxspeed), randint(-maxspeed, maxspeed) ])

k = 0    
for unit in pool:
    unit.penup()
    unit.turtlesize(turtle_size)
    unit.speed(((pool_vx_vy[k][0]**2 + pool_vx_vy[k][1]**2)**(1/2))*30)
    unit.goto(pool_xy[k][0], pool_xy[k][1])
    k += 1
  
k = 0
for i in range(steps_of_time_number):
    k = 0
    for unit in pool:
        if (pool_xy[k][0] + pool_vx_vy[k][0]*dt) > border-3 or (pool_xy[k][0] + pool_vx_vy[k][0]*dt) < -border+3:
            pool_vx_vy[k][0] = -pool_vx_vy[k][0]
            pool_xy[k][0] = pool_xy[k][0] + pool_vx_vy[k][0]*dt
            pool_xy[k][1] = pool_xy[k][1] + pool_vx_vy[k][1]*dt
            unit.goto(pool_xy[k][0], pool_xy[k][1])
        elif (pool_xy[k][1] + pool_vx_vy[k][1]*dt) > border-3 or (pool_xy[k][1] + pool_vx_vy[k][1]*dt) < -border+3:
            pool_vx_vy[k][1] = -pool_vx_vy[k][1] 
            pool_xy[k][0] = pool_xy[k][0] + pool_vx_vy[k][0]*dt
            pool_xy[k][1] = pool_xy[k][1] + pool_vx_vy[k][1]*dt
            unit.goto(pool_xy[k][0], pool_xy[k][1])                                 
        else:
            pool_xy[k][0] = pool_xy[k][0] + pool_vx_vy[k][0]*dt
            pool_xy[k][1] = pool_xy[k][1] + pool_vx_vy[k][1]*dt
            unit.goto(pool_xy[k][0], pool_xy[k][1])
        k += 1
