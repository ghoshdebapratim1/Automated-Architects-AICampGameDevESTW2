
def gameOver(scoreText):  
  import pygame 
  from pygame import mixer
  #from pygame import font 
  SCREEN_WIDTH= 640
  SCREEN_HEIGHT= 480
  pygame.init()
  pygame.font.init()
  mixer.init()
  mixer.music.load("videogame-death-sound-43894.mp3")
  mixer.music.play()
  screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
  
  
  running=True 
  bgd=pygame.image.load('gameover background.png')
  bgd=pygame.transform.scale(bgd, (SCREEN_WIDTH,SCREEN_HEIGHT))
  
  pygame.init()
  
  #screen=pygame.display.set_mode((800,600))
  
  font = pygame.font.SysFont("comicsans", 50)
  running=True
  
  while running:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running=False
      #screen.fill((255,0,0))
      screen.blit(bgd,(0,0))
      go_font=font.render('GAME OVER', False, (255, 255, 255))
      screen.blit(go_font,(50,100))
      score_font=font.render('Your Score is '+scoreText,False, (255, 255, 255))
      screen.blit(score_font,(50,200))
      pygame.display.update()


#gameOver(str(1000))