import pyxel

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120

class Shellcreeper:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 1

    def update(self):
        self.x += 2 * self.direction
        if self.x >= SCREEN_WIDTH or self.x < 0:
            self.x = (self.x + SCREEN_WIDTH) % SCREEN_WIDTH
            self.direction *= -1

class Game:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.shellcreepers = []

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.frame_count % 10 == 0:
            self.spawn_shellcreeper()

        for shellcreeper in self.shellcreepers:
            shellcreeper.update()

    def draw(self):
        pyxel.cls(0)

        for shellcreeper in self.shellcreepers:
            pyxel.rect(shellcreeper.x, shellcreeper.y, 8, 8, 9)

    def spawn_shellcreeper(self):
        shellcreeper = Shellcreeper(0, 8)
        self.shellcreepers.append(shellcreeper)

Game()