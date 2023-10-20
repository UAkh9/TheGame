import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 700, 700
BACKGROUND_COLOR = (255, 255, 255)
SPRITE_COLOR = (0, 0, 0)
SPRITE_SIZE = 50
SPRITE_SPEED = 1

# Creates the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Sprite")

# Initial sprite position
sprite_x = (WIDTH - SPRITE_SIZE) // 2
sprite_y = (HEIGHT - SPRITE_SIZE) // 2

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    y = 50
    isJump = False
    jumpCount = 10
    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and sprite_x > 0:
        sprite_x -= SPRITE_SPEED
    if keys[pygame.K_RIGHT] and sprite_x < WIDTH - SPRITE_SIZE:
        sprite_x += SPRITE_SPEED
    if keys[pygame.K_UP] and sprite_y > 0:
        sprite_y -= SPRITE_SPEED
    if keys[pygame.K_DOWN] and sprite_y < HEIGHT - SPRITE_SIZE:
        sprite_y += SPRITE_SPEED
    #if keys[pygame.K_SPACE]:
       # sprite_x
    isjump = False
   
# Force (v) up and mass m. 
    v = 5
    m = 1
    if isjump == False: 
   
        # if space bar is pressed 
        if keys[pygame.K_SPACE]: 
                  
            # make isjump equal to True 
            isjump = True
               
    if isjump : 
        # calculate force (F). F = 1 / 2 * mass * velocity ^ 2. 
        F =(1 / 2)*m*(v**2) 
           
        # change in the y co-ordinate 
        y-= F 
           
        # decreasing velocity while going up and become negative while coming down 
        v = v-1
           
        # object reached its maximum height 
        if v<0: 
               
            # negative sign is added to counter negative velocity 
            m =-1
   
        # objected reaches its original state 
        if v ==-6: 
   
            # making isjump equal to false  
            isjump = False
  
     
            # setting original values to v and m 
            v = 5
            m = 1
    
     


    # Clears the screen
    window.fill(BACKGROUND_COLOR)

    # Rectangle Sprite
    pygame.draw.rect(window, SPRITE_COLOR, (sprite_x, sprite_y, SPRITE_SIZE, SPRITE_SIZE))

    # Updates the dislpay 
    pygame.display.update()

# Allows user to exit
pygame.quit()
sys.exit()
