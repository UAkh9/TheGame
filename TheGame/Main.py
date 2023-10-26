# Simple pygame program - taken from https://realpython.com/pygame-a-primer/
# Adapt from this template

# Import and initialize the pygame library
#Test by Angelo
import pygame
import sys 
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([900, 800])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (360, 150), 55)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
sys.exit()