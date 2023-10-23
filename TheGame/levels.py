
import pygame
import random

#  this helps us Initialize Pygame
pygame.init()

#  these settings must be Constants
WIDTH, HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 50
PLAYER_COLOR = (0, 255, 0)
OBSTACLE_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (220, 200, 0)
SPEED = 5
GRAVITY = 1

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Running Obstacle Game")

# Load player image
player_image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
player_image.fill(PLAYER_COLOR)

# Initialize player's position and velocity
player_x, player_y = WIDTH // 4, HEIGHT // 2
player_velocity = 0

# we use this to store obstacles
obstacles = []

#  this Clock is used to control the frame rate
clock = pygame.time.Clock()

#  this Function is used to generate obstacles
def spawn_obstacle():
    obstacle_x = WIDTH
    obstacle_y = random.randint(0, HEIGHT - OBSTACLE_HEIGHT)
    obstacles.append([obstacle_x, obstacle_y])

# Game loop
running = True
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
       
                
   
            
    pygame.display.update()
pygame.quit()







