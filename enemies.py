import pyxel
from properties import Properties

class Shellcreeper(Properties): # This class defines all the movements for the shellcreeper and its behavior in the game. 
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 1  # 1 for right, -1 for left
        self.width = 16
        self.height = 16

    def update(self):
        # Sheelcreeper movement.
        self.x += self.speed * self.direction

        if self.x < 0:
            self.x == 255
        if self.x > pyxel.width:
            self.x = 0

    def draw(self):
        # Function for the drawing of the sprite.
        for xd in range(3):
            pyxel.blt(self.x, self.y - 3, 0, 0, 32, self.width * self.direction, self.height, 0)


class Sidestepper(Properties):
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 1  # 1 for right, -1 for left
        self.width = 16
        self.height = 16

    def update(self):
        # Sidestepper movement.
        self.x += self.speed * self.direction

        if self.x < 0:
            self.x == 255
        if self.x > pyxel.width:
            self.x = 0

    def draw(self):
        # Function for the drawing of the sprite.
        pyxel.blt(self.x, self.y - 3, 0, 0, 48, self.width * self.direction, self.height, 0)
