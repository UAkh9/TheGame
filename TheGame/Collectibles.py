import pygame
#Collect the collectibles if the player touches it
Player_touched_collectible = Player_rectangle.colliderect(collectible)

#Draw the collectibles 
Collectibles_color = pygame.color(255, 0, 0)
Collectibles_size_in_pixels = 20
collectible_rectangle = pygame.rect (
    collectibles_x,
    collectible_y,
    collectible_size_in_pixels,
    collectible_size_in_pixels)
pygame.draw.rect (
    screen,
    Collectible_color,
    collectible_rect)