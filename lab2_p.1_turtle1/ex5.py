import turtle

def square(a):
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)
        

turtle.shape('turtle')
a = 20
for i in range(10):
    square(a) 
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.pendown()
    a += 20
    

