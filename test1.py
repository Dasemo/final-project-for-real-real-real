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

    def detect_collision(self, map_elements):
        for element in map_elements:
            collision, direction = self.collides_with_element(element)
            if collision:
                return True, direction
        return False, ''

    def collides_with_element(self, element):
        player_right = self.x + self.w
        player_bottom = self.y + self.h
        element_right = element[0] + element[3]
        element_bottom = element[1] + element[4]

        if (
            self.x < element_right and
            player_right > element[0] and
            self.y < element_bottom and
            player_bottom > element[1]
        ):
            overlap_x = min(player_right, element_right) - max(self.x, element[0])
            overlap_y = min(player_bottom, element_bottom) - max(self.y, element[1])

            if overlap_x < overlap_y:
                return True, 'horizontal' if self.x < element[0] else 'horizontal_inv'
            else:
                return True, 'vertical' if self.y < element[1] else 'vertical_inv'

        return False, ''

    def push_back(self, map_elements):
        collision, direction = self.detect_collision(map_elements)
        if collision:
            if direction == 'horizontal':
                sign = -1 if self.dx > 0 else 1
                while collision:
                    self.dx += sign
                    collision, direction = self.detect_collision(map_elements)
                self.jumping = False
            else:
                sign = -1 if self.dy > 0 else 1
                if sign == 1:
                    self.jumping = True
                while collision:
                    self.dy += sign
                    collision, direction = self.detect_collision(map_elements)

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

    def ground(self):
        return self.y == self.groundHeight()

    def groundHeight(self):
        return 218


from map import Map
import pyxel

from map import Map
import pyxel

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

        for element in self.map.drawing:
            pyxel.blt(element[0], element[1], element[2], element[3], element[4], element[5], element[6])

        pyxel.blt(self.player.x, self.player.y, 0, 0, 10, 16, 22)

    def draw(self):
        pyxel.cls(0)

        for element in self.map.drawing:
            pyxel.blt(element[0], element[1], element[2], element[3], element[4], element[5], element[6])

        pyxel.blt(self.player.x, self.player.y, 0, 0, 10, 16, 22)


# Run the application
app = App()
pyxel.run(app.update, app.draw)


