from properties import Properties

class Shellcreeper(Properties):
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


class Sidestepper(Properties):
    def __init(self, x, y, is_falling):
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