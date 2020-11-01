import turtle 

def circle_left():
    for i in range(30):
        turtle.forward(5)
        turtle.left(360 / 30)
        
        
def circle_right():
    for i in range(30):
        turtle.forward(5)
        turtle.right(360 / 30)


turtle.shape('turtle')
for i in range(3):
    circle_left()
    circle_right()
    turtle.left(120)


