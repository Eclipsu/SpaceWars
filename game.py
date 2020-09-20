import math
import random
import pygame
from pygame import mixer
# Pygame initialization
pygame.init()

# Background music



score         = 0            # Kills
TITLE         = 'Space Wars' # Game title
WINDOW_HEIGHT = 800          # Height
WINDOW_WIDTH  = 600          # WIDTH
running       = True         # GAME LOOP STATE
menu_running  = True
lLollision    = False

# GAME GUI
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
background = pygame.image.load('res/Sprites/background.png')
menu_background = pygame.image.load('res/Sprites/menu_screen.png')

# X-WING
Xx = 370
Xy = 480
xVelocity = 0
xIMG = pygame.image.load('res/Sprites/player.png')

# TIE-FIGHTER
Tx = random.randint(0, 700)
Ty = 100
tVelocity = 10
tIMG = pygame.image.load('res/Sprites/enemy.png')

# LEASER
shooting = False
Lx = 0
Ly = 480
lVelocity = 30
leser = pygame.image.load('res/Sprites/bullet.png')

# Coordinates

# SCORE
score_font = pygame.font.Font('res/fonts/Starjedi.ttf', 32)
Sx = 10
Sy = 10

# T_Leser
t_shooting = False
Tlx = 0
Tly = 100
tLeser = pygame.image.load('res/Sprites/bullet.png')
TlVelocity = 30


def show_score(x, y ,s ):
    """displays the score in the screen
        font: starwars font"""
    score_  = score_font.render(f"Kills: {str(score)}" , True, (255, 255, 255))  # Score variabe
    screen.blit(score_, (x, y))                                                  # Display score



def x_wing(x, y):
    """PLAYER"""
    screen.blit(xIMG, (x, y)) # Draw Xwing | i.e player



def spwan():
    """SPWANS TIE FIGHTER AFTER 1 IS KILELD
    re spwans the tie fighter in random location between 0x - 700x
    """
    global Tx, Ty
    # These variables will re summon
    Tx = random.randint(0, 700)
    Ty = 100



def tie_fighter(x, y):
    """ENEMY """
    screen.blit(tIMG, (x, y)) # Draws tie Fighter



def tie_fighter_movement(x, y):
    """LEFT AND RIGHT MOVEMENT OF TIE FIGHTER
    :arguments:
        :tVelocity: The velocity of the fighter, more it is the faster the fighter moves

    :useage: moves the tiw fighter left and right making it difficult for the player to hit the tie fighter 
    """
    global Tx, tVelocity
    Tx += tVelocity     # Core of this function, this will add values to X cordinate of the fighter.
    if Tx >= 736:       # This will stop the fighter from going out of the screen
        tVelocity = -10 # Change the velocity to negetive which will make the fighter go left isntead
    if Tx <= 0:         # This will too stop the fighter from going out of the screen
        tVelocity = 10  # Change the velocity to negetive which will make the fighter go right isntead



def tFire(x=Tx, y=Tly):
    """FIRING SYSTEM
        :usage: firing function of tie fighter, a challange for the player
    """
    global t_shooting
    t_shooting = True                    # THIS WILL PREVENT THE LESER FOLLWOING THE PLAYER
    screen.blit(tLeser, (x +16, y + 10)) # Draws the leser


def xFire(x, y):
    """FIRING SYSTEM
        :usage: firing function of xwing.
    """
    global shooting 
    shooting = True                      # THIS WILL PREVENT THE LESER FOLLWOING THE PLAYER
    screen.blit(leser, (x + 16, y + 10)) # Draws the leser



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
    """Leser movement
    :usage: leser for xwing movement. this will make the leser go brrrrrrr
    """
    global Ly, shooting
    # Prevents the lser going out of screen
    if Ly <= 0:
        Ly = 480
        shooting = False
    # brrrr
    if shooting == True:
       
        xFire(Lx, Ly)
        Ly -= lVelocity
    


def Tl_movement():
    """Leser movement
    :usage: tie fighters leser movement. this will make the leser go brrrrrrr
    """
    global TlX, Tly, t_shooting
    # Prevents the lser going out of screen
    if Tly >= 600:
        Tly = 100
        t_shooting = False
    # brrrr
    if t_shooting == True:
        tFire(Tlx, Tly)
        Tly += 30



