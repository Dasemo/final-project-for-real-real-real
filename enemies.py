import pyxel
from properties import Properties

class Shellcreeper:
    def __init__(self, x, y, is_falling):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.direction = -1
        self.is_falling = False
    
    def update(self):
        self.x += 1
        if self.is_falling:
            self.y += 1
            if self.y > 200:
                self.is_falling = False
                self.y = 200