import turtle
t = turtle.Pen()
turtle.bgcolor("grey")
# Ask the user for the number of circles in their rosette, default to 6
number_of_circles = int(turtle.numinput("Number of circles",
"How many circles in your rosette?", 6))
for x in range(number_of_circles):
 colors = ["blue","red","orange","black","yellow","pink"]
 t.pencolor(colors[x%6])
 t.circle(100)
 t.left(360/number_of_circles)
