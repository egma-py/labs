import turtle as t

def star(b, n):
    for i in range(n):
        t.forward(b)
        t.right(180 - (90 - (90 * n - 180) / n))

t.shape('arrow')
star(100, 5)
t.penup()
t.left(180)
t.forward(150)
t.pendown()
t.left(180)
star(100, 11)




