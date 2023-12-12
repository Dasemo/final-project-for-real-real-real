import pyxel
from properties import Properties

player_properties = {"x": 218,"y": 218,"w": 8,"h": 16,}

class Player(Properties):
    def __init__(self, x: int, y: int):
        player_properties["x"] = x
        player_properties['y'] = y
        self.sprite = (0, 0, 0, 16, 22)
        self.lives = 3
        self.vel_y = 0
        self.jumping = False


    def move(self, direction: str, size: int):
        xSize = self.sprite[3]
        if direction.lower() == 'right' and player_properties["x"] < size - xSize:
            player_properties["x"] += 4
        elif direction.lower() == 'left' and player_properties["x"] > 0:
            player_properties["x"] -= 4
        elif player_properties["x"] == 0 and direction.lower() == 'left':
            player_properties["x"] = 255
        elif player_properties["x"] == size - xSize and direction.lower() == 'right':
            player_properties["x"] = 0

    def jump(self):
        if self.jumping == False:
            self.vel_y = -8
            self.jumping = True
        
        
    def update(self, newground: int):
        
        player_properties['y'] += self.vel_y
        if player_properties['y'] != newground:
            self.vel_y += 0.5
            self.jumping = True
        if (abs(player_properties['y'] - newground) < 7):
            print(newground,player_properties['y'])
            self.vel_y = 0
            self.jumping = False
            player_properties['y'] = newground 


    def lives(self):
        if self.lives == 0:
            return False
        else:
            return True