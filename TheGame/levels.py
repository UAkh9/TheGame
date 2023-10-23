
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
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player_velocity = -15  # Jump by setting a negative velocity

    # Update player position
    player_y += player_velocity
    player_velocity += GRAVITY

    # Keep the player within the screen bounds
    if player_y >= HEIGHT - PLAYER_HEIGHT:
        player_y = HEIGHT - PLAYER_HEIGHT
        player_velocity = 0

    # creating new  new obstacles
    if random.randint(1, 100) < 10:
        spawn_obstacle()

    # Update obstacle positions and remove if they go off-screen
    for obstacle in obstacles:
        obstacle[0] -= SPEED

    obstacles = [obstacle for obstacle in obstacles if obstacle[0] > -OBSTACLE_WIDTH]

    #  this helps us Check for collisions
    for obstacle in obstacles:
        if (
            player_x < obstacle[0] + OBSTACLE_WIDTH
            and player_x + PLAYER_WIDTH > obstacle[0]
            and player_y < obstacle[1] + OBSTACLE_HEIGHT
            and player_y + PLAYER_HEIGHT > obstacle[1]
        ):
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    

    # Draw the obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle[0], obstacle[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

    # Update the display
    pygame.display.update()

    # Increase the score
    score += 1

    # Set the frame rate
    clock.tick(30)

# Game over
print("Game Over. Your Score:", score)

# Quit Pygame
pygame.quit()







