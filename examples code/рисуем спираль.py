import turtle

turtle.shape('turtle')
x = 0.5
for i in range(20):
    for j in range(30):
        turtle.forward(x)
        turtle.left(6)
    x += 0.5
#
## Есть и другое быстрое решение, нужно подключить модуль math
#
#from math import pi, sin, cos
#import turtle
#
#turtle.shape('turtle')
#for i in range(200):
#    t = i / 10 * pi
#    dx = t * cos(t)
#    dy = t * sin(t)
#    turtle.goto(dx, dy)
