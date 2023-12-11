import pyxel
from properties import Properties

class Shellcreeper(Properties):
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 1  # 1 for right, -1 for left
        self.width = 16
        self.height = 16

    def update(self):
        # Move sidestepper
        self.x += self.speed * self.direction

        # Check for collisions with walls and change direction
        if self.x < 0 or self.x + self.width > pyxel.width:
            self.direction *= -1

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 2, 2, self.width * self.direction, self.height, 0)


class Sidestepper(Properties):
    def __init__(self, x, y, is_falling):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.direction = -1
        self.is_falling = False
        self.is_alive = True
        self.is_mad = False
    
    def update(self):
        self.x += 1
        if self.x >= 255 or self.x < 0:
            self.x = (self.x + 255) % 255
            self.direction *= -1