import pygame

WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

class Collect():

    def draw_window():
        
        # coin import/Coin size /coin postion as X & 
        coin_image = pygame.image.load('assets/coin.png')
        coin = pygame.transform.scale(coin_image,(50,60))
        coinx = 650
        coiny = 300
        WIN.blit(coin,(coinx,coiny))

        coin_image = pygame.image.load('assets/coin.png')
        coin = pygame.transform.scale(coin_image,(50,60))
        coinx = 150
        coiny = 250
        WIN.blit(coin,(coinx,coiny))

        coin_image = pygame.image.load('assets/coin.png')
        coin = pygame.transform.scale(coin_image,(50,60))
        coinx = 350
        coiny = 50
        WIN.blit(coin,(coinx,coiny))

        coin_image = pygame.image.load('assets/coin.png')
        coin = pygame.transform.scale(coin_image,(50,60))
        coinx = 70
        coiny = 100
        WIN.blit(coin,(coinx,coiny))

        coin_image = pygame.image.load('assets/coin.png')
        coin = pygame.transform.scale(coin_image,(50,60))
        coinx = 450
        coiny = 250
        WIN.blit(coin,(coinx,coiny))


        # Heart import/Heart size /Heart postion as X & Y
        Heart_image = pygame.image.load('assets/Heart.png')
        Heart = pygame.transform.scale(Heart_image,(50,60))
        Heartx = 500
        Hearty = 10
        WIN.blit(Heart,(Heartx,Hearty))

        Heart_image = pygame.image.load('assets/Heart.png')
        Heart = pygame.transform.scale(Heart_image,(50,60))
        Heartx = 200
        Hearty = 50
        WIN.blit(Heart,(Heartx,Hearty))
 
 
 






