import pygame
from sys import exit
import time
import random

name = raw_input("What's your nickname?")

try:
    f = open('scoresys.txt')
    lines = f.readlines()
    f.close()
except:
    print"Make sure there's scoresys.txt with 1st line'0 0' under dir"

docs = {}
for line in lines:
    data = line.split()
    docs[data[0]] = data[1:]

player = docs.get(name)
if player == None:
    player = [0,0]

rounds = int(player[0])
maxscore = int(player[1])
print"Hello,%s.You have played %dround(s),your highest score is %d"%(name, rounds, maxscore)

sumround = 0

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
        return True
    else:
        return False

def checkcrash(aircraft,enemy):
    #I draw a pic to analysis their relative position to make visual effect reasonble,yet still little strange:(
    if (aircraft.x + 0.1*aircraft.image.get_width() > enemy.x) and (aircraft.x + 0.9*aircraft.image.get_width() < enemy.x + enemy.image.get_width()) and (aircraft.y + 0.1*aircraft.image.get_height() > enemy.y) and (aircraft.y + 0.9*aircraft.image.get_height() < enemy.y +enemy.image.get_height()):
        return True
    else:
        return False

pygame.init()

print"Game starts"
track = pygame.mixer.music.load('Flower Dance.mp3')
pygame.mixer.music.play()

#open game window
screen = pygame.display.set_mode((820, 461), 0, 32)
pygame.display.set_caption("Stardust            --Click to Pause for 7s  -- if GAMEOVER Click to Revive  --ONE click each time!!")
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
for i in range(5):
    enemies.append(Enemy())

#creat goal board
score = 0
font = pygame.font.Font(None,48)

gameover = False

#mean the game is running,else game is paused
status = 1

#the main loop of game
while True:
    #respond to event that user trigger
    if status == 1: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if gameover == True and event.type == pygame.MOUSEBUTTONDOWN:
                #restart game
                aircraft.restart()
                for b in bullets:
                    b.active = False
                for e in enemies:
                    e.restart()
                score = 0
                gameover = False
                status = 0

            if gameover == False and event.type == pygame.MOUSEBUTTONDOWN:
                pygame.time.delay(7000)
                status = 0
    else:
        print"Easy!Easy!Be paitient to wait!:)"
        status = 1

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
                    if checkhit(b,e):
                        score += 10
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

        #draw text on a new Surface
        #Grammar: render(text, antialias, color, background=None) -> Surface
        text = font.render("Your score:%d"%score, 1, (46,169,223))
        screen.blit(text, (0,0))

    else:
        text = font.render("Your score:%d"%score, 1, (46,169,223))
        screen.blit(text, (410,230))
        if score > maxscore:
            maxscore = score
        sumround += 1

    pygame.display.update()

    docs[name] = [str(sumround),str(maxscore)]
    result = ''
    for nickname in docs:
        putin = nickname + ' ' + ' '.join(docs[nickname]) + '\n'

    result += putin

    f = open('scoresys.txt','w')
    f.write(result)
    f.close()