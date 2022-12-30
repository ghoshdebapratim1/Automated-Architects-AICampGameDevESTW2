### Import Pygame
import pygame

### Initialize
pygame.init()

SCREEN_WIDTH= 640
SCREEN_HEIGHT= 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont("comicsans", 100)
font.render('GAMER OVER', False, (255, 0, 0))

running = True
while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
