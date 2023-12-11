import pyxel

def check_collision(player_x, player_y, player_width, player_height, platform_x, platform_y, platform_width, platform_height):
    # Check if player and platform overlap in the x-axis
    x_collision = player_x < platform_x + platform_width and player_x + player_width > platform_x

    # Check if player and platform overlap in the y-axis
    y_collision = player_y < platform_y + platform_height and player_y + player_height > platform_y

    # Return True if there is a collision, False otherwise
    return x_collision and y_collision

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Collision Detection Example")
        self.player_x = 80
        self.player_y = 60
        self.player_width = 16
        self.player_height = 16

        self.platform_x = 60
        self.platform_y = 80
        self.platform_width = 80
        self.platform_height = 10

        pyxel.run(self.update, self.draw)

    def update(self):
        # Example: Move the player left or right
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x -= 1
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x += 1

        # Example: Check for collision with the platform
        if check_collision(self.player_x, self.player_y, self.player_width, self.player_height,
                            self.platform_x, self.platform_y, self.platform_width, self.platform_height):
            # Handle collision (e.g., stop the player from falling)
            # For simplicity, we'll just set the player's y-coordinate to the top of the platform
            self.player_y = self.platform_y - self.player_height

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.player_x, self.player_y, self.player_width, self.player_height, 9)
        pyxel.rect(self.platform_x, self.platform_y, self.platform_width, self.platform_height, 6)

if __name__ == "__main__":
    App()