import pyxel

class Game:
    def __init__(self):
        pyxel.init(160, 120)
        self.player_x = 75
        self.player_y = 100

        self.enemy_x = 30
        self.enemy_y = 100

        pyxel.run(self.update, self.draw)

    def update(self):
        # Mover el jugador
        if pyxel.btn(pyxel.KEY_LEFT) and self.player_x > 0:
            self.player_x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x < pyxel.width - 10:
            self.player_x += 1

        # Mover el enemigo (en este caso, el enemigo se mueve automáticamente)
        self.enemy_x += 2
        if self.enemy_x > pyxel.width:
            self.enemy_x = 0

        # Detección de colisión
        player_rect = (self.player_x, self.player_y, 10, 10)
        enemy_rect = (self.enemy_x, self.enemy_y, 10, 10)

        if self.check_collision(player_rect, enemy_rect):
            print("¡Colisión!")

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.player_x, self.player_y, 10, 10, 9)  # Dibuja al jugador
        pyxel.rect(self.enemy_x, self.enemy_y, 10, 10, 8)  # Dibuja al enemigo

    def check_collision(self, rect1, rect2):
        # Verifica si dos rectángulos se intersectan
        return (
            rect1[0] < rect2[0] + rect2[2] and
            rect1[0] + rect1[2] > rect2[0] and
            rect1[1] < rect2[1] + rect2[3] and
            rect1[1] + rect1[3] > rect2[1]
        )

if __name__ == "__main__":
    Game()
