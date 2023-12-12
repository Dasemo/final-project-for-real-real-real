import pyxel

class Game:
    def __init__(self):
        pyxel.init(255, 255, title="Press P to Start")
        self.game_started = False

    def update(self):
        if pyxel.btnp(pyxel.KEY_P):
            self.game_started = True

    def draw(self):
        pyxel.cls(0)
        if self.game_started:
            # Your main game drawing code goes here
            pyxel.text(80, 100, "Main Game is Running", pyxel.COLOR_WHITE)
        else:
            # Draw the start screen text
            pyxel.text(80, 100, "Press P to start the game", pyxel.COLOR_WHITE)

if __name__ == "__main__":
    game = Game()

    while not pyxel.quit:
        game.update()
        game.draw()
        pyxel.flip()
