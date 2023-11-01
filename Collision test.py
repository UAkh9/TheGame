import pygame
import sys

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def is_colliding(self, other):
        return (self.x < other.x + other.width and
                self.x + self.width > other.x and
                self.y < other.y + other.height and
                self.y + self.height > other.y)

pygame.init()

WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
SPRITE_COLOR = (0, 0, 0)
SPRITE_SIZE = 50
SPRITE_SPEED = 3
JUMP_HEIGHT = 4
GRAVITY = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Sprite")

# Initial sprite position and state
sprite_x = (WIDTH - SPRITE_SIZE) // 9
sprite_y = (HEIGHT - SPRITE_SIZE) // 5
is_jumping = False
jump_count = 0  
max_jump_count = 7 
space_pressed = False
bg_img = pygame.image.load("assets/Sky_Background.png")
greenbackground_img = pygame.image.load("assets/greengrass.jpg")

ground = Rectangle(0, 330, 40, 70)
plat1 = Rectangle(200, 330, 40, 70)

# Game loop
running = True
while running:
    screen.blit(bg_img, (0, 0))
    screen.blit(greenbackground_img, (0, 530))
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
            sprite_y -= (jump_count ** 2) * 1
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

    # Apply gravity and check for ground collision
    if sprite_y < HEIGHT - SPRITE_SIZE:
        sprite_y += GRAVITY
    elif sprite_y > HEIGHT - SPRITE_SIZE:
        sprite_y = HEIGHT - SPRITE_SIZE

    if ground.is_colliding(Rectangle(sprite_x, sprite_y, SPRITE_SIZE, SPRITE_SIZE)):
        sprite_y = ground.y - SPRITE_SIZE
    
    if plat1.is_colliding(Rectangle(sprite_x, sprite_y, SPRITE_SIZE, SPRITE_SIZE)):
        sprite_y = ground.y - SPRITE_SIZE

    # Check for collision
    if ground.is_colliding(Rectangle(sprite_x, sprite_y, SPRITE_SIZE, SPRITE_SIZE)):
        is_jumping = False
        jump_count = 0
    
    if plat1.is_colliding(Rectangle(sprite_x, sprite_y, SPRITE_SIZE, SPRITE_SIZE)):
        is_jumping = False
        jump_count = 0

    # Draw the sprite and ground
    pygame.draw.rect(screen, SPRITE_COLOR, (sprite_x, sprite_y, SPRITE_SIZE, SPRITE_SIZE))
    pygame.draw.rect(screen, (203, 100, 105), (ground.x, ground.y, ground.width, ground.height))
    pygame.draw.rect(screen, (203, 100, 105), (plat1.x, plat1.y, plat1.width, plat1.height))

    pygame.display.update()

# Done! Time to quit.
pygame.quit()
sys.exit()
