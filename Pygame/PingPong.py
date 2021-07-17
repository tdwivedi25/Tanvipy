# Setup
import pygame
pygame.init()
screen = pygame.display.set_mode([1000,600])
pygame.display.set_caption("Smiley Pong")
keepGoing = True
pic = pygame.image.load(r"C:\Users\denali\PycharmProjects\Tanvipy\Pygame\CrazySmile.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0,0,0)
WHITE = (255,255,255)
timer = pygame.time.Clock()
speedx = 5
speedy = 5
paddlew = 200
paddleh = 25
paddlex = 300
paddley = 550
picw = 100
pich = 100
points = 0
lives = 5
font = pygame.font.SysFont("Impact", 30)
# Game loop
while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        if event.type == pygame.KEYDOWN:# F1= new game
            if event.key== pygame.K_F1:
             points=0
             lives=5
             speedx=5
             speedy=5
             picx=0
             picy=0
    picx += speedx
    picy += speedy

    #if picx <= 0 or picx + pic.get_width() >= 800:# make sure the smiley doesn't go off the screen
    #        speedx = -speedx
    if picx <= 0 or picx >= 700:# increasing the x speed by multiplying it by 1.1 only when users points increase
        speedx = -speedx * 1.1
    if picy <= 0:# increasing the y speed only when the users points increase
        speedy = -speedy * 1.1
    if picy >= 500:# slow down the speed if the user is losing lives
        lives -= 1
        speedy = -5
        speedx = 5
        picy = 499
    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))
# Draw paddle
    paddlex = pygame.mouse.get_pos()[0]
    paddlex -= paddlew/2
    pygame.draw.rect(screen, WHITE, (paddlex, paddley, paddlew, paddleh))
# Check for paddle bounce
    if picy + pich >= paddley and picy + pich <= paddley + paddleh and speedy > 0:# make sure the ball touches the paddle's x coordinate
        if picx + picw / 2 >= paddlex and picx + picw / 2 <= paddlex + paddlew:# make sure the ball touches the paddle's y coordinate
            points += 1
            speedy = -speedy
# Draw text on screen
    draw_string = "Lives: " + str(lives) + " Points: " + str(points)
    if lives<1:
            speedx=speedy=0
            draw_string="Game Over. Your score was: "+ str(points)
            draw_string += ". Press F1 to try again."

    text = font.render(draw_string, True, WHITE)
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx # centering the text
    text_rect.y = 10
    screen.blit(text, text_rect)
    pygame.display.update()
    timer.tick(60)
pygame.quit() # Exit
