from random import *
import turtle as t

t.shape('turtle')
t.speed(20)
for i in range (100):
    t.forward(randint(5, 40))
    t.left(randint(0, 359))


