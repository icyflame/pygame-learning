import pygame

from pygame.locals import *

import sys

pygame.init()

big = "bg.jpg"
mfi = "mouse.png"

screen = pygame.display.set_mode((640,360),0,32)

background = pygame.image.load(big).convert()

cursor = pygame.image.load(mfi).convert_alpha()

x,y = 0,0

movex, movey = 0,0

unit = 10

while True:

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()


        if event.type == KEYDOWN:

            if event.key==K_LEFT:

                movex = -1*unit

            if event.key == K_RIGHT:

                movex = unit

            if event.key == K_UP:

                movey = -1*unit

            if event.key == K_DOWN:

                movey = unit

        if event.type == KEYUP:

            if event.key==K_LEFT:

                movex = 0

            elif event.key == K_RIGHT:

                movex = 0

            elif event.key == K_UP:

                movey = 0


            elif event.key == K_DOWN:

                movey = 0     


        x+= movex

        y+= movey


        screen.blit(background,(0,0))


        screen.blit(cursor,(x,y))

        pygame.display.update()

                
