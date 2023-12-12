import pyxel

class CollisionObject:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class Properties:
    def __init__(self, x, y, u, v, w, h, sprite=0):
        self.__x = x
        self.__y = y
        self.__u = u
        self.__v = v
        self.__w = w
        self.__h = h
        self.sprite = sprite

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

class Player(Properties):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.sprite = (0, 0, 0, 16, 22)
        self.lives = 3
        self.vel_y = 0
        self.jumping = False
        
    def move(self, direction: str, size: int):
        xSize = self.sprite[3]
        if direction.lower() == 'right' and self.x < size - xSize:
            self.x = self.x + 4
        elif direction.lower() == 'left' and self.x > 0:
            self.x -= 4
        elif self.x == 0 and direction.lower() == 'left':
            self.x = 255
        elif self.x == size - xSize and direction.lower() == 'right':
            self.x = 0
        

    def jump(self):
        if not self.jumping:
            self.vel_y = -8
            self.jumping = True

    def update(self, map_elements):
        if not self.ground():
            self.vel_y += 0.5

        self.y += self.vel_y

        if self.ground():
            self.y = min(self.y, self.groundHeight())
            self.vel_y = 0
            self.jumping = False
        else:
            self.jumping = True

        self.push_back(map_elements)
            
            

    def detect_collision(self, map_elements):
        player_left = self.x
        player_right = self.x + self.sprite[3]
        player_top = self.y
        player_bottom = self.y + self.sprite[4]

        for element in map_elements:
            x, y, w, h = element[0], element[1], element[3], element[4]

            if (
                player_left < x + w and
                player_right > x and
                player_top < y + h and
                player_bottom > y
            ):
                return True

        return False

    def push_back(self, map_elements):
        collision = self.detect_collision(map_elements)

        if collision:
            self.vel_y = 0
            self.jumping = False

            # Move player up slightly to resolve collision
            self.y -= 3



    def ground(self):
        return self.y == self.groundHeight()

    def groundHeight(self):
        return 218

# Clase para el mapa
import pyxel

