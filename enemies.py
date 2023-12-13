import pyxel
from collisions import shellcreeper_properties
from properties import Properties
class Shellcreeper(Properties): # This class defines all the movements of the shellcreeper and its behavior in the game
    def __init__(self, x, y, speed):
        shellcreeper_properties['x'] = x
        shellcreeper_properties['y'] = y
        self.direction = 1  # 1 for right, -1 for left
        self.sprite_x = 0
        self.sprite_y = 32
        self.vel_y = 0
        self.speed = .7
        self.counter = 1
        
    def update(self):   #Controls the sellcreepers animations and how he moves around the map
        
        #Controls the animation
        self.counter = self.counter + 1
        if self.counter % 4:
            self.sprite_x = (self.sprite_x + 16) % 32
        
        #Controls how he moves around the map
        shellcreeper_properties['x'] += self.speed * self.direction
        if shellcreeper_properties['x'] < 0:
            shellcreeper_properties['x'] == 255
        if shellcreeper_properties['x'] >= 230.0 and shellcreeper_properties['y'] >= 220.0:
            shellcreeper_properties['x'] = 50  
            shellcreeper_properties['y'] = 32
        if shellcreeper_properties['x'] > pyxel.width:
            shellcreeper_properties['x'] = 0   
            



    def fall(self): #This function controls how he moves around the map too
        if 88 <= shellcreeper_properties['x'] <= 1000 and 57 <= shellcreeper_properties['y'] <= 105 :
            self.vel_y = 2.5
            shellcreeper_properties['y'] += self.vel_y
        if 192 <= shellcreeper_properties['x'] <= 1000 and 105 <= shellcreeper_properties['y'] <= 169:
            self.vel_y = 2.5
            shellcreeper_properties['y'] += self.vel_y
        if 88 <= shellcreeper_properties['x'] <= 150 and 169 <= shellcreeper_properties['y'] <= 226:
            self.vel_y = 2.5
            shellcreeper_properties['y'] += self.vel_y
        if 49 <= shellcreeper_properties['x'] <= 80 and 32 <= shellcreeper_properties['y'] <= 57.5:
            self.vel_y = 2.5
            shellcreeper_properties['y'] += self.vel_y


class Sidestepper(Properties):
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 1  # 1 for right, -1 for left
        self.sprite_x = 0
        self.sprite_y = 48

    def update(self):
        # Sidestepper movement
        self.x += self.speed * self.direction

        # Sidestepper animation
        self.sprite_x = (self.sprite_x + 16) % 32

        if self.x < 0:
            self.x == 255
        if self.x > pyxel.width:
            self.x = 0



class Fighter(Properties):
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 1  # 1 for right, -1 for left
        self.width = 16
        self.height = 16

    def update(self):
        # Fighter fly movement
        self.x += self.speed * self.direction

        if self.x < 0:
            self.x == 255
        if self.x > pyxel.width:
            self.x = 0

