import turtle

turtle.shape('turtle')
x = 15
for i in range(20):
    for j in range(30):
        turtle.forward(x)
        turtle.left(90)
        x += 5
