import turtle
t = turtle.Pen()
colors = ["red", "yellow", "blue", "green"]
for x in range(4):
 t.pencolor(colors[x+1])
 t.forward(x)
 t.left(91)
