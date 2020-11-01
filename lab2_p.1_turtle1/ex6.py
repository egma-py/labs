import turtle

turtle.shape('turtle')
r = 200
n = 15
for i in range(n):
    turtle.forward(r)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(r)
    turtle.right(180)
    turtle.left(360/n)