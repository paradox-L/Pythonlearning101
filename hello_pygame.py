import pygame
from sys import exit
import time

class Bullet:
    #initialize bullet's position and variable to save
    #set initial y<0 then it will run path1 in later loop
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load('bullet.png').convert_alpha()
    def move(self):
        #this loop is to set position for bullet drawing
        #if bullet beyond window
        if self.y < 0:
            #get mouse's position and store them in variables mousex, mousey
            mX, mY = pygame.mouse.get_pos()
            #set bullet's initial position in accordance with mouse(seem shooted from aircraft/mouse)
            #the two evaluation below will make bullet_y,x positive cuz your mouse(x,y)are very POSITIVE!
            self.x = mX - self.image.get_width() / 2
            self.y = mY - self.image.get_height() / 2
        #if bullet within window
        else:
            time.sleep(0.0025)
            #make bullet move up for 5 units each time
            #until y<0 and get return to path1 to get initial position again
            self.y -= 5

pygame.init()

#open game window
screen = pygame.display.set_mode((820, 461), 0, 32)
pygame.display.set_caption("Stardust")
#pull in images
background = pygame.image.load('back.jpg').convert()
plane = pygame.image.load('ufo.png').convert_alpha()
bullet = Bullet()

#the main loop of game
while True:
    #respond to event that user trigger 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #draw background on canvas
    screen.blit(background, (0,0))

    bullet.move()
    #draw bullet before airctaft then the bullet fly from under it
    screen.blit(bullet.image, (bullet.x, bullet.y))
    #if directly use x,y the aircraft will be at the lower right corner of mouse.Why?...
    x, y = pygame.mouse.get_pos()
    #to make mouse at the center of aircraft,move aircraft more
    #move towards origin flatly -> (0,height/2)<-relatively to mouse
    x -= plane.get_width() / 2
    #up -> (0,0)
    y -= plane.get_height() / 2
    #now aircraft's(x,y) = mouse's(x,y),draw aircraft!
    screen.blit(plane, (x,y))
    pygame.display.update()