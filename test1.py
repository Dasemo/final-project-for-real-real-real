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

    def update(self, map_elements):
        if not self.ground():
            self.vel_y += 0.5

        self.y += self.vel_y

        for element in map_elements:
            element_properties = CollisionObject(element[0], element[1], element[4], element[5])
            if check_collision(self, element_properties):
                self.y = min(self.y, element_properties.y - self.h)
                self.vel_y = 0
                self.jumping = False

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
        if self.x > 255:
            self.x = -16

def check_collision(entity1, entity2):
    left1, right1, top1, bottom1 = entity1.x, entity1.x + entity1.w, entity1.y, entity1.y + entity1.h
    left2, right2, top2, bottom2 = entity2.x, entity2.x + entity2.w, entity2.y, entity2.y + entity2.h

    return not (right1 < left2 or left1 > right2 or bottom1 < top2 or top1 > bottom2)

from map import Map
class App:
    _initialized = False

    def __init__(self):
        self.width = 255
        self.height = 255

        if not App._initialized:
            pyxel.init(self.width, self.height, title="Mario Bros. Classic")
            pyxel.load("assets/ey.pyxres")
            App._initialized = True

        self.player = Player(self.width // 2, 218)
        self.enemy = Enemy(20, 218, speed=1)
        self.map = Map()

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.player.jump()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.player.move('right', self.width)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.player.move('left', self.width)

        self.player.update(self.map.drawing)
        self.enemy.move()

        if check_collision(self.player, self.enemy):
            print("Collision! Mario touched the enemy.")

        for element in self.map.drawing:
            element_properties = CollisionObject(element[0], element[1], element[4], element[5])
            if check_collision(self.player, element_properties):
                print(f"Collision! Mario touched an element at ({element[0]}, {element[1]})")

    def draw(self):
        pyxel.cls(0)
        self.map.draw()
        pyxel.blt(self.player.x, self.player.y, 0, 0, 10, 16, 22)

# Run the application
app = App()
pyxel.run(app.update, app.draw)
