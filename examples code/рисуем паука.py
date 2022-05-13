import turtle

a = int(input())  # количество лап паука
turtle.shape('turtle')
for i in range(a):
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(360 / a)
input()
