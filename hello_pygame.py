import pygame
from sys import exit
import time
import random

class Aircraft:
    def restart(self):
        self.x = 1000
        self.y = 800

    def __init__(self):
        self.restart()
        self.image = pygame.image.load('ufo.png').convert_alpha()

    def move(self):
        x, y = pygame.mouse.get_pos()
        #turned out aircraft(x,y) actually is aircraft's top left corner(x,y)
        #to make mouse at the center of aircraft,move more
        #move towards origin flatly -> (0,height/2)<-relatively to mouse
        x -= self.image.get_width() / 2
        #up -> (0,0)
        y -= self.image.get_height() / 2
        #reassign examp's attribute
        self.x = x
        self.y = y

class Bullet:
    #initialize bullet's position and variable to save
    #set initial y<0 then it will run path1 in later loop
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load('bullet.png').convert_alpha()
        #set bullet's default status as inactive
        #then they can sleep in box soundly to be arranged
        self.active = False
    def move(self):
        #this loop is to set position for bullet drawing
        #only active bullets fly
        if self.active == True:
            self.y -= 3
        #if bullet beyond window give it a rest for next run
        if self.y < 0:
            self.active = False

    def restart(self):
        #initialize bullet's position in accordance with mouse(seem shooted from aircraft/mouse)
        #get mouse's position and store them in variables mX, mY
        mX, mY = pygame.mouse.get_pos()
        self.x = mX - self.image.get_width() / 2
        self.y = mY - self.image.get_height() / 2
        time.sleep(0.0025)
        self.active = True

class Enemy:
    def restart(self):
        self.x = random.randint(100,750)
        self.y = random.randint(-200,-50)
        self.speed = random.random() + 0.1

    def __init__(self):
        self.restart()
        #to enrich game I use choice to add diverse enemy,turn out they don't always all appear in a round:(WHAT SHOULD I DO?
        self.image = pygame.image.load(random.choice(['red.png','yellow.png','boss.png'])).convert_alpha()

    def move(self):
        #if enemy is within window, move down
        if self.y < 500:
            self.y += 0.3
        else:
            #initialize position
            self.restart()

def checkhit(bullet,enemy):
    if (bullet.x > enemy.x and bullet.x < enemy.x + enemy.image.get_width()) and (bullet.y > enemy.y and bullet.y < enemy.y + enemy.image.get_height()):
        enemy.restart()
        bullet.active = False
    else:
        pass

def checkcrash(aircraft,enemy):
    if (aircraft.x + 0.5*aircraft.image.get_width() > enemy.x) and (aircraft.x + 0.5*aircraft.image.get_width() < enemy.x + enemy.image.get_width()) and (aircraft.y + 0.5*aircraft.image.get_height() > enemy.y) and (aircraft.y + 0.5*aircraft.image.get_height() < enemy.y +enemy.image.get_height()):
        return True
    else:
        return False

pygame.init()

#open game window
screen = pygame.display.set_mode((820, 461), 0, 32)
pygame.display.set_caption("Stardust")
#pull in images
background = pygame.image.load('back.jpg').convert()
aircraft = pygame.image.load('ufo.png').convert_alpha()

aircraft = Aircraft()

#create bullets' box
bullets = []
#load 5 bullets
for i in range(5):
    #all bullets belong to class Bullet
    bullets.append(Bullet())
#sum of bullets
count_b = len(bullets)
#the to-be-active bullet next;default is NO.0
index_b = 0
#set interval between different bullet so they don't mix
interval_b = 0

#creat enemy camp
enemies = []
for i in range(3):
    enemies.append(Enemy())

gameover = False

#the main loop of game
while True:
    #respond to event that user trigger 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.time.delay(7000)
    #draw background on canvas
    screen.blit(background, (0,0))

    if gameover == False:

        #like countdown:3,2,1,shoot!
        interval_b -= 1
        if interval_b < 0:
            bullets[index_b].restart()
            #reset for countdowm again
            interval_b = 100
            #choose the next bullet
            #0%5=0, 3%5=3, 5%5=0, smart loop!
            index_b = (index_b + 1) % count_b
        #give bullet method according to its status
        for b in bullets:
            if b.active == True:
                #check each bullet whether it hit an enemy
                for e in enemies:
                    checkhit(b,e)
                b.move()
                #draw bullet before aircraft then the bullet fly from under it
                screen.blit(b.image, (b.x, b.y))
            
        for e in enemies:
            if checkcrash(aircraft,e) == True:
                gameover = True
            e.move()
            screen.blit(e.image, (e.x, e.y))

        aircraft.move()
        screen.blit(aircraft.image, (aircraft.x,aircraft.y))
        pygame.display.update()

    else:
        pass