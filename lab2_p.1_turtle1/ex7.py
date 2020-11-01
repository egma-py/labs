import turtle

def circle(b, a):
    phi = int(360 / 25)
    for i in range(int(25 * a / 360)):
        turtle.forward(b)
        turtle.left(phi)       
    

turtle.shape('turtle')
n = 21
b = 1
for i in range(n):
    circle(b, 120)
    b += 1
    
