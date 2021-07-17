import pygame
import random
pygame.init()
screen=pygame.display.set_mode([1000,600])
pic=pygame.image.load(r'C:\Users\denali\PycharmProjects\Tanvipy\Pygame\CrazySmile.bmp')
BLACK=(0,0,0)
RED=(255,0,0)
keep_going=True
mousedown=False
font = pygame.font.SysFont("Impact", 35)
count_smileys=0
count_popped=0
clock=pygame.time.Clock()
sprite_list=pygame.sprite.Group()# List created to store the smiley sprites.Sprites are moving graphical objects on screen.
pygame.mixer.init()
pop=pygame.mixer.Sound(r'C:\Users\denali\PycharmProjects\Tanvipy\Pygame\Pop.wav')
blip=pygame.mixer.Sound(r'C:\Users\denali\PycharmProjects\Tanvipy\Pygame\blip.wav')

class Smiley(pygame.sprite.Sprite):
    pos=(0,0)
    xvel=1
    yvel=1
    scale=100
    def __init__(self, pos, xvel, yvel,):
        pygame.sprite.Sprite.__init__(self)
        self.image=pic
        self.scale=random.randint(10,100)
        self.image=pygame.transform.scale(self.image,(self.scale,self.scale))# takes the random scale and transforms it into an image
        self.rect=self.image.get_rect()
        self.pos=pos
        self.rect.x=pos[0]-self.scale/2 # create the smiley at the center where the user chooses
        self.rect.y=pos[1]-self.scale/2
        self.xvel=xvel
        self.yvel=yvel
    def update(self):
        self.rect.x+=self.xvel
        self.rect.y+=self.yvel
        if self.rect.x<=0 or self.rect.x>screen.get_width()-self.scale:#collision detection
            self.rect.x=-self.rect.x
        if self.rect.y<=0 or self.rect.y>screen.get_width()-self.scale:
            self.rect.y=-self.rect.y

while keep_going: # Game loop
 for event in pygame.event.get():
    if event.type==pygame.QUIT:
        keep_going=False
    if event.type==pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
          mousedown=True
          blip.play()
          count_smileys+=1

        elif pygame.mouse.get_pressed()[2]:
         pos=pygame.mouse.get_pos()
         clicked_smiley=[s for s in sprite_list if s.rect.collidepoint(pos)]
         sprite_list.remove(clicked_smiley)
         if len(clicked_smiley)>0:
             pop.play()
             count_popped += len(clicked_smiley)
    if event.type==pygame.MOUSEBUTTONUP:
        mousedown=False
    draw_string = "Bubbles created: " + str(count_smileys)
    draw_string += ". Bubbles popped: " + str(count_popped)
    if count_smileys>0:
        draw_string+=".Percent: "
        draw_string+=str(round(count_popped/count_smileys*100,1))
        draw_string+="%"
    text = font.render(draw_string, True, RED)
    text_rect=text.get_rect()
    text_rect.centerx=screen.get_rect().centerx
    text_rect.y=10
    screen.blit(text, text_rect)
    pygame.display.update()
    if mousedown:
        speedx=random.randint(-5,5)
        speedy=random.randint(-5,5)
        newsmiley=Smiley(pygame.mouse.get_pos(),speedx, speedy)
        sprite_list.add(newsmiley)# new smiley which is drawn will be added to the list called"sprite_list".
    screen.fill(BLACK)
    sprite_list.update()# calling the update function writen above
    sprite_list.draw(screen)
    clock.tick(60)

pygame.quit()




