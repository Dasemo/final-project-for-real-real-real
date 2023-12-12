import pyxel
from properties import Properties

class Player(Properties):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.sprite = (0, 0, 0, 16, 22)
        self.lives = 3
        self.vel_y = 0
        self.jumping = False


    def move(self, direction: str, size: int):
        xSize = self.sprite[3]
        if direction.lower() == 'right' and self.x < size - xSize:
            self.x = self.x + 4
        elif direction.lower() == 'left' and self.x > 0:
            self.x -= 4
        elif self.x == 0 and direction.lower() == 'left':
            self.x = 255
        elif self.x == size - xSize and direction.lower() == 'right':
            self.x = 0
        

    def jump(self):
        if not self.jumping:
            self.vel_y = -8
            self.jumping = True
        
        
    def update(self):
        if not self.ground():
            self.vel_y += 0.5

        self.y += self.vel_y
        # Ajusta la lógica de colisión para que Mario no se hunda por debajo del suelo
        if self.ground():
            self.y = min(self.y, self.groundHeight())
            self.vel_y = 0
            self.jumping = False
        else:
            self.jumping = True  # Permite que Mario siga saltando mientras esté en el aire

    def ground(self):
        return self.y == self.groundHeight()

    def groundHeight(self):
        return 218
    def lives(self):
        if self.lives == 0:
            return False
        else:
            return True