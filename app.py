import pyxel
from Player import Player
from map import Map
from enemies import Shellcreeper
from enemies import Sidestepper
from enemies import Fighter

class StartScreen:
    def __init__(self):
        self.show_start = True
    def update(self):
        if self.show_start and pyxel.btnp(pyxel.KEY_P):
            self.show_start = False
    def draw(self):
        if self.show_start:
            pyxel.cls(0)
            pyxel.text(55, 50, "Press P to start", 7)

class App:
    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h
        self.start_screen = True
        pyxel.init(self.width, self.height, title="Mario Bros. Classic")
        pyxel.load("assets/ey.pyxres")
        self.plane = Player(self.width // 2, 218)
        self.shellcreeper = Shellcreeper(80, 60, 1)
        self.sidestepper = Sidestepper(100, 60, 1)
        self.fighter = Fighter(120, 60, 1)
        self.map = Map()

    def update(self):
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
        
        self.shellcreeper.update()
        self.sidestepper.update()
        self.fighter.update()
        # Update the plane's state
        self.plane.update()

    def draw(self):
        pyxel.cls(0)
        self.map.draw()
        self.shellcreeper.draw()
        self.sidestepper.draw()
        self.fighter.draw()
        # Dibujar el jugador
        pyxel.blt(self.plane.x, self.plane.y, 0, 0, 10, 16, 22, 0)
        pyxel.blt(60, 20, 0, 8, 0, 8, 8, 0)
        pyxel.blt(70, 20, 0, 8, 0, 8, 8, 0)
        pyxel.blt(80, 20, 0, 8, 0, 8, 8, 0)
    
    def startgame(self):
        self.startgame = False
        while not self.startgame:
            pyxel.text(self.height // 2, self.width // 2, "Press P to start the game", 6)
            if pyxel.btn(pyxel.KEY_P):
                self.startgame = True
    