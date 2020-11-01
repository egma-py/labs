import turtle

turtle.shape('turtle')
a = 5
for i in range(20):
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    a += 5