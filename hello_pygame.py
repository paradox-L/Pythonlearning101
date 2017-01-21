import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((820, 461), 0, 32)
pygame.display.set_caption("Star War")
background = pygame.image.load('back.jpg').convert()
plane = pygame.image.load('ufo.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0,0))

    x, y = pygame.mouse.get_pos()
    x-= plane.get_width() / 2
    y-= plane.get_height() / 2
    screen.blit(plane, (x,y))
    pygame.display.update()