import turtle
t = turtle.Pen()
# Ask the user for the number of sides or circles, default to 6
number = int(turtle.numinput("Number of sides or circles",
"How many sides or circles in your shape?", 6))
# Ask the user whether they want a polygon or rosette
shape = turtle.textinput("Which shape do you want?",
"Enter 'p' for polygon or 'r' for rosette:")
for x in range(number):
 if shape == 'r': # User selected rosette
  t.circle(100)
  t.left(40)
else: # Default to polygon
    for x in range (100):
     t.forward (x)
     t.left(91)