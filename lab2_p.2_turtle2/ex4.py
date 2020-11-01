import turtle as t

t.shape('circle')
t.width(4)
t.speed(1000)
t.forward(1000)
t.backward(1100)
t.forward(100)
t.width(1)
t.speed(2)
t.goto(1, 1)
x = 1
y = 1
vx = 5
vy = 25
ay = -2.5
dt = 0.15
number_of_timesteps = 20000
for i in range(number_of_timesteps):
    if (y + vy*dt + (ay*dt**2)/2) > 0:
        t.speed(((vx*vx+vy*vy)**(1/2))*30)
        t.goto(x, y)
        x = x + vx*dt
        y = y + vy*dt + (ay*dt**2)/2
        vy = vy + ay*dt
    else:
        vy = vy * (-1) * 0.85
        vx = vx * 0.85