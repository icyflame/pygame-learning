import pygame

from pygame.locals import *

import sys

pygame.init()

big = "bg.jpg"
mfi = "mouse.png"

screen = pygame.display.set_mode((640,360),0,32)

background = pygame.image.load(big).convert()

mouse_c = pygame.image.load(mfi).convert_alpha()

while True:

    ##to make sure that the loop never ends

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()


    screen.blit(background,(0,0))

    x,y = pygame.mouse.get_pos()

    print x,y

    x -= mouse_c.get_width()/2

    y -= mouse_c.get_height()/2

    screen.blit(mouse_c,(x,y))

    pygame.display.update()
