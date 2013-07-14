import pygame

from pygame.locals import *

import sys

pygame.init()

bif = "bg.jpg"
mfi = "mouse.png"

screen = pygame.display.set_mode((640,360),0,32)

background = pygame.image.load(bif).convert()

ball = pygame.image.load(mfi).convert_alpha()

x = 0

while True:

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()


    screen.blit(background,(0,0))

    screen.blit(ball,(x,160))

    x += 0.5

    if x > 640:

        x =0

    pygame.display.update()

                
