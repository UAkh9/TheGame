import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 700, 700
BACKGROUND_COLOR = (255, 255, 255)
SPRITE_COLOR = (0, 0, 0)
SPRITE_SIZE = 50
SPRITE_SPEED = 3

# Create the game window
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
    if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    # Clear the screen
    window.fill(BACKGROUND_COLOR)

    # Draw the sprite
    pygame.draw.rect(window, SPRITE_COLOR, (sprite_x, sprite_y, SPRITE_SIZE, SPRITE_SIZE))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
