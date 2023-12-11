import pyxel
from map import Map

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
            self.x = size - xSize
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

        # Adjust the collision logic to prevent Mario from sinking below the ground
        if self.ground():
            self.y = min(self.y, self.groundHeight())
            self.vel_y = 0
            self.jumping = False
        else:
            self.jumping = True  # Allows Mario to keep jumping while in the air

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
            self.x = -16  # Reset the position when the enemy goes off-screen

class App:
    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h

        pyxel.init(self.width, self.height, title="Mario Bros. Classic")
        pyxel.load("assets/ey.pyxres")

        self.plane = Player(self.width // 2, 218)
        self.enemy = Enemy(20, 218, speed=1)
        self.mapa = Map()

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
        if self.check_collision(self.plane, self.enemy):
            print("Collision! Mario touched the enemy.")

    def check_collision(self, obj1, obj2):
        return (
            obj1.x < obj2.x + obj2.w and
            obj1.x + obj1.w > obj2.x and
            obj1.y < obj2.y + obj2.h and
            obj1.y + obj1.h > obj2.y
        )

    def draw(self):
        pyxel.cls(0)
        self.mapa.draw()

        # Draw the enemy
        pyxel.blt(self.enemy.x, self.enemy.y, 0, 0, 10, 16, 22, 0)

        # Draw the player
        pyxel.blt(self.plane.x, self.plane.y, 0, 0, 10, 16, 22, 0)

# Run the application
app = App(255, 255)
pyxel.run(app.update, app.draw)
