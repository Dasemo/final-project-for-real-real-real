import pyxel

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
        super().__init__(x, y, 0, 0, 16, 22)
        self.lives = 3
        self.vel_y = 0
        self.jumping = False

    def move(self, direction: str, size: int):
        xSize = self.w
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

    def update(self):
        if not self.ground():
            self.vel_y += 0.5

        self.y += self.vel_y

        # Adjust collision logic to prevent Mario from sinking below the ground
        if self.ground():
            self.y = min(self.y, self.groundHeight())
            self.vel_y = 0
            self.jumping = False
        else:
            self.jumping = True

    def ground(self):
        return self.y == self.groundHeight()

    def groundHeight(self):
        return 218

class Enemy(Properties):
    def __init__(self, x, y, speed):
        super().__init__(x, y, 0, 10, 16, 22)
        self.speed = speed

    def move(self):
        self.x += self.speed
        if self.x > pyxel.width:
            self.x = -16

def check_collision(entity1, entity2):
    """
    Check for collision between two rectangular entities.

    Parameters:
    - entity1: An object representing the first entity with properties 'x', 'y', 'w' (width), and 'h' (height).
    - entity2: An object representing the second entity with properties 'x', 'y', 'w' (width), and 'h' (height).

    Returns:
    - True if collision is detected, False otherwise.
    """
    left1, right1, top1, bottom1 = entity1.x, entity1.x + entity1.w, entity1.y, entity1.y + entity1.h
    left2, right2, top2, bottom2 = entity2.x, entity2.x + entity2.w, entity2.y, entity2.y + entity2.h

    # Check for overlap along both axes
    return not (right1 < left2 or left1 > right2 or bottom1 < top2 or top1 > bottom2)

class Map:
    def __init__(self):
        self.drawing = [
            [0, 240, 0, 48, 104, 16, 16],  # Brick block
            [0, 0, 0, 64, 104, 8, 8],  # Blue block
            [0, 0, 0, 80, 104, 16, 16],  # Straight pipe
            [0, 0, 0, 0, 104, 16, 16],  # POW
            [0, 0, 0, 128, 104, 16, 16],  # Pipe2
            [0, 0, 0, 110, 104, 16, 16],  # Pipe3
        ]

    def draw(self):
        for i in range(len(self.drawing)):
            a = 0
            for e in range(33):
                pyxel.blt(a, self.drawing[0][1], self.drawing[0][2], self.drawing[0][3], self.drawing[0][4], self.drawing[0][5], self.drawing[0][6])  # ground
                a = a + 8
            a = 0
            for xd in range(11):
                pyxel.blt(a, self.drawing[1][1] + 184, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])  # first level left
                a = a + 8
            a = 255
            for xd in range(12):
                pyxel.blt(a, self.drawing[1][1] + 184, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])  # first level right
                a = a - 8
            pyxel.blt(239, 223, self.drawing[2][2], self.drawing[2][3], self.drawing[2][4], self.drawing[2][5], self.drawing[2][6])  # Pipe right
            pyxel.blt(0, 223, self.drawing[2][2], self.drawing[2][3], self.drawing[2][4], -self.drawing[2][5], self.drawing[2][6])  # Pipe left
            pyxel.blt(120, 184, self.drawing[3][2], self.drawing[3][3], self.drawing[3][4], self.drawing[3][5], self.drawing[3][6])  # POW
            a = 0
            for xd in range(4):
                pyxel.blt(a, self.drawing[1][1] + 136, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])  # first level left
                a = a + 8
            a = 255
            for xd in range(5):
                pyxel.blt(a, self.drawing[1][1] + 136, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])  # first level left
                a = a - 8
            a = 0
            for xd in range(11):
                pyxel.blt(a, self.drawing[1][1] + 72, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])  # first level left
                a = a + 8
            a = 255
            for xd in range(12):
                pyxel.blt(a, self.drawing[1][1] + 72, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])  # first level left
                a = a - 8
            a = 64
            for xd in range(16):
                pyxel.blt(a, self.drawing[1][1] + 120, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])  # first level left
                a = a + 8

            pyxel.blt(self.drawing[4][0] + 16, self.drawing[4][1] + 48, self.drawing[4][2], self.drawing[4][3], self.drawing[4][4], -self.drawing[4][5], self.drawing[4][6])  # Pipe2 left
            pyxel.blt(self.drawing[2][0], self.drawing[2][1] + 47, self.drawing[2][2], self.drawing[2][3], self.drawing[2][4], -self.drawing[2][5], self.drawing[2][6])  # Pipe1 left
            pyxel.blt(self.drawing[5][0] + 18, self.drawing[5][1] + 32, self.drawing[5][2], self.drawing[5][3], self.drawing[5][4], -self.drawing[5][5], self.drawing[5][6])  # Pipe3 left
            pyxel.blt(self.drawing[2][0] + 34, self.drawing[2][1] + 32, self.drawing[2][2], self.drawing[2][3], self.drawing[2][4], -self.drawing[2][5], self.drawing[2][6])  # Pipe1(2) left

            pyxel.blt(self.drawing[4][0] + 255 - 32, self.drawing[4][1] + 48, self.drawing[4][2], self.drawing[4][3], self.drawing[4][4], self.drawing[4][5], self.drawing[4][6])  # Pipe2 right
            pyxel.blt(self.drawing[5][0] + 255 - 34, self.drawing[5][1] + 32, self.drawing[5][2], self.drawing[5][3], self.drawing[5][4], self.drawing[5][5], self.drawing[5][6])  # Pipe3 right
            pyxel.blt(self.drawing[2][0] + 255 - 50, self.drawing[2][1] + 32, self.drawing[2][2], self.drawing[2][3], self.drawing[2][4], self.drawing[2][5], self.drawing[2][6])  # Pipe1(2) right
            pyxel.blt(self.drawing[2][0] + 239, self.drawing[2][1] + 47, self.drawing[2][2], self.drawing[2][3], self.drawing[2][4], self.drawing[2][5], self.drawing[2][6])  # Pipe1 right

class App:
    _initialized = False

    def __init__(self):
        self.width = 255
        self.height = 255

        # Initialize Pyxel only if it hasn't been initialized before
        if not App._initialized:
            pyxel.init(self.width, self.height, title="Mario Bros. Classic")
            pyxel.load("assets/ey.pyxres")
            App._initialized = True

        # Create an instance of the Player class and assign it to the 'plane' attribute
        self.plane = Player(self.width // 2, 218)
        self.enemy = Enemy(20, 218, speed=1)
        self.mapa = Map()

    # ... (rest of the App class)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.plane.jump()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.plane.move('right', self.width)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.plane.move('left', self.width)

        # Update the plane's state
        self.plane.update()
        # Update the enemy's state
        self.enemy.move()

        # Check for collision with enemy
        if check_collision(self.plane, self.enemy):
            print("Collision! Mario touched the enemy.")

        # Check for collision with each element in the map
        for element in self.mapa.drawing:
            element_properties = {
                "x": element[0],
                "y": element[1],
                "w": element[4],
                "h": element[5]
            }
            if check_collision(self.plane, element_properties):
                print(f"Collision! Mario touched an element at ({element[0]}, {element[1]})")

    # ... (remaining code)


    def draw(self):
        pyxel.cls(0)
        self.mapa.draw()

        # Draw the player
        pyxel.blt(self.plane.x, self.plane.y, 0, 0, 10, 16, 22)

# Run the application
app = App()
pyxel.run(app.update, app.draw)