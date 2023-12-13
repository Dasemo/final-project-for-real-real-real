import pyxel
from properties import Properties

class Shellcreeper(Properties): # This class defines all the movements for the shellcreeper and its behavior in the game. 
    
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.direction = 1  # 1 for right, -1 for left
        self.sprite_x = 0
        self.sprite_y = 32
        self.vel_y = 0
        self.speed = 1
    def update(self):
        # Update frame for walking animation
        self.sprite_x = (self.sprite_x + 16) % 32
        self.x += self.speed * self.direction

        if self.x < 0:
            self.x == 255
        if self.x >= 230.0 and self.y >= 220.0:
            self.x = 50  
            self.y = 32
        if self.x > pyxel.width:
            self.x = 0 
        
    def fall(self):
        if 88 <= self.x <= 1000 and 57 <= self.y <= 106 :
            self.vel_y = 2.5
            self.y += self.vel_y
        if 192 <= self.x <= 1000 and 106 <= self.y <= 169:
            self.vel_y = 2.5
            self.y += self.vel_y
        if 88 <= self.x <= 150 and 169 <= self.y <= 226:
            self.vel_y = 2.5
            self.y += self.vel_y
        if 49 <= self.x <= 80 and 32 <= self.y <= 57.5:
            self.vel_y = 2.5
            self.y += self.vel_y


class Sidestepper(Properties):
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 1  # 1 for right, -1 for left
        self.sprite_x = 0
        self.sprite_y = 48

    def update(self):
        # Sidestepper movement.
        self.x += self.speed * self.direction

        # Update frame for walking animation
        self.sprite_x = (self.sprite_x + 16) % 32

        if self.x < 0:
            self.x == 255
        if self.x > pyxel.width:
            self.x = 0

    def draw(self):
        # Function for the drawing of the sprite.
        pyxel.blt(self.x, self.y - 3, 0, self.sprite_x, self.sprite_y, 16 * self.direction, 16, 0)


class Fighter(Properties):
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 1  # 1 for right, -1 for left
        self.width = 16
        self.height = 16

    def update(self):
        # Fighter fly movement.
        self.x += self.speed * self.direction

        if self.x < 0:
            self.x == 255
        if self.x > pyxel.width:
            self.x = 0

    def draw(self):
        # Function for the drawing of the sprite.
        pyxel.blt(self.x, self.y - 3, 0, 0, 64, self.width * self.direction, self.height, 0)
