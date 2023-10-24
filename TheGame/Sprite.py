#Sprite
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 700
BACKGROUND_COLOR = (255, 255, 255)
SPRITE_COLOR = (0, 0, 0)
SPRITE_SIZE = 50
SPRITE_SPEED = 0.95
JUMP_HEIGHT = 6
GRAVITY = 1

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Sprite")

# Initial sprite position and state
sprite_x = (WIDTH - SPRITE_SIZE) // 9
sprite_y = (HEIGHT - SPRITE_SIZE) // 5
is_jumping = False
jump_count = 0  
max_jump_count = 7  
sprite_y = 0  
space_pressed = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and sprite_x > 0:
        sprite_x -= SPRITE_SPEED
    if keys[pygame.K_RIGHT] and sprite_x < WIDTH - SPRITE_SIZE:
        sprite_x += SPRITE_SPEED

    # New Jumping Mechanism which should only allow user to jump and not continuously float
    if is_jumping:
        if jump_count >= -max_jump_count:
            sprite_y -= (jump_count ** 2) * 0.5
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 0
    else:
        if keys[pygame.K_SPACE] and not is_jumping and not space_pressed:
            is_jumping = True
            jump_count = max_jump_count
            space_pressed = True
        elif not keys[pygame.K_SPACE]:
            space_pressed = False

    # Apply gravity
    if sprite_y < HEIGHT - SPRITE_SIZE:
        sprite_y += GRAVITY
    
    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the sprite
    pygame.draw.rect(screen, SPRITE_COLOR, (sprite_x, sprite_y, SPRITE_SIZE, SPRITE_SIZE))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
