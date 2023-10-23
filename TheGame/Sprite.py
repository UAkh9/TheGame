import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 700
BACKGROUND_COLOR = (255, 255, 255)
SPRITE_COLOR = (0, 0, 0)
SPRITE_SIZE = 50
SPRITE_SPEED = 0.85
JUMP_HEIGHT = 4
GRAVITY = 1

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Sprite")

# Initial sprite position and state
sprite_x = (WIDTH - SPRITE_SIZE) // 9
sprite_y = (HEIGHT - SPRITE_SIZE) // 1
is_jumping = True
jump_count = JUMP_HEIGHT

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

    # Implement jumping mechanism
    #if is_jumping:
    jumping = True
    while jumping:
            if keys[pygame.K_SPACE]:
                #key = keys[pygame.K_SPACE]
                is_jumping = False
            break
    else:
        if jump_count >= -JUMP_HEIGHT:
            sprite_y -= (jump_count ** 2) * 0.5
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = JUMP_HEIGHT

    # Apply gravity
    if sprite_y < HEIGHT - SPRITE_SIZE:
        sprite_y += GRAVITY
    else:
        jump_count = JUMP_HEIGHT

    # Clear the screen
    window.fill(BACKGROUND_COLOR)

    # Draw the sprite
    pygame.draw.rect(window, SPRITE_COLOR, (sprite_x, sprite_y, SPRITE_SIZE, SPRITE_SIZE))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
