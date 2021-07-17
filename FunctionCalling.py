from Smiley import *
for n in range(200):

    x = random.randrange(-turtle.window_width()//2,
    turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,
    turtle.window_height()//2)
    draw_smiley(x,y)
