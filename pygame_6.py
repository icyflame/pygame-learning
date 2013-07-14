import pygame

from pygame.locals import *

import sys

pygame.init()


screen = pygame.display.set_mode((640,360),0,32)

color = (255,0,0)

rectangle = (40,80,150,90)



while True:

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()


    screen.lock()

    ##we will draw a shape now.

    pygame.draw.ellipse(screen,color,rectangle)

    pygame.draw.rect(screen,color,rectangle,1)

    ##this rectangle is a rectangle which has the four lines as tangents.
            

    screen.unlock()

    pygame.display.update()

                
