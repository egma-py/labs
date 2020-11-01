import turtle

def circle(b):
    for i in range(15):
        turtle.forward(b)
        turtle.right(360 / 30)
    turtle.forward(b)

turtle.shape('turtle')
turtle.left(90)
for i in range(5):
    circle(10)
    circle(2)
