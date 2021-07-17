import turtle
for i in range(0,11):
    if i%7==0:
       print(i,'is divisible by 7')
       colors = ['red', 'yellow', 'violet', 'white', 'pink', 'black','cyan']
       turtle.penup()
       turtle.setpos(90, 5)
       turtle.pendown()
       for x in range(20):
        turtle.bgcolor("blue")
        sides = 7
        turtle.pencolor(colors[x % sides])
        turtle.forward(x * 3 / sides + x)
        turtle.left(360 / sides + 1)
        turtle.width(x * sides / 200)
    elif i%5==0:
        print(i,'is divisible by 5')
        colors = ['red', 'yellow','blue','black']
        turtle.penup()
        turtle.setpos(-63, -5)
        turtle.pendown()
        for x in range(20):
            #import turtle
           #import random
            turtle.bgcolor('cyan')
            sides = 4
            turtle.pencolor(colors[x % sides])
            turtle.forward(x * 3 / sides + x)
            turtle.left(360 / sides + 1)
            turtle.width(x * sides / 200)
    else:
        print(i,'is divisible by some other number')
        colors=['red','yellow','blue','black','purple','pink']
        turtle.penup()
        turtle.setpos(63, 5)
        turtle.pendown()
        for x in range(20):
            turtle.bgcolor('grey')

           #random.randint(turtle.setpos(-63, -5))
            sides = 6
            turtle.pencolor(colors[x % sides])
            turtle.forward(x * 3 / sides + x)
            turtle.left(360 / sides + 1)
            turtle.width(x * sides / 200)
