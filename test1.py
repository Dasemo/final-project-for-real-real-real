import pyxel
import time
player_properties = {"x": 218,"y": 218,"w": 8,"h": 16,}
shellcreeper_properties = {"x": 16,"y": 59,"w": 8,"h": 16}
suelo = {"x": 0,"y": 218,"w": 255,"h": 1}
ramp1_l = {"x": 0,"y": 184-22,"w": 88,"h": 8}
ramp1_r = {"x": 167, "y": 184-22, "w": 88, "h": 8}
ramp2_l = {"x": 0,"y": 136-22,"w": 32, "h": 8}
ramp2_r = {"x": 223, "y": 136-22, "w": 32, "h": 8}
ramp3 = {"x": 64, "y": 120-22, "w":128, "h": 8}
ramp4_l = {"x": 0, "y": 72-22, "w": 88, "h": 8}
ramp4_r = {"x": 167, "y": 72-22, "w": 88, "h": 8}


suelo = {"x": 0,"y": 218,"w": 255,"h": 1}
ramp1_l = {"x": 0,"y": 184-22,"w": 88,"h": 8}
ramp1_r = {"x": 167, "y": 184-22, "w": 88, "h": 8}
ramp2_l = {"x": 0,"y": 136-22,"w": 32, "h": 8}
ramp2_r = {"x": 223, "y": 136-22, "w": 32, "h": 8}
ramp3 = {"x": 64, "y": 120-22, "w":128, "h": 8}
ramp4_l = {"x": 0, "y": 72-22, "w": 88, "h": 8}
ramp4_r = {"x": 167, "y": 72-22, "w": 88, "h": 8}

ground = suelo['y']
class Properties:
    def __init__(self, x, y, u, v, w, h, sprite=(0, 0, 0, 16, 22)):
        self.__x = x
        self.__y = y
        self.__u = u
        self.__v = v
        self.__w = w
        self.__h = h
        self.sprite = sprite

    # Resto del código de la clase Properties


    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def u(self):
        return self.__u

    @property
    def v(self):
        return self.__v

    @property
    def w(self):
        return self.__w

    @property
    def h(self):
        return self.__h

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        if y < 0:
            self.__y = 0
        else:
            self.__y = y

    @u.setter
    def u(self, u):
        if type(u) is not int:
            raise TypeError("u must be an integer")
        elif u > pyxel.width:
            self.__u = pyxel.width
        elif u < 0:
            self.__u = 0
        else:
            self.__u = u

    @v.setter
    def v(self, v):
        if type(v) is not int:
            raise TypeError("v must be an integer")
        elif v > pyxel.height:
            self.__v = pyxel.height
        elif v < 0:
            self.__v = 0
        else:
            self.__v = v

    @w.setter
    def w(self, w):
        if type(w) is not int:
            raise TypeError("w must be an integer")
        elif w > pyxel.width:
            self.__w = pyxel.width
        elif w < -pyxel.width:
            self.__w = -w
        else:
            self.__w = w

    @h.setter
    def h(self, h):
        if type(h) is not int:
            raise TypeError("h must be an integer")
        elif h > pyxel.height:
            self.__h = pyxel.height
        elif h < -pyxel.height:
            self.__h = -h
        else:
            self.__h = h
            
            
            
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
            self.vel_y = 0
            self.jumping = False
            player_properties['y'] = newground 


    def lives(self):
        if self.lives == 0:
            return False
        else:
            return True
        
      
from map import Map    
    
class Shellcreeper(Properties): # This class defines all the movements for the shellcreeper and its behavior in the game. 
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 1  # 1 for right, -1 for left
        self.sprite_x = 0
        self.sprite_y = 32
        self.vel_y = 0

    def update(self):
        # Sheelcreeper movement
        
        # Update frame for walking animation
        self.sprite_x = (self.sprite_x + 16) % 32
        self.x += self.speed * self.direction

        if self.x < 0:
            self.x == 255
        if self.x > pyxel.width:
            self.x = 0   
            self.x += self.speed * self.direction
        print(self.y)
        
    def fall(self):
        if 88 <= self.x <= 1000 and 59 <= self.y <= 106 :
            self.vel_y = 2.5
            self.y += self.vel_y
        if 192 <= self.x <= 1000 and 106 <= self.y <= 120:
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
        
app = App(255, 255)
pyxel.run(app.update, app.draw)