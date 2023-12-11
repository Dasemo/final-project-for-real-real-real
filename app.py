import pyxel
from Player import Player
from map import Map
from enemies import Shellcreeper
from enemies import Sidestepper

class App:
    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h

        pyxel.init(self.width, self.height, title="Mario Bros. Classic")
        pyxel.load("assets/ey.pyxres")

        self.plane = Player(self.width // 2, 218)
        self.shellcreeper = Shellcreeper(80, 60, 1)
        self.sidestepper = Sidestepper(100, 60, 1)
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
        elif pyxel.btn(pyxel.KEY_A):
            self.plane.move('left', self.width)
        elif pyxel.btn(pyxel.KEY_D):
            self.plane.move('right', self.width)
        elif pyxel.btn(pyxel.KEY_W):
            self.plane.jump()
        
        self.shellcreeper.update()
        self.sidestepper.update()
        # Update the plane's state
        self.plane.update()

    def draw(self):
        pyxel.cls(0)
        self.mapa.draw()
        self.shellcreeper.draw()
        self.sidestepper.draw()
        # Dibujar el jugador
        pyxel.blt(self.plane.x, self.plane.y, 0, 0, 10, 16, 22)
       