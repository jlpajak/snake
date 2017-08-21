#all time classic

import pygame #module for 2D games
import sys #quiting and such usefull functionality
import random #to randomize food position
import time #sleep

#init error check
check4error=pygame.init()
#pygame.init is a tuple first (i,j) where i is number of tasks j is number of errors
if check4error[1] > 0:
    print ("Had {0} errors initializing".format(check4error[1]))
    sys.exit()
else:
    print("PyGame initialized successfully")

#colours
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

#interface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake')

#fraps control
fpsControll = pygame.time.Clock()

#snake himself
snakePosition = [360, 230] #head coordinates
snakeBody = [[360,230],[350,230],[340,230]]

#the f word
foodPosition = [random.randrange(1,72)*10, random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changedirection = direction

score = 0

#game over
def gameover():
    goFont = pygame.font.SysFont('monaco', 72)
    gosurface = goFont.render('Game over!', True, red)
    gorect = gosurface.get_rect()
    gorect.midtop=(360, 20)
    playSurface.blit(gosurface,gorect)
    scoredisplay(gameinprogres=0)
    pygame.display.flip()
    time.sleep(10)
    pygame.quit() #pygame
    sys.exit() #console

#score board
def scoredisplay(gameinprogres=1):
    sFont = pygame.font.SysFont('monaco', 24)
    ssurface = sFont.render('Score: {0}'.format(score), True, black)
    srect=ssurface.get_rect()
    if gameinprogres == 1:
        srect.midtop = (80,10)
    else:
        srect.midtop = (360,120)
    playSurface.blit(ssurface,srect)

#game logic
while True: #infinte loop
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord ('d'):
                changedirection = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord ('a'):
                 changedirection = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord ('w'):
                changedirection = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord ('s'):
                changedirection = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    #direction conditions
    if changedirection == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changedirection == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changedirection == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changedirection == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    #movement
    if direction == 'RIGHT':
        snakePosition[0] += 10
    if direction == 'LEFT':
        snakePosition[0] -= 10
    if direction == 'UP':
        snakePosition[1] -= 10
    if direction == 'DOWN':
        snakePosition[1] += 10

    #body mechanics
    snakeBody.insert(0, list(snakePosition))
    if snakePosition[0] == foodPosition[0] and snakePosition[1] == foodPosition[1]:
        score +=1
        foodSpawn = False
    else:
        snakeBody.pop()

    #spawning new food
    if foodSpawn == False:
        foodPosition = [random.randrange(1,72)*10, random.randrange(1,46)*10]
    foodSpawn = True

    #drawing actual game
    playSurface.fill(white) #background
    for position in snakeBody: #snake
        pygame.draw.rect(playSurface, green, \
        pygame.Rect(position[0],position[1],10,10))
    pygame.draw.rect(playSurface, blue, \
    pygame.Rect(foodPosition[0],foodPosition[1],10,10)) #food

    #boundaries
    if snakePosition[0] > 710 or snakePosition[0] <0: #x axis
        gameover()
    if snakePosition[1] > 450 or snakePosition[1] <0: #y axis
        gameover()

    for block in snakeBody[1:]: #selfbites
        if snakePosition[0] == block[0] and snakePosition[1] == block[1]:
            gameover()

    scoredisplay()
    pygame.display.flip()
    fpsControll.tick(30)
