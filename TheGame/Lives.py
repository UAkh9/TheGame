class Player:
    def __init__(self, max_lives):
        self.max_lives = max_lives
        self.max_lives = max_lives
    
    def life_lose(self):
        if self.lives > 0:
            self.lives -= 1

    def alive(self):
        return self.lives

    def get_lives(self):
        return self.lives

player = Player(max_lives=3)