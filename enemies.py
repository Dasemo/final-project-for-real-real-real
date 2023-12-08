from properties import Properties

class Shellcreeper:
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
        self.dx = self.direction
        self.x += 1
        if self.direction < 0:
            self.x = 255
    