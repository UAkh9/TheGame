import pygame

SCREEN = pygame.display.set_mode ((800, 600))

coinimage = pygame.image.load('coin.jpg')
coinx = 370
coiny = 480

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False





