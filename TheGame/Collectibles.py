import pygame

WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_window():
    WHITE = (255, 255, 255)
    coin_image = pygame.image.load('assets/coin.png')
    coin = pygame.transform.scale(coin_image,(50,60))
    coinx = 30
    coiny = 50
    WIN.blit(coin,(coinx,coiny))
    

running = True
while running:

    draw_window()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()



        



pygame.quit()








