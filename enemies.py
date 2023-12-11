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

        if self.x < 0:
            self.x == 255
        if self.x > pyxel.width:
            self.x = 0

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 32, self.width * self.direction, self.height, 0)


class Sidestepper(Properties):
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

        if self.x > 0:
            self.x == self.x + self.width > pyxel.width
        if self.x == self.x + self.width > pyxel.width:
            self.x = 0

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 1, 32, self.width * self.direction, self.height, 0)
