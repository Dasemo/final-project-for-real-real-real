import pyxel

class Map:
    def __init__(self):
        self.drawing = [
            [0, 240, 0, 48, 104, 16, 16],  # Brick block
            [0, 0, 0, 64, 104, 8, 8],  # Blue block
            [0, 0, 0, 80, 104, 16, 16],  # Straight pipe
            [0, 0, 0, 0, 104, 16, 16],  # POW
            [0, 0, 0, 128, 104, 16, 16],  # Pipe 2
            [0, 0, 0, 110, 104, 16, 16],  # Pipe 3
        ]

        # List of obstacles with their positions and dimensions
        self.obstacles = [
            {"x": 0, "y": 240, "w": 33 * 8, "h": 16},  # Ground
            {"x": 0, "y": 184, "w": 11 * 8, "h": 8},  # First level left
            {"x": 255 - 12 * 8, "y": 184, "w": 12 * 8, "h": 8},  # First level right
            {"x": 239, "y": 223, "w": 16, "h": 16},  # Pipe right
            {"x": 0, "y": 223, "w": 16, "h": 16},  # Pipe left
            {"x": 120, "y": 184, "w": 16, "h": 16},  # POW
            {"x": 0, "y": 136, "w": 4 * 8, "h": 8},  # Second level left
            {"x": 255 - 5 * 8, "y": 136, "w": 5 * 8, "h": 8},  # Second level right
            {"x": 0, "y": 72, "w": 11 * 8, "h": 8},  # Third level left
            {"x": 255 - 12 * 8, "y": 72, "w": 12 * 8, "h": 8},  # Third level right
            {"x": 64, "y": 120, "w": 16 * 8, "h": 8},  # Fourth level
            {"x": 16 + 16, "y": 48 + 32, "w": 16, "h": 16},  # Pipe 2 left
            {"x": 255 - 32, "y": 48 + 32, "w": 16, "h": 16},  # Pipe 2 right
            {"x": 18, "y": 32 + 32, "w": 16, "h": 16},  # Pipe 3 left
            {"x": 34 + 255, "y": 32 + 32, "w": 16, "h": 16},  # Pipe 1 (2) left
        ]

    def draw(self):
        for i in range(len(self.drawing)):
            a = 0
            for e in range(33):
                pyxel.blt(a, self.drawing[0][1], self.drawing[0][2], self.drawing[0][3], self.drawing[0][4], self.drawing[0][5], self.drawing[0][6])  # Ground
                a = a + 8

            for obstacle in self.obstacles:
                pyxel.rect(obstacle["x"], obstacle["y"], obstacle["w"], obstacle["h"], 0)  # Draw obstacles (for debugging)