class Map:
    
    def __init__(self):
        self.drawing = [
            [0, 240, 0, 48, 104, 16, 16],  # Bloque de brick
            [0, 0, 0, 64, 104, 8, 8],  # Bloque azul
            [0, 0, 0, 80, 104, 16, 16], #Tubería recta
            [0, 0, 0, 0, 104, 16, 16],  #POW
            [0, 0, 0, 128, 104, 16, 16],    #Tuberia2
            [0, 0, 0, 110, 104, 16, 16],    #Tuberia3
        ]

    def draw(self):
        for i in range(len(self.drawing)):
            a = 0
            for e in range(33):
                pyxel.blt(a, self.drawing[0][1], self.drawing[0][2], self.drawing[0][3], self.drawing[0][4], self.drawing[0][5], self.drawing[0][6])# suelo
                a = a + 8
            a = 0
            for xd in range(11):
                pyxel.blt(a, self.drawing[1][1] + 184, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])#primer nivel izquierda
                a = a + 8
            a = 255
            for xd in range(12):
                pyxel.blt(a, self.drawing[1][1] + 184, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])#primer nivel derecha
                a = a - 8
            pyxel.blt(239, 223, self.drawing[2][2], self.drawing[2][3], self.drawing[2][4], self.drawing[2][5], self.drawing[2][6]) #Tuberia derecha
            pyxel.blt(0, 223, self.drawing[2][2], self.drawing[2][3], self.drawing[2][4], -self.drawing[2][5], self.drawing[2][6])  #Tuberia izquierda
            pyxel.blt(120, 184, self.drawing[3][2], self.drawing[3][3], self.drawing[3][4], self.drawing[3][5], self.drawing[3][6])  #POW
            a = 0
            for xd in range(4):
                pyxel.blt(a, self.drawing[1][1] + 136, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6]) # segundo nivel izquierda
                a = a + 8
            a = 255
            for xd in range(5):
                pyxel.blt(a, self.drawing[1][1] + 136, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6]) #segundo nivel izquierda
                a = a - 8
            a = 0
            for xd in range(11):
                pyxel.blt(a, self.drawing[1][1] + 72, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])#primer nivel izquierda
                a = a + 8
            a = 255
            for xd in range(12):
                pyxel.blt(a, self.drawing[1][1] + 72, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])#primer nivel izquierda
                a = a - 8
            a = 64
            for xd in range(16):
                pyxel.blt(a, self.drawing[1][1] + 120, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])#primer nivel izquierda
                a = a + 8
            
            pyxel.blt(self.drawing[4][0] + 16, self.drawing[4][1] + 48, self.drawing[4][2], self.drawing[4][3], self.drawing[4][4], -self.drawing[4][5], self.drawing[4][6])#Tuberia2 izq
            pyxel.blt(self.drawing[2][0], self.drawing[2][1] + 47, self.drawing[2][2], self.drawing[2][3], self.drawing[2][4], -self.drawing[2][5], self.drawing[2][6])#Tuberia1 izq
            pyxel.blt(self.drawing[5][0] + 18, self.drawing[5][1] + 32, self.drawing[5][2], self.drawing[5][3], self.drawing[5][4], -self.drawing[5][5], self.drawing[5][6])#Tuberia3 izq
            pyxel.blt(self.drawing[2][0] + 34, self.drawing[2][1] + 32, self.drawing[2][2], self.drawing[2][3], self.drawing[2][4], -self.drawing[2][5], self.drawing[2][6])#Tuberia1(2) izq
            
            pyxel.blt(self.drawing[4][0] + 255 - 32, self.drawing[4][1] + 48, self.drawing[4][2], self.drawing[4][3], self.drawing[4][4], self.drawing[4][5], self.drawing[4][6])#Tuberia2 izq
            pyxel.blt(self.drawing[5][0] + 255 - 34, self.drawing[5][1] + 32, self.drawing[5][2], self.drawing[5][3], self.drawing[5][4], self.drawing[5][5], self.drawing[5][6])#Tuberia3 izq
            pyxel.blt(self.drawing[2][0] + 255 - 50, self.drawing[2][1] + 32, self.drawing[2][2], self.drawing[2][3], self.drawing[2][4], self.drawing[2][5], self.drawing[2][6])#Tuberia1(2) izq
            pyxel.blt(self.drawing[2][0] + 239, self.drawing[2][1] + 47, self.drawing[2][2], self.drawing[2][3], self.drawing[2][4], self.drawing[2][5], self.drawing[2][6])#Tuberia1 izq
            

class App:
    _initialized = False

    def __init__(self):
        self.width = 255
        self.height = 255
        self.map = Map()
        if not App._initialized:
            pyxel.init(self.width, self.height, title="Mario Bros. Classic")
            pyxel.load("assets/ey.pyxres")
            App._initialized = True

        self.player = Player(self.width // 2, 218)
        # Initialize your map class here

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.player.jump()
        elif pyxel.btn(pyxel.KEY_W):
            self.player.jump()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.player.move('right', self.width)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.player.move('left', self.width)
        elif pyxel.btn(pyxel.KEY_A):
            self.player.move('left', self.width)
        elif pyxel.btn(pyxel.KEY_D):
            self.player.move('right', self.width)
            
        self.player.update(self.map.drawing)

    def draw(self):
        pyxel.cls(0)
        self.map.draw()
        # Dibujar el jugador
        pyxel.blt(self.player.x, self.player.y, 0, 0, 10, 16, 22)
        pyxel.blt(60, 20, 0, 8, 0, 8, 8, 0)
        pyxel.blt(70, 20, 0, 8, 0, 8, 8, 0)
        pyxel.blt(80, 20, 0, 8, 0, 8, 8, 0)

# Run the application
app = App()
pyxel.run(app.update, app.draw)
