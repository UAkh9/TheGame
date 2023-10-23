import pygame
import sys

pygame.init()
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image test")

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


BACKGROUND = pygame.image.load("assets/cluodbackground.png")
SCREEN.blit(BACKGROUND, (0, 0))

pygame.display.update()
CLOCK.tick(60)
