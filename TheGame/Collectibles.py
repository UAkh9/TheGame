import pygame

WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

class Collect():

    def draw_window():
        WHITE = (255, 255, 255)
        # coin import/Coin size /coin postion as X & Y
        coin_image = pygame.image.load('assets/coin.png')
        coin = pygame.transform.scale(coin_image,(50,60))
        coinx = 350
        coiny = 500
        WIN.blit(coin,(coinx,coiny))

        coin_image = pygame.image.load('assets/coin.png')
        coin = pygame.transform.scale(coin_image,(50,60))
        coinx = 200
        coiny = 300
        WIN.blit(coin,(coinx,coiny))

        coin_image = pygame.image.load('assets/coin.png')
        coin = pygame.transform.scale(coin_image,(50,60))
        coinx = 150
        coiny = 250
        WIN.blit(coin,(coinx,coiny))

        coin_image = pygame.image.load('assets/coin.png')
        coin = pygame.transform.scale(coin_image,(50,60))
        coinx = 70
        coiny = 80
        WIN.blit(coin,(coinx,coiny))

        coin_image = pygame.image.load('assets/coin.png')
        coin = pygame.transform.scale(coin_image,(50,60))
        coinx = 450
        coiny = 250
        WIN.blit(coin,(coinx,coiny))


        # Heart import/Heart size /Heart postion as X & Y
        Heart_image = pygame.image.load('assets/Heart.png')
        Heart = pygame.transform.scale(Heart_image,(50,60))
        Heartx = 10
        Hearty = 10
        WIN.blit(Heart,(Heartx,Hearty))

        Heart_image = pygame.image.load('assets/Heart.png')
        Heart = pygame.transform.scale(Heart_image,(50,60))
        Heartx = 140
        Hearty = 50
        WIN.blit(Heart,(Heartx,Hearty))

    running = True
    while running:

        draw_window()

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()



        



pygame.quit()








