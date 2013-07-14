import pygame

from pygame.locals import *

import sys

pygame.init()


screen = pygame.display.set_mode((640,360),0,32)

color = (255,0,0)

pos1 = (20,20)

pos2 = (140,100)



while True:

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()


    screen.lock()

    pygame.draw.line(screen,color,pos1,pos2,8)
            

    screen.unlock()

    pygame.display.update()

                
