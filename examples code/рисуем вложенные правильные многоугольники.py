import turtle
import math

turtle.shape('turtle')
n = 3
r = 10  #задаем радиус первой окружности


def more_agles(n, m):  #опеределяем функцию, рисующую многоугольник
    q = 360 / n
    while n > 0:

        turtle.left(q)
        turtle.forward(m)
        n -= 1


while n < 13:
    m = 2 * r * math.sin(
        math.pi / n)  #считаем размер стороны многоугольника (a=2Rsin (360/2n))
    x = (180 - 360 / n) / 2
    turtle.left(x)

    more_agles(n, m)
    turtle.right(x)
    turtle.penup()
    turtle.forward(10)  # задаем расстояние м/у окружностями

    turtle.pendown()
    n += 1
    r += 10  #раз расстояние м/у окружностями 10, увеличиваем радиус на 10