def TiAI(x, Tly):
    """A psudo Ai for the enemy fighter.
    :arguments:
        :sfx:    sound effeft
        :AiRand: creates a random number, if the number is 10, then brrr, ik cringe but WFM mate. 
    :usage: Helps our no brainer tie fighter to shoot the leser
        """
    global Tx, Tlx
    global Tx, Xx, Ty, Xy
    distance = math.sqrt((math.pow(Tx-Xx, 2) + math.pow(Ty-Xy, 2)))

    AiRand = random.randint(0, 20)
    if (AiRand == 10 or AiRand == 15 or AiRand == 10) and not t_shooting:
        sfx = mixer.Sound('res/sfx/t_shooting.wav')
        sfx.play()
        Tlx = Tx
        tFire(Tlx, Tly)


def display_cordinates(x, y):
    pass
# GAME LOOP


def menu_loop():
    mixer.music.load('res/sfx/menu_song.wav')
    mixer.music.play(-1)
    menu_running = True
    while menu_running:
        screen.fill((1,1,1))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu_running = False
        screen.blit(menu_background, (0, 0))
        pygame.display.update()




def game_loop():
    mixer.music.load('res/sfx/background.wav')
    mixer.music.play(-1) 
    global t_shooting, running, screen, Tx, Ty, Xx, Xy, Lx, Ly, Tlx, Tly, tVelocity, xVelocity, tVelocity, tLeser, TlVelocity, lVelocity, score, shooting
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
                    lVelocity = -20
                if event.key == pygame.K_DOWN:
                    lVelocity = 20
                # FIRING SYSTEM
                if event.key == pygame.K_SPACE:
                    if not shooting:
                        lSFX = mixer.Sound('res/sfx/shoooting.wav')
                        lSFX.play()
                        Lx = Xx
                        xFire(Lx, Ly)
                # Enemmy manual fire
                if event.key == pygame.K_RETURN:
                    if not shooting:
                        sfx = mixer.Sound('res/sfx/t_shooting.wav')
                        sfx.play()
                        Tlx = Tx
                        print(Tlx)
                        tFire(Tlx, Tly)
                    

            # KEYREALSE EVENT
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xVelocity = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    xVelocity = 0

        BLACK = 1,1,1
        xw_hitbox = pygame.Rect(Xx, Xy, 64, 64)     # Xwing's hitbox     
        ls_hitbox = pygame.Rect(Lx, Ly, 32, 32)     # Xwing's lesers hitbox
        tl_hitbox = pygame.Rect(Tlx, Tly, 32, 32)   # Tie fighter hitbox
        tf_hitbox = pygame.Rect(Tx, Ty, 64, 64)     # Tie fighter lesers hitbox



        # collision check between enemy and player
        if tl_hitbox.colliderect(xw_hitbox):
            """
            :arguments:
                :exSFX: sound effect
                :score: Decrease when hitten
                :t_shooting: sets shooting to falase

            """
            exSFX = mixer.Sound('res/sfx/explosion.wav')
            exSFX.play()
            Tly = 100
            score -= 1
            t_shooting = False

        # collision check between player and enemy
        if ls_hitbox.colliderect(tf_hitbox):
            """
            :arguments:
                :exSFX: sound effect
                :score: Increase when hitten
                :t_shooting: sets shooting to falase

            """
            exSFX = mixer.Sound('res/sfx/explosion.wav')
            exSFX.play()
            Ly = 480
            score += 1
            shooting = False
            spwan()

        # Tie figher summoners
        tie_fighter(Tx, Ty)  
        Tl_movement()
        tie_fighter_movement(Tx, Ty)
        TiAI(Tly, Tly)

        # Xwing summoners
        x_wing(Xx, Xy)
        lMovement()
        XxMovement()

        # Display score
        show_score(Sx, Sy, score)

        # Display cordinates
        display_cordinates(Xx, Xy)
        pygame.display.update() # Honestly, IDK WHAT THIS DOES LOL


menu_loop()
game_loop()