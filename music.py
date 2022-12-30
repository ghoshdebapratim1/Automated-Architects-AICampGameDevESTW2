
def play_music(path): 
  #Pygame Initizalion
  from pygame import mixer
  mixer.init()
  # Background Music
  mixer.music.load(path)
  mixer.music.play()

import pygame 

pygame.init()

screen=pygame.display.set_mode((800,600))


running=True


 

while running:
  
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
  play_music('dark-forest.mp3')
  screen.fill((0,0,0))
  pygame.display.update()
