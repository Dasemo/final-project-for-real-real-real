

from properties import Properties
from collisions import player_properties, shellcreeper_properties

class Player(Properties):
    def __init__(self, x: int, y: int):
        player_properties["x"] = x
        player_properties['y'] = y
        self.sprite = (0, 0, 0, 16, 22, 0)
        self.lives = 3
        self.vel_y = 0
        self.jumping = False
        self.direction = 1


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
            self.direction = 0
        
    def enemyCol(self, enemy):
        if is_collision(player_properties, shellcreeper_properties):
            player_properties["x"] = 123
            player_properties['y'] = 0
            self.lives = self.lives - 1
            print(self.lives)
            if self.lives == 0:
                quit()
            
        
    def update(self, newground: int):
        
        player_properties['y'] += self.vel_y
        if player_properties['y'] != newground:
            self.vel_y += 0.5
            self.jumping = True
        if (abs(player_properties['y'] - newground) < 7):
            self.vel_y = 0
            self.jumping = False
            player_properties['y'] = newground
            
def is_collision(character, platform):
    # Rectangle collision detection
    return (
        character["x"] < platform["x"] + platform["w"]
        and character["x"] + character["w"] > platform["x"]
        and character["y"] < platform["y"] + platform["h"]
        and character["y"] + character["h"] > platform["y"]
    )   