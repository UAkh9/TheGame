import pygame
import sys



# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg_img = pygame.image.load("/assets/Sky_Background.png")
greenbackground_img = pygame.image.load("/assets/greengrass.jpg")



running = True
while running:

    screen.blit(bg_img,(0, 0))
    screen.blit(greenbackground_img,(0, 530))
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()




# Quit the game
pygame.quit()
sys.exit()

