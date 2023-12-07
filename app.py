from Player import Player
import pyxel

class App:
    """ This class contains all the information needed to represent the
    board"""
    def __init__(self, w: int, h: int):
        """ The parameters are the width and height of the board"""
        # Initializing the object
        self.width = w
        self.height = h

        # This block initializes pyxel
        # The first thing to do is to create the screen, see API for more parameters
        pyxel.init(self.width, self.height, title="Mario Bros. Classic")
        # Loading the pyxres file, it has a 16x16 cat in (0,0) in bank 0
        pyxel.load("assets/ey.pyxres")


        # This creates a Plane at the middle of the screen in x and at y = 200
        # Notice the image is stored in the init of plane class, now it is a
        # cat
        self.plane = Player(self.width / 2, 200)

        # Running the game
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
        """ This is executed also each frame, here you should just draw
        things """
        pyxel.cls(0)
        # We draw the plane taking the values from the plane object
        # Parameters are x, y, and a tuple containing the image bank,
        # the starting x and y and the size
        pyxel.blt(self.plane.x, self.plane.y, 0, 0, 10, 16, 22)
