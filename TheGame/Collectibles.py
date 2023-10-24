import pygame

WIN = pygame.display.set_mode ((800, 600))
WIDTH = 800
HEIGHT = 600


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False

coin_image = pygame.image.load('Coin.jpg')
coinx = 370
coiny = 480          

def draw_window():
    WIN.blit(coin_image,(300,100))
    pygame.display.update()

pygame.quit()








