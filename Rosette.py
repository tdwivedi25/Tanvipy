import turtle
t = turtle.Pen()
for x in range(10):
 colors = ["red","yellow","black","blue"]
 t.pencolor(colors[x%4])
 t.circle(20)
 t.left(60)