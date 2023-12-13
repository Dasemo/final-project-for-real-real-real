import pyxel
from Player import Player, player_properties
from enemies import Shellcreeper, Fighter, Sidestepper
from map import Map
from collisions import ramp1_l, ramp1_r, ramp2_l, ramp2_r, ramp3, ramp4_l, ramp4_r, suelo, shellcreeper_properties, pow

class App:
    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h
        
        pyxel.init(self.width, self.height, title="Mario Bros. Classic")
        pyxel.load("assets/ey.pyxres")

        self.plane = Player(self.width // 2, 218)   #Creates Mario
        self.shellcreeper = Shellcreeper(50, 33, 1) #Creates an enemy
        self.map = Map()    #Imports the map
    def update(self):       
        #These are created to ensure the collision works
        ground = suelo['y'] 
        prev_player_x, prev_player_y = player_properties["x"], player_properties["y"]
        
        #These conditions ensure what keys are used for each movement
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.plane.jump()
            self.direction = 0
        elif pyxel.btn(pyxel.KEY_W):
            self.plane.jump()
            self.direction = 0
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.plane.move('right', self.width)
            self.plane.direction = 1
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.plane.move('left', self.width)
            self.plane.direction = -1
        elif pyxel.btn(pyxel.KEY_A):
            self.plane.move('left', self.width)
            self.plane.direction = -1
        elif pyxel.btn(pyxel.KEY_D):
            self.plane.move('right', self.width)
            self.plane.direction = 1

        #These are created to ensure the collision works
        prev_player_x, prev_player_y = player_properties["x"], player_properties["y"]
        colliders = [player_properties]
        
        #This loop and conditions are created for Mario to collide with the Map
        for i in range(1):    
            if is_collision(colliders[i], suelo):
                colliders[i]["x"], colliders[i]["y"] = prev_player_x, prev_player_y
                ground = suelo['y']                  
            if is_collision(colliders[i], ramp1_l):
                colliders[i]["x"], colliders[i]["y"] = prev_player_x, prev_player_y
                ground = ramp1_l['y']
            if is_collision(colliders[i], ramp1_r):
                colliders[i]["x"], colliders[i]["y"] = prev_player_x, prev_player_y
                ground = ramp1_r['y']
            if is_collision(colliders[i], ramp2_l):
                colliders[i]["x"], colliders[i]["y"] = prev_player_x, prev_player_y
                ground = ramp2_l['y']
            if is_collision(colliders[i], ramp2_r):
                colliders[i]["x"], colliders[i]["y"] = prev_player_x, prev_player_y
                ground = ramp2_r['y']
            if is_collision(colliders[i], ramp3):
                colliders[i]["x"], colliders[i]["y"] = prev_player_x, prev_player_y
                ground = ramp3['y']
            if is_collision(colliders[i], ramp4_l):
                colliders[i]["x"], colliders[i]["y"] = prev_player_x, prev_player_y
                ground = ramp4_l['y']
            if is_collision(colliders[i], ramp2_r):
                colliders[i]["x"], colliders[i]["y"] = prev_player_x, prev_player_y
                ground = ramp2_r['y']
            if is_collision(colliders[i], ramp4_r):
                colliders[i]["x"], colliders[i]["y"] = prev_player_x, prev_player_y
                ground = ramp4_r['y'] 
            if is_collision(colliders[i], pow):
                colliders[i]["x"], colliders[i]["y"] = prev_player_x, prev_player_y
                ground = pow['y'] 
                
        #Controls Mario's collision with the enemy
        self.plane.enemyCol(shellcreeper_properties)
        #Controls Mario's collision with the platforms
        self.plane.update(ground)
        #Controls shellcreepers' physics
        self.shellcreeper.update()
        self.shellcreeper.fall()

        
    def draw(self): #This function 'draws' the characters of the game
        pyxel.cls(0)
        self.map.draw()
        pyxel.blt(shellcreeper_properties["x"], shellcreeper_properties['y'] - 3, 0, self.shellcreeper.sprite_x, self.shellcreeper.sprite_y, 16 * self.shellcreeper.direction, 16, 0) #Shellcreeperç
        
        #Mario' animations
        if self.plane.direction == 1:
            pyxel.blt(player_properties['x'], player_properties['y'], 0, 0, 10, 16, 22, 0)
        elif self.plane.direction == -1:
            pyxel.blt(player_properties['x'], player_properties['y'], 0, 0, 10, -16, 22, 0)
        elif self.plane.direction == 0:
            pyxel.blt(player_properties['x'], player_properties['y'], 0, 64, 10, 16, 22, 0)
            
        #Mario's lives
        pyxel.blt(30, 10, 0, 4, 0, 13, 8, 0)
        if self.plane.lives >= 2:
            pyxel.blt(42, 10, 0, 4, 0, 13, 8, 0)
        if self.plane.lives == 3:
            pyxel.blt(54, 10, 0, 4, 0, 13, 8, 0)
            
        
        
        
def is_collision(character, platform):  #This function detects the colision
    return (
        character["x"] < platform["x"] + platform["w"]
        and character["x"] + character["w"] > platform["x"]
        and character["y"] < platform["y"] + platform["h"]
        and character["y"] + character["h"] > platform["y"]
    )    
  