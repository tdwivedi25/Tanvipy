import random
import turtle
answer = input("Do you want a happy face or sad face? ")
t = turtle.Pen()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")
def draw_smiley(x,y):
 if answer == "sad":
  t.penup()
  t.setpos(x,y)
  t.pendown()
# Head
  t.pencolor("red")
  t.fillcolor("red")
  t.begin_fill()
  t.circle(50)
  t.end_fill()
 # Left eye
  t.setpos(x-15, y+60)
  t.fillcolor("black")
  t.begin_fill()
  t.circle(10)
  t.end_fill()
# Right eye
  t.setpos(x+15, y+60)
  t.begin_fill()
  t.circle(10)
  t.end_fill()
# Mouth
  t.setpos(x-30, y+20)
  t.pencolor("black")
  t.width(10)
# t.goto(x-10, y+20)
  t.setpos(x-25, y+40)
  t.goto(x+25, y+40)
  t.goto(x+30, y+20)
  t.width(1)
 if answer == "happy":
  t.penup()
  t.setpos(x,y)
  t.pendown()
# Head
  t.pencolor("yellow")
  t.fillcolor("yellow")
  t.begin_fill()
  t.circle(50)
  t.end_fill()
 # Left eye
  t.setpos(x-15, y+60)
  t.fillcolor("blue")
  t.begin_fill()
  t.circle(10)
  t.end_fill()
# Right eye
  t.setpos(x+15, y+60)
  t.begin_fill()
  t.circle(10)
  t.end_fill()
# Mouth
  t.setpos(x-25, y+40)
  t.pencolor("red")
  t.width(10)
# t.goto(x-10, y+20)
  t.setpos(x-10, y+20)
  t.goto(x+10, y+20)
  t.goto(x+25, y+40)
  t.width(1)
for n in range(200):
    x = random.randrange(-turtle.window_width()//2,
    turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,
    turtle.window_height()//2)
    draw_smiley(x,y)
