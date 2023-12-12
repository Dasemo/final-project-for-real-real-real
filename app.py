import pyxel
from Player import Player
from map import Map
from enemies import Shellcreeper
from enemies import Sidestepper
from enemies import Fighter

player_properties = {"x": 218,"y": 218,"w": 8,"h": 16,}
suelo = {"x": 0,"y": 218,"w": 255,"h": 1}
ramp1_l = {"x": 0,"y": 184-22,"w": 88,"h": 8}
ramp1_r = {"x": 167, "y": 184-22, "w": 88, "h": 8}
ramp2_l = {"x": 0,"y": 136-22,"w": 32, "h": 8}
ramp2_r = {"x": 223, "y": 136-22, "w": 32, "h": 8}
ramp3 = {"x": 64, "y": 120-22, "w":128, "h": 8}
ramp4_l = {"x": 0, "y": 72-22, "w": 88, "h": 8}
ramp4_r = {"x": 167, "y": 184-22, "w": 88, "h": 8}

class App:
    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h

        pyxel.init(self.width, self.height, title="Mario Bros. Classic")
        pyxel.load("assets/ey.pyxres")

        self.plane = Player(self.width // 2, 218)
        self.shellcreeper = Shellcreeper(80, 60, 1)
        self.sidestepper = Sidestepper(100, 60, 1)
        self.fighter = Fighter(120, 60, 1)
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
            
        if is_collision(player_properties, suelo):
            player_properties["x"], player_properties["y"] = prev_player_x, prev_player_y
            ground = suelo['y']                  
            #print(ground)
        if is_collision(player_properties, ramp1_l):
            player_properties["x"], player_properties["y"] = prev_player_x, prev_player_y
            ground = ramp1_l['y']
        if is_collision(player_properties, ramp1_r):
            player_properties["x"], player_properties["y"] = prev_player_x, prev_player_y
            ground = ramp1_r['y']
        if is_collision(player_properties, ramp2_l):
            player_properties["x"], player_properties["y"] = prev_player_x, prev_player_y
            ground = ramp2_l['y']
        if is_collision(player_properties, ramp2_r):
            player_properties["x"], player_properties["y"] = prev_player_x, prev_player_y
            ground = ramp2_r['y']
        if is_collision(player_properties, ramp3):
            player_properties["x"], player_properties["y"] = prev_player_x, prev_player_y
            ground = ramp3['y']
        if is_collision(player_properties, ramp4_l):
            player_properties["x"], player_properties["y"] = prev_player_x, prev_player_y
            ground = ramp4_l['y']
        if is_collision(player_properties, ramp2_r):
            player_properties["x"], player_properties["y"] = prev_player_x, prev_player_y
            ground = ramp2_r['y']
        if is_collision(player_properties, ramp4_r):
            player_properties["x"], player_properties["y"] = prev_player_x, prev_player_y
            ground = ramp4_r['y']      
        
        self.shellcreeper.update()
        self.sidestepper.update()
        self.fighter.update()
        # Update the plane's state
        self.plane.update(ground)

    def draw(self):
        pyxel.cls(0)
        self.map.draw()
        self.shellcreeper.draw()
        self.sidestepper.draw()
        self.fighter.draw()
        # Dibujar el jugador
        pyxel.blt(player_properties['x'], player_properties['y'], 0, 0, 10, 16, 22)
    
def is_collision(obj1, obj2):
# Rectangle collision detection
    return (
        obj1["x"] < obj2["x"] + obj2["w"]
        and obj1["x"] + obj1["w"] > obj2["x"]
        and obj1["y"] < obj2["y"] + obj2["h"]
        and obj1["y"] + obj1["h"] > obj2["y"]
    )
    