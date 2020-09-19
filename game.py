import math
import random
import pygame
from pygame import mixer

# Pygame initialization
pygame.init()

# Background music
mixer.music.load('res/background.wav')
mixer.music.play(-1)

score         = 0
TITLE         = 'Space Wars' # Game title
WINDOW_HEIGHT = 800          # Height
WINDOW_WIDTH  = 600          # WIDTH
running       = True         # GAME LOOP STATE
lLollision    = False

# GAME GUI
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
background = pygame.image.load('/home/eclipse/Documents/Workspace/Space Wars/res/background.png')

# X-WING
Xx = 370
Xy = 480
xVelocity = 0
xIMG = pygame.image.load('/home/eclipse/Documents/Workspace/Space Wars/res/player.png')


# TIE-FIGHTER
Tx = random.randint(0, 736)
Ty = random.randint(50, 150)
tVelocity = 10
tIMG = pygame.image.load('/home/eclipse/Documents/Workspace/Space Wars/res/enemy.png')

# LEASER
shooting = False
Lx = 0
Ly = 480
lVelocity = 30
lIMG = pygame.image.load('/home/eclipse/Documents/Workspace/Space Wars/res/bullet.png')

# SCORE
score_font = pygame.font.Font('res/Starjedi.ttf', 32)
Sx = 10
Sy = 10

def show_score(x, y ,s ):
    score_  = score_font.render(f"Kills: {str(score)}" , True, (255, 255, 255))
    screen.blit(score_, (x, y))

def x_wing(x, y):
    """PLAYER"""
    screen.blit(xIMG, (x, y))

def spwan():
    global Tx, Ty
    Tx = random.randint(0, 756)
    Ty = random.randint(50, 150)


def tie_fighter(x, y):
    """ENEMY"""
    screen.blit(tIMG, (x, y))



def fire_bullet(x, y):
    global shooting
    shooting = True
    screen.blit(lIMG, (x + 16, y + 10))

def XxMovement():
    """MOVEMENTS OF X WING

    :Xx: GLOBAL VARIABLE OF XWING'S X AXIS

    #USEAGE: PLAYER CONTROLLED XWING""" 
    global Xx
    Xx += xVelocity
    # BOUNDRY THING
    if Xx <= 0:
        Xx = 0
    elif Xx >= 736:
        Xx = 736



def XyMovement():
    """MOVEMENTS OF X WING

    :Xx: GLOBAL VARIABLE OF XWING'S X AXIS

    #USEAGE: PLAYER CONTROLLED XWING""" 
    global Xy
    Xy += xVelocity
    # BOUNDRY THING
    if Xy <= 0:
        Xy = 0
    elif Xx >= 736:
        Xx = 736
     
    

def lMovement():
    global Ly, shooting
    if Ly <= 0:
        Ly = 480
        shooting = False
    if shooting == True:
       
        fire_bullet(Lx, Ly)
        Ly -= lVelocity



      



# GAME LOOP
while running:
    
    screen.fill((1,1,1)) 
    # Implementing background image
    screen.blit(background, (0, 0))
    #  Event listener
    for event in pygame.event.get():
        # On close button function
        if event.type == pygame.QUIT:
            running = False
        # KEY PRESSED EVENTS
        if event.type == pygame.KEYDOWN:
            # LEFT KEY
            if event.key == pygame.K_LEFT:
                xVelocity = -20
            # RIGHT KEY
            if event.key == pygame.K_RIGHT:
                xVelocity = 20
            # UP
            if event.key == pygame.K_UP:
                xVelocity = -20
            if event.key == pygame.K_DOWN:
                xVelocity = 20
            # FIRING SYSTEM
            if event.key == pygame.K_SPACE:
                if not shooting:
                    lSFX = mixer.Sound('/home/eclipse/Documents/Workspace/Space Wars/res/shoooting.wav')
                    lSFX.play()
                    Lx = Xx
                    fire_bullet(Lx, Ly)

        # KEYREALSE EVENT
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xVelocity = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                xVelocity = 0

    BLACK = 1,1,1
    xw_hitbox = pygame.Rect(Xx, Xy, 64, 64)    

    tf_hitbox = pygame.Rect(Tx, Ty, 64, 64)

    ls_hitbox = pygame.Rect(Lx, Ly, 32, 32)


    # CLOOSION

    if ls_hitbox.colliderect(tf_hitbox):
        exSFX = mixer.Sound('res/explosion.wav')
        exSFX.play()
        Ly = 480
        score += 1
        shooting = False
        spwan()
    
    tie_fighter(Tx, Ty)    
    lMovement()
    XxMovement()
    x_wing(Xx, Xy)
    
    show_score(Sx, Sy, score)
    pygame.display.update()