def StartGame():
    import pygame
    from pygame import mixer
    from menu import StartMenu
    
    pygame.init()
    
    ## Music
    
    mixer.init()
    mixer.music.load("caveoftime.mp3")
    mixer.music.set_volume(0.2)
    mixer.music.play()
    #Display Setup
    WIDTH = 640
    HEIGHT = 480
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Main Screen")
    
    #Score setup
    score=0
    font = pygame.font.SysFont("comicsans", 40)
    
    #Load images
    Background = pygame.image.load('road.png').convert_alpha()
    Background = pygame.transform.scale(Background, (WIDTH, HEIGHT))
    
    
    #Player Locations
    playerAlive = True
    playerX = WIDTH / 2 - 300
    playerY = HEIGHT / 2 + 80
    playerY_change = 0
    
    #Zombie Locations
    import random
    
    
    enemyX = playerX + random.randint(300, 600)
    enemyY = random.randint(0, 360) 
    offset=0
    
    enemyfX = playerX + random.randint(600, 800)
    enemyfY = random.randint(0, 360) 
    
    ### Zombie Animation
    '''
    zombieMoving = False
    zombieVelocity = 12
    zombieX = WIDTH
    zombieY = playerY #Placeholder
    '''
    
    zombieBoyWalk = []
    zombieBoyFrame = 0
    for i in range(10):
      j = i + 1
      zombieBoyWalk.append(
        pygame.image.load(f"zombie/male/Walk ({j}).png").convert_alpha())
    lastUpdate = pygame.time.get_ticks()
    
    zombieGirlWalk = []
    zombieGirlFrame = 0
    for i in range(10):
      j = i + 1
      zombieGirlWalk.append(
        pygame.image.load(f"zombie/female/Walk ({j}).png").convert_alpha())
    
    #Player Animation
    PlayerWalk = []
    PlayerFrame = 0
    for i in range(15):
      j = i + 1
      PlayerWalk.append(
        pygame.image.load(f"character walk/Walk ({j}).png").convert_alpha())
    
    ## Initialising The Side Scroll
    bgx = 0
    
    #Game loop
    running = True
    while running:
    
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
    
      #score text
      scoreText = font.render(str(int(score/1000)), False, (0, 0, 0))
    
      #Background
      screen.blit(Background, (bgx - WIDTH, 0))
      screen.blit(Background, (bgx, 0))
      screen.blit(Background, (bgx + WIDTH, 0))
    
      bgx = bgx - 0.5
    
      if bgx <= -WIDTH:
        bgx = 0
    
      #Time
      current_time = pygame.time.get_ticks()
    
      ###Animations
      if zombieBoyFrame >= len(zombieBoyWalk):
        zombieBoyFrame = 0
      Enemy = zombieBoyWalk[zombieBoyFrame]
      Enemy = pygame.transform.rotozoom(Enemy, 0, 0.2)
      Enemy = pygame.transform.flip(Enemy, True, False)
    
      if current_time - lastUpdate > 1000:
        zombieBoyFrame += 1
      
      if zombieGirlFrame >= len(zombieGirlWalk):
        zombieGirlFrame = 0
      EnemyF = zombieGirlWalk[zombieGirlFrame]
      EnemyF = pygame.transform.rotozoom(EnemyF, 0, 0.2)
      EnemyF = pygame.transform.flip(EnemyF, True, False)
    
      if current_time - lastUpdate > 1000:
        zombieGirlFrame += 1
    
      if PlayerFrame >= len(PlayerWalk):
        PlayerFrame = 0
      Player = PlayerWalk[PlayerFrame]
      Player = pygame.transform.rotozoom(Player, 0, 0.2)
    
      if current_time - lastUpdate > 1000:
        PlayerFrame += 1
    
      ## Move Up/Down
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          playerY_change=-0.2  
        elif event.key == pygame.K_DOWN:
          playerY_change=0.2
      if event.type == pygame.KEYUP:
        if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
          playerY_change=0
    
      playerY+=playerY_change
      if playerY<0:
        playerY=0
      elif playerY>HEIGHT-100:
        playerY=HEIGHT-100
      
      #enemy
      enemyX -= 0.2
      enemyfX -= 0.4
      
      
      if enemyX < -300:
        enemyX = playerX + random.randint(600, 800)
        enemyY = random.randint(0, 360) 
      if enemyfX < -100:
        enemyfX = playerX + random.randint(600, 800)
        enemyfY = random.randint(0, 360) 
      
      #Blit
      enemy_rect = screen.blit(Enemy, (enemyX, enemyY)) 
      enemy_rect = screen.blit(Enemy, (enemyX+200, offset))
      enemy_rect = screen.blit(EnemyF, (enemyfX, enemyfY))
      player_rect = screen.blit(Player, (playerX, playerY))
      screen.blit(scoreText,(10,10))
      
      #Collision+lose condition
      if player_rect.colliderect(enemy_rect):
        #StartMenu()
        print("Game Over")
        playerAlive = False
        
        '''
        pygame.display.quit()
        exit()
        '''
      #Update
      if playerAlive == True:
        score+=1
        #score=int(score)
    
      pygame.display.update()
      