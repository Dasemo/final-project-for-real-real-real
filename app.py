from Player import Player
from enemies import Shellcreeper
import pyxel

class App:
    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h

        pyxel.init(self.width, self.height, title="Mario Bros. Classic")
        pyxel.load("assets/ey.pyxres")

        self.plane = Player(self.width // 2, 200)

        # Definir el mapa (un ejemplo simple)
        self.map_width = 8
        self.map_height = 1
        self.tile_size = 12
        self.map_data = [
            [3, 4, 2, 3, 4, 5, 2, 2, 2],
        ]

        pyxel.run(self.update, self.draw)

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

    def draw(self):
        pyxel.cls(0)

        # Dibujar el mapa
        for y in range(self.map_height):
            for x in range(self.map_width):
                tile_index = self.map_data[y][x]
                pyxel.blt(x * self.tile_size, y * self.tile_size, 0, 0, tile_index * self.tile_size, self.tile_size, self.tile_size)

        # Dibujar el jugador
        pyxel.blt(self.plane.x, self.plane.y, 0, 0, 10, 16, 22)
        # We draw the plane taking the values from the plane object
        # Parameters are x, y, and a tuple containing the image bank,
        # the starting x and y and the size
        pyxel.blt(self.plane.x, self.plane.y, 0, 0, 10, 16, 22)
