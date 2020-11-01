import turtle
import math

def figure(n, a):
    for i in range(n):
        turtle.forward(a)
        turtle.left(360 / n)
        

turtle.shape('turtle')
turtle.speed(4)
n = 3
step = 10
a = 20
for i in range(10):
    turtle.left(180 - (180 * (n - 2)) / (2 * n))
    figure(n, a)
    turtle.penup()
    turtle.right(180 - (180 * (n - 2)) / (2 * n))
    turtle.forward(step)
    turtle.pendown()
    a = 2 * (a / (2 * math.sin(math.pi / n)) + step) * math.sin(math.pi / (n + 1)) 
    n += 1