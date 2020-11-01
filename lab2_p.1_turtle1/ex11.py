import turtle

def circle_left(b):
    for i in range(30):
        turtle.forward(b)
        turtle.left(360 / 30)
        
        
def circle_right(b):
    for i in range(30):
        turtle.forward(b)
        turtle.right(360 / 30)


turtle.shape('turtle')
turtle.left(90)
turtle.speed(50)
b = 10
for i in range(10):
    circle_left(b)
    circle_right(b)
    b += 1
    