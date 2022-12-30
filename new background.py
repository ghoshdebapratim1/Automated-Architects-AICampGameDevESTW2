# #Feel free to use parts of the code below in your final project!

# #The code below is for generating map5 as seen in the Maps folder in the Final Project Scaffold. You can edit it to your own liking!

# import pygame, sys
# from pygame.locals import QUIT

# pygame.init()
# screen = pygame.display.set_mode((640,480)) #All maps are made for this screen resolution, if you want a different size screen, you need to edit the map file or make your own.
# pygame.display.set_caption('Final Project Scaffold')

# dirt=pygame.image.load('Game_Assets/Map_Tiles/dirt1.png').convert_alpha() # How the images are loaded in
# dirt= pygame.transform.scale(dirt,(16,16)) #Changing image to 16x16

# grass=pygame.image.load('Game_Assets/Map_Tiles/grass1.png').convert_alpha() # How the images are loaded in
# grass= pygame.transform.scale(grass,(16,16)) #Changing image to 16x16

# tile_size=(16,16)

# def load_map(path):
#     '''Function to load the map file and split it into list.

#     Inputs:
#     path: the folder where the map is stored

#     Outputs:
#     game_map: the map on the screen
    
#     '''
#     f = open(path + '.txt', 'r')
#     data = f.read()
#     f.close
#     data = data.split('\n')
#     game_map = []
#     for row in data:
#         game_map.append(list(row))
#     return game_map

  
# #Loads map file
# game_map = load_map('Maps/map5') #Opens the map as listed in maps.txt in the Maps folder.



# while True:
#     screen.fill((146,244,255)) #Sets the sky-blue BG color
#     y = 0
#     for row in game_map:
#         x = 0
#         for tile in row:
#             if tile == '1':
#                 screen.blit(dirt, (x * tile_size[0], y * tile_size[1]))
#             elif tile == '2':
#                 screen.blit(grass, (x * tile_size[0], y * tile_size[1]))          
#             elif tile =='3':
#                 #screen.blit(image3, (x * tile_size[0], y * tile_size[1])) #Just an example, add as many images as you need.
#               pass
#             x += 1
#         y += 1
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()


#Initislizing
import pygame
pygame.init()

#Display Setup
WIDTH= 640
HEIGHT= 480
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Screen")

#Load images
Background = pygame.image.load('road.png').convert_alpha()
Background=pygame.transform.scale(Background,(WIDTH,HEIGHT))
Player = pygame.image.load('character_.png').convert_alpha()
Player=pygame.transform.rotozoom(Player,0,0.2)
enemyboy = pygame.image.load("zombie.png").convert_alpha()
enemygirl = pygame.image.load("Zombiegirl.jpg").convert_alpha()
enemyboy=pygame.transform.scale(enemyboy,(100,100))
enemygirl=pygame.transform.scale(enemyboy,(100,100))

enemyboy=pygame.transform.flip(enemyboy,True,False)
enemygirl=pygame.transform.flip(enemygirl,True,False)

playerX=WIDTH/2-300
playerY=HEIGHT/2+80
playerY_change=0

import random
enemyX= playerX + random.randint(300,600)
enemyY= playerY
enemyZ= playerX + random.randint(320,620)

## Initialising The Side Scroll 
bgx=0

## Jump Mechanics Initialisation 
gravity=1
jumpcount=0
jump=0


#Game loop
running=True
while running:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      running=False
  
  #Background
  screen.blit(Background,(bgx-WIDTH,0))    
  screen.blit(Background,(bgx,0))
  screen.blit(Background,(bgx+WIDTH,0))

  bgx=bgx-0.5

  if bgx<=-WIDTH:
    bgx=0

  #Player Jump Mechanics 
  if playerY< (HEIGHT/2+80):
    playerY+=gravity
  ## Jump 
    
  if event.type==pygame.KEYDOWN:
    if event.key==pygame.K_UP:
      if playerY==(HEIGHT/2+80):
        jump=1

  if jump==1:
    playerY=playerY-4
    jumpcount+=1 
    if jumpcount>60:
      jumpcount=0
      jump=0


  if playerY<0:
    playerY=0
  
  #enemy
  enemyX -= 0.1
  enemyZ -= 0.2
  
  if enemyX < 0:
    enemyX = playerX + random.randint(600,800)

  enemy_rect=screen.blit(enemyboy,(enemyX,enemyY))
  enemy_rect=screen.blit(enemygirl,(enemyX,enemyY))
  player_rect=screen.blit(Player,(playerX,playerY))

  if player_rect.colliderect(enemy_rect):
    print("Player has died.")
    
    '''
    pygame.display.quit()
    exit()
    '''
    
  #Update
  pygame.display.update()

  
  