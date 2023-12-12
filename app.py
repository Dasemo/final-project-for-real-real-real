import pyxel
from Player import Player, player_properties
from enemies import Shellcreeper, Fighter, Sidestepper
from map import Map
from collisions import ramp1_l, ramp1_r, ramp2_l, ramp2_r, ramp3, ramp4_l, ramp4_r, suelo

class App:
    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h
        
        pyxel.init(self.width, self.height, title="Mario Bros. Classic")
        pyxel.load("assets/ey.pyxres")

        self.plane = Player(self.width // 2, 218)
        self.shellcreeper = Shellcreeper(16, 59, 1)
        self.sidestepper = Sidestepper(100, 60, 1)
        self.fighter = Fighter(120, 59, 1)
        self.map = Map()


    def update(self):
        ground = suelo['y'] 
        prev_player_x, prev_player_y = player_properties["x"], player_properties["y"]
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.plane.jump()
        elif pyxel.btn(pyxel.KEY_W):
            self.plane.jump()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.plane.move('right', self.width)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.plane.move('left', self.width)
        elif pyxel.btn(pyxel.KEY_A):
            self.plane.move('left', self.width)
        elif pyxel.btn(pyxel.KEY_D):
            self.plane.move('right', self.width)
            
        prev_player_x, prev_player_y = player_properties["x"], player_properties["y"]
        colliders = [player_properties,]
        
        for i in range(1):    
            if is_collision(colliders[i], suelo):
                colliders[i]["x"], colliders[i]["y"] = prev_player_x, prev_player_y
                ground = suelo['y']                  
                #print(ground)
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
        #print(ground)
        self.plane.update(ground)
        self.shellcreeper.update()
        self.shellcreeper.fall()
        self.sidestepper.update()
        self.fighter.update()
        
    def draw(self):
        pyxel.cls(0)
        self.map.draw()
        pyxel.blt(self.shellcreeper.x, self.shellcreeper.y - 3, 0, self.shellcreeper.sprite_x, self.shellcreeper.sprite_y, 16 * self.shellcreeper.direction, 16, 0)
        self.sidestepper.draw()
        self.fighter.draw()
        pyxel.blt(player_properties['x'], player_properties['y'], 0, 0, 10, 16, 22)
        
def is_collision(character, platform):
    # Rectangle collision detection
    return (
        character["x"] < platform["x"] + platform["w"]
        and character["x"] + character["w"] > platform["x"]
        and character["y"] < platform["y"] + platform["h"]
        and character["y"] + character["h"] > platform["y"]
    )         
        