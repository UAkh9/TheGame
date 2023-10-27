import pygame

#Player class 
class Player:

    #Constructor Method For Lives
    def __init__(self, max_lives):
    
        #Sets the max amount of lives for the character
        self.max_lives = max_lives
        self.lives = max_lives
    
    #Checks if player lose lives
    def life_lose(self):
    
        #Checks if player has any lives left
        if self.lives > 0:
        
            #Checks if player loses a life by 1
            self.lives -= 1

    #Checks if player is alive
    def alive(self):
    
        #Returns how many lives are left
        return self.lives

    #Checks how many lives are left
    def get_lives(self):
        return self.lives

#Sets the amount of lives the player has
player = Player(max_lives=3)
