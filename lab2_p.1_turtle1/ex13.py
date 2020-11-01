import turtle as t
import math

def circle_blue(b):
    for i in range(30):
        t.forward(b)
        t.left(360 / 30)
    
    
def circle_y(b):
    for i in range(30):
        t.forward(b)
        t.left(360 / 30)
        
        
def half_circle(b, width):
    for i in range(30):
        t.forward(b)
        t.left(360 / 30)
    

t.shape('turtle')
t.width(1)
b = 50
t.begin_fill()
t.fillcolor('yellow')
t.filling()
t.circle(b)
t.end_fill()
t.penup()
t.left(90)
t.forward(6 * b / 4)
t.left(90)
t.forward(1.5 * b / 7)
t.right(90)
t.begin_fill()
t.fillcolor('blue')
t.filling()
t.circle(b / 10)
t.end_fill()
t.penup()
t.right(90)
t.forward(3 * b / 7)
t.right(90)
t.begin_fill()
t.fillcolor('blue')
t.filling()
t.circle(b / 10)
t.end_fill()
t.right(90)
t.forward(1.5 * b / 7)
t.left(90)
t.forward(b / 3)
t.pendown()
t.width(4)
t.forward(1 * b / 3)
t.penup()
t.width(1)
t.forward(b / 18)
t.right(90)
t.forward(b / 2)
t.width(4)
t.color('red')
t.pendown()
t.left(90)
t.circle(b / 2, 180)