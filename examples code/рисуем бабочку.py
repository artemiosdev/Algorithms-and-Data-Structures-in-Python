import turtle

radius = 20
turtle.left(90)

for i in range(5):
  turtle.circle(radius)
  turtle.circle(-radius)
  radius += 10
