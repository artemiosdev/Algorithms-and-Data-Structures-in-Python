import turtle
turtle.shape('turtle')
turtle.speed(3)
turtle.penup()
turtle.setx(-450)
turtle.pendown()

for _ in range(4):
    # Повернуть черепашку под углом to_angle к вертикали (0 — наверх, 90 — направо);
    turtle.setheading(90)
    turtle.circle(-100, 180)
    turtle.circle(-20, 180)
turtle.circle(-100, 180)
turtle.done()
