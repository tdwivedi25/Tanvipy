import turtle
t = turtle.Pen()
turtle.bgcolor("white")
colors = [ "red","violet","blue","green"]
for x in range(200):
 t.pencolor(colors[x%4])
 t.forward(x%20)
 t.left(10)