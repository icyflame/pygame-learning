import pygame

from pygame.locals import *

import sys

pygame.init()


screen = pygame.display.set_mode((640,360),0,32)

listOfPoints = [(1,1),(2,5),(6,120),(41,78),(100,100),(80,60)]

colorRed = (255,0,0)

while True:

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()


    screen.lock()

    ##we will draw a shape now.

    pygame.draw.polygon(screen,colorRed,listOfPoints)        
            

    screen.unlock()

    pygame.display.update()

                
