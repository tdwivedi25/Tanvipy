import random, turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("grey")
color = ["red","blue","white","yellow","black","orange","purple","pink"]
#t.pencolor(random.choice(color))
for n in range(50):
    t.pencolor(random.choice(color))
    size =random.randint(10,40)
    x = random.randrange(-turtle.window_width()//2,
                         turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,
                         turtle.window_height()//2)
    print(x,y)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
            t.forward(m*2)
            t.right(89)

    print(-x, y)
    t.penup()
    t.setpos(-x, y)
    t.pendown()
    for m in range(size):
        t.forward(m * 2)
        t.right(89)
    print(x, -y)
    t.penup()
    t.setpos(x, -y)
    t.pendown()
    for m in range(size):
        t.forward(m * 2)
        t.right(59)
    print(x, -y)
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    for m in range(size):
        t.forward(m * 2)
        t.right(59)



