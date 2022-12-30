### Import Pygame
import pygame

### Initialize
pygame.init()


SCREEN_WIDTH= 640
SCREEN_HEIGHT= 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



zombieBoySprite=[]
for i in range(10):
    j=i+1
    zombieBoySprite.append(pygame.image.load(f"zombie/male/Walk ({j}).png"))



#zombieBoySprite = [pygame.image.load("zombie/male/Attack (1).png"), #pygame.image.load("zombie/male/Attack (2).png"), pygame.image.load("zombie/male/Attack #(3).png")]
               
#I think we're supposed to load the images into main
               #I am making a function for it so we can call it in main
        #oh ok
value=0               
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  if value >= len(zombieBoySprite):
        value = 0
  Enemy=zombieBoySprite[value]
  enemy_rect=screen.blit(enemy,(enemyX,enemyY))

  value=value+1
  pygame.display.update()