import pygame

from pygame.locals import *

import sys

pygame.init()


screen = pygame.display.set_mode((640,360),0,32)

color = (255,255,0)

position = (300,176)

radius = 60


while True:

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()


    screen.lock()

    ##we will draw a shape now.

    pygame.draw.circle(screen,color,position,radius)

    pygame.draw.circle(screen,(255,0,0),position,20)

    pygame.draw.circle(screen,color,(420,176),radius)

    pygame.draw.circle(screen,(255,0,0),(420,176),20)
            

    screen.unlock()

    pygame.display.update()

                
