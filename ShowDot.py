import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
GREEN = (255,0,0) # RGB color triplet for GREEN
YELLOW = (255,255,0)
radius = 50
while keep_going:
# for x in range(100):
     pygame.draw.circle(screen, (255,0,0), (90, 70), radius)
     pygame.draw.circle(screen, (255,255,0), (190, 170), radius)

     '''for event in pygame.event.get():
         #print("event is: ",pygame.event.get(event))
         if event.type == pygame.QUIT:
            pygame.display.update()
           #pygame.quit()'''
#pygame
