##like paint. Draw a figue using this and then
##stop drawing when the mouse button is pressed down.

import pygame

from pygame.locals import *

import sys

pygame.init()


screen = pygame.display.set_mode((640,360),0,32)

color = (255,0,0)

points = []

flag = False

while True:

    

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()

        if event.type == KEYDOWN:

            if event.key == K_d:  ##draw

                flag = True

            if event.key == K_s:  ##stop drawing

                flag = False

                points = []


    if flag:

        points.append(pygame.mouse.get_pos())

        if len(points) > 1:

            pygame.draw.lines(screen,color,False,points,2)
        
    pygame.display.update()

                
