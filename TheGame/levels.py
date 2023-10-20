import pygame

pygame.init()

Screen_Width = 640
Screen_Height = 460
Lower_Margin = 340
Side_Margin = 340


Screen = pygame.display.set_mode((Screen_Width + Side_Margin, Screen_Height + Lower_Margin ))
pygame.display.set_caption("Level Editor")

scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1.5
Screen.fill((255,225,225))


    
#Usman has fixed this code it should now be able to close the window when u click the X  
running = True
while running:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

       
                
   
            
pygame.display.update()
pygame.quit()




