# SpiralMyName.py - prints a colorful spiral of the user's name
import turtle # Set up turtle graphics
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]
# Ask the user's name using turtle's textinput pop-up window
your_name = turtle.textinput("Enter your name", "What is your name?")
sides = int(turtle.numinput("Number of sides",
"How many sides do you want (1-8)?", 4, 1, 8))
# Draw a spiral of the name on the screen, written 100 times
for x in range(50):
 t.pencolor(colors[x%4]) # Rotate through the four colors
 t.penup() # Don't draw the regular spiral lines
 t.forward(x*4) # Just move the turtle on the screen
 t.pendown() # Write the user's name, bigger each time
 t.write(your_name, font = ("Aerial", int( (x + 20) / 4)) )
 t.left(60) # Turn left, just as in our other spirals
