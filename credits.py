
def creditScreen():  
  import pygame 
  #from pygame import font 
  SCREEN_WIDTH= 640
  SCREEN_HEIGHT= 480
  pygame.init()
  pygame.font.init()
  screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
  
  
  running=True 
  bgd=pygame.image.load('credits screen.png')
  bgd=pygame.transform.scale(bgd, (SCREEN_WIDTH,SCREEN_HEIGHT))
  
  pygame.init()
  
  #screen=pygame.display.set_mode((800,600))
  
  font = pygame.font.SysFont("comicsans", 50)
  creditsText = font.render("Credits", False, (255, 255, 255))
  running=True
  
  while running:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running=False
      #screen.fill((255,0,0))
      screen.blit(bgd,(0,0))
     
      #screen.blit(score_font,(50,200))
      screen.blit(creditsText, ((SCREEN_WIDTH - creditsText.get_width()) // 2, 50))
      pygame.display.update()


#creditScreen()