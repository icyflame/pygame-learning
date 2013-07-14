import pygame

from pygame.locals import *

import sys

pygame.init()

big = "bg.jpg"
mfi = "mouse.png"

screen = pygame.display.set_mode((640,360),0,32)

background = pygame.image.load(big).convert()

cursor = pygame.image.load(mfi).convert_alpha()


while True:

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()


    screen.lock()

    ##we will draw a shape now.

    pygame.draw.rect(screen, (0,0,255),Rect((100,100),(10,20)))        

    screen.unlock()

    pygame.display.update()

                
