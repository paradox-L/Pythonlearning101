import pygame
from sys import exit
import time
import random

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
            #set bullet's initial position in accordance with mouse(seem shooted from aircraft/mouse)
            #get mouse's position and store them in variables mX, mY
            mX, mY = pygame.mouse.get_pos()
            #the two evaluation below will make bullet.y,x positive cuz your mouse(x,y)are very POSITIVE!
            self.x = mX - self.image.get_width() / 2
            self.y = mY - self.image.get_height() / 2
        #if bullet within window
        else:
            time.sleep(0.0025)
            #make bullet move up for 5 units each time
            #until y<0 and get return to path1 to get initial position again
            self.y -= 5

class Enemy:
    def restart(self):
        self.x = random.randint(100,750)
        self.y = random.randint(-200,-50)
        self.speed = random.random() + 0.1

    def __init__(self):
        self.restart()
        self.image = pygame.image.load('red.png').convert_alpha()

    def move(self):
        #if enemy is within window, move down
        if self.y < 500:
            self.y += 0.3
        else:
            #initialize position
            self.restart()

pygame.init()

#open game window
screen = pygame.display.set_mode((820, 461), 0, 32)
pygame.display.set_caption("Stardust")
#pull in images
background = pygame.image.load('back.jpg').convert()
aircraft = pygame.image.load('ufo.png').convert_alpha()

bullet = Bullet()

enemy = Enemy()

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
    #draw bullet before aircraft then the bullet fly from under it
    screen.blit(bullet.image, (bullet.x, bullet.y))

    enemy.move()
    screen.blit(enemy.image, (enemy.x, enemy.y))
    #if directly use x,y the aircraft will be at the lower right corner of mouse.Why?...
    x, y = pygame.mouse.get_pos()
    #to make mouse at the center of aircraft,move aircraft more
    #move towards origin flatly -> (0,height/2)<-relatively to mouse
    x -= aircraft.get_width() / 2
    #up -> (0,0)
    y -= aircraft.get_height() / 2
    #now aircraft's(x,y) = mouse's(x,y),draw aircraft!
    screen.blit(aircraft, (x,y))
    pygame.display.update()