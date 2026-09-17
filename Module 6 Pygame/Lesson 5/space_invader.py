import math
import random
import pygame

#Constants
SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27

#INITIALIZE Pygame
pygame.init()

#Create the screen
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#background
bg=pygame.image.load('background.png')

#caption and icon
pygame.display.set_caption("Space Invader")
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player
playerImg=pygame.image.load('player.png')
playerx=PLAYER_START_X
playerY=PLAYER_START_Y
playerx_change=0

#enemy
enemyimg=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
num_of_enemies=6

#this i is not used in the loop
for _i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('energy.png'))
    enemyx.append(random.randint(0, SCREEN_WIDTH -64))
    enemyy.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyx_change.append(ENEMY_SPEED_X)
    enemyy_change.append(ENEMY_SPEED_Y)

#BULLET
bulletimg=pygame.image.load('bullet.png')
bulletx=0
bullety=PLAYER_START_Y
bulletx_change=0
bullety_change=BULLET_SPEED_Y
bullet_state="ready"

#score
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textx=10
texty=10

#game over text
over_font=pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    #display text
    score=font.render("score:"+str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    #display text
    over_text=over_font.render("GAME OVER:(", True, (255, 255, 255))