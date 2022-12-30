

def StartMenu():    
    ### Import Pygame
    import pygame
    from game import StartGame
    from credits import creditScreen
    from pygame import mixer
    ### Initialize
    pygame.init()
    pygame.font.init()
    mixer.init()
    mixer.music.load("dark-forest.mp3")
    mixer.music.play()
    
    
    SCREEN_WIDTH= 640
    SCREEN_HEIGHT= 480
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    Background = pygame.image.load('road.jpg').convert_alpha()
    Background = pygame.transform.scale(Background,(SCREEN_WIDTH,SCREEN_HEIGHT))

    normal_button = pygame.image.load("button.png").convert_alpha()
    normal_button = pygame.transform.scale(normal_button, (120, 60))
    hover_button = pygame.image.load("buttonhover.png").convert_alpha()
    hover_button = pygame.transform.scale(hover_button, (120, 60))
    
    ### Game Loop
    running = True
    while running:
      #play_music('caveoftime.mp3')
      """
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

      """
      screen.blit(Background,(0,0))
      
      ### Title Text (can replace later with image for better aesthetics)
      max_text_width = SCREEN_WIDTH*.8
      Title = "Zombie Road Rage" #sample title, can be changed
      titleSize = int(max_text_width / len(Title))
      titleFont = pygame.font.SysFont("comicsans", titleSize)

      titleText = titleFont.render(Title, False, (0, 0, 0))
      titleX_pos = (SCREEN_WIDTH-titleText.get_width()) // 2
      
      screen.blit(titleText, (titleX_pos, 50))
    
      ### Buttons Setting
    
      buttonHeight = 60
      buttonWidth = buttonHeight*2
      buttonX_Pos = (SCREEN_WIDTH-buttonWidth) // 2
      
      ### Start Button
      
      start_normal_button = normal_button
      start_hover_button = hover_button
      screen.blit(start_normal_button,(buttonX_Pos, 100))
      for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range(buttonX_Pos,buttonX_Pos+120) and event.pos[1] in range(100,160):
              StartGame()
      mouse_x, mouse_y = pygame.mouse.get_pos()
      if buttonX_Pos < mouse_x < buttonX_Pos+120 and 100 < mouse_y < 160:
        screen.blit(start_hover_button,(buttonX_Pos, 100))
      
      ### Credits Button
        
      credits_normal_button = normal_button
      credits_hover_button = hover_button
      screen.blit(credits_normal_button,(buttonX_Pos, 200))
      for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range(buttonX_Pos,buttonX_Pos+120) and event.pos[1] in range(200,260):
              creditScreen()
      mouse_x, mouse_y = pygame.mouse.get_pos()
      if buttonX_Pos < mouse_x < buttonX_Pos+120 and 200 < mouse_y < 260:
        screen.blit(credits_hover_button,(buttonX_Pos, 200))
    
      ### Exit Button

      exit_normal_button = normal_button
      exit_hover_button = hover_button
      screen.blit(exit_normal_button,(buttonX_Pos, 300))
      """for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range(buttonX_Pos,buttonX_Pos+120) and event.pos[1] in range(300,360):
              pygame.quit()"""
      mouse_x, mouse_y = pygame.mouse.get_pos()
      if buttonX_Pos < mouse_x < buttonX_Pos+120 and 300 < mouse_y < 360:
        screen.blit(exit_hover_button,(buttonX_Pos, 300))
      
        ### Text Settings
      maxTextSize = buttonWidth*.8
      buttonTextSize = int(maxTextSize / 5)
      buttonsFont = pygame.font.SysFont("comicsans", buttonTextSize)
    
      ### Start Text
      startText = buttonsFont.render("Start", False, (0, 0, 0))

      startText_X = buttonX_Pos + (120 - startText.get_width()) // 2
      
      screen.blit(startText, (startText_X, 125))
      screen.blit(startText, (startText_X, 125))
    
      ### Credits Text
      creditsText = buttonsFont.render("Credits", False, (0, 0, 0))
    
      creditText_X = buttonX_Pos + (120 - creditsText.get_width()) // 2
      
      screen.blit(creditsText, (creditText_X, 225))
      screen.blit(creditsText, (creditText_X, 225))
    
      ### Exit Text
      exitText = buttonsFont.render("Exit", False, (0, 0, 0))
    
      exitText_X = buttonX_Pos + (120 - exitText.get_width()) // 2
      
      screen.blit(exitText, (exitText_X, 325))
      screen.blit(exitText, (exitText_X, 325))

      ### Event
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range(buttonX_Pos,buttonX_Pos+120) and event.pos[1] in range(100,160):
              #print("Game started.")
              StartGame()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range(buttonX_Pos,buttonX_Pos+120) and event.pos[1] in range(200,260):
              creditScreen()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range(buttonX_Pos,buttonX_Pos+120) and event.pos[1] in range(300,360):
              pygame.quit()
      ### Best Score
    
    
      
      pygame.display.update()


#StartMenu()