import pygame
from sys import exit
import time

pygame.init()

#open game window
screen = pygame.display.set_mode((820, 461), 0, 32)
pygame.display.set_caption("Stardust")
#pull in images
background = pygame.image.load('back.jpg').convert()
plane = pygame.image.load('ufo.png').convert_alpha()
bullet = pygame.image.load('bullet.png').convert_alpha()

#initialize bullet's position and variable to save
bullet_x = 0
#set initial y<0 then it will run path1 in later loop
bullet_y = -1
#the main loop of game
while True:
    #respond to event that user trigger 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #draw background on canvas
    screen.blit(background, (0,0))
    #get mouse's position and store them in variables x, y
    x, y = pygame.mouse.get_pos()
    #if bullet beyond window
    if bullet_y < 0:
        #set bullet's initial position(seem shooted from aircraft/mouse)
        #the two evaluation below will make bullet_y,x positive cuz your mouse(x,y)are very POSITIVE!
        bullet_x = x - bullet.get_width() / 2
        bullet_y = y - bullet.get_height() / 2
    #if bullet within window
    else:
        #make bullet move up for 5 units
        #each time until y<0 and get return to path1 to get initial position again
        bullet_y -= 5
    #draw bullet before airctaft then the bullet fly from under it
    time.sleep(0.0025)
    screen.blit(bullet, (bullet_x,bullet_y))
    #if directly use x,y the aircraft will be at the lower right corner of mouse.Why?...
    #to make mouse at the center of aircraft,move aircraft more
    #move towards origin flatly -> (0,height/2)
    x -= plane.get_width() / 2
    #up -> (0,0)
    y -= plane.get_height() / 2
    #now aircraft's(x,y) = mouse's(x,y),draw aircraft!
    screen.blit(plane, (x,y))
    pygame.display.update()