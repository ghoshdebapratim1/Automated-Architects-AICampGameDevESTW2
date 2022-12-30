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

#Initializing
import pygame
from pygame import mixer

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
score=0
font = pygame.font.SysFont("comicsans", 10)
scoreText = font.render('score, False, (0, 0, 0))



#Load images
Background = pygame.image.load('road.png').convert_alpha()
Background = pygame.transform.scale(Background, (WIDTH, HEIGHT))
Player = pygame.image.load('walk(1).png').convert_alpha()
Player = pygame.transform.rotozoom(Player, 0, 0.2)

#Player Locations
playerX = WIDTH / 2 - 300
playerY = HEIGHT / 2 + 80
playerY_change = 0

#Zombie Locations
import random

enemyX = playerX + random.randint(300, 600)
enemyY = random.randint(0, 360) 
enemyZ = playerX + random.randint(320, 620)

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

## Initialising The Side Scroll
bgx = 0

## Jump Mechanics Initialisation
'''
gravity = 0.5
jumpcount = 0
jump = 0
'''

#Game loop
running = True
while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #Background
  screen.blit(Background, (bgx - WIDTH, 0))
  screen.blit(Background, (bgx, 0))
  screen.blit(Background, (bgx + WIDTH, 0))

  bgx = bgx - 0.5

  if bgx <= -WIDTH:
    bgx = 0

  #Time
  current_time = pygame.time.get_ticks()

  ### Enemy Animations
  if zombieBoyFrame >= len(zombieBoyWalk):
    zombieBoyFrame = 0
  Enemy = zombieBoyWalk[zombieBoyFrame]
  Enemy = pygame.transform.rotozoom(Enemy, 0, 0.2)
  Enemy = pygame.transform.flip(Enemy, True, False)

  if current_time - lastUpdate > 3000:
    zombieBoyFrame += 1
  
  if zombieGirlFrame >= len(zombieGirlWalk):
    zombieGirlFrame = 0
  EnemyF = zombieGirlWalk[zombieGirlFrame]
  EnemyF = pygame.transform.rotozoom(EnemyF, 0, 0.2)
  EnemyF = pygame.transform.flip(EnemyF, True, False)

  if current_time - lastUpdate > 3000:
    zombieGirlFrame += 1

  ## Move Up
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
  enemyZ -= 0.2

  if enemyX < 0:
    enemyX = playerX + random.randint(600, 800)
    enemyY = random.randint(0, 360) 
  if enemyfX < 0:
    enemyfX = playerX + random.randint(600, 800)
    enemyfY = random.randint(0, 360) 
  
  #Blit
  enemy_rect1 = screen.blit(Enemy, (enemyX, enemyY))
  enemy_rect2 = screen.blit(EnemyF, (enemyfX, enemyfY))
  player_rect = screen.blit(Player, (playerX, playerY))
  screen.blit(scoreText,(0,0))
  
  #Collision+lose condition
  if player_rect.colliderect(enemy_rect1):
    print("Player has died.")
   
    pygame.display.quit()
    exit()
  if player_rect.collderect(enemy_rect2):
     print("Player has died")
     
     pygame.display.quit()
     exit()
    event.type == pygame.QUIT
    
  #Update
  pygame.display.update()
  score+=1
