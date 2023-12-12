import pyxel

# Initialize Pyxel
pyxel.init(160, 120)

# Player and enemy rectangles
player = {"x": 20, "y": 20, "w": 10, "h": 10}
enemy = {"x": 100, "y": 50, "w": 10, "h": 15}

def update():

    # Store the player's current position
    prev_player_x, prev_player_y = player["x"], player["y"]

    # Move player with arrow keys
    if pyxel.btn(pyxel.KEY_LEFT):
        player["x"] -= 1
    if pyxel.btn(pyxel.KEY_RIGHT):
        player["x"] += 1
    if pyxel.btn(pyxel.KEY_UP):
        player["y"] -= 1
    if pyxel.btn(pyxel.KEY_DOWN):
        player["y"] += 1

    # Check for collision
    if is_collision(player, enemy):
        # If collision, revert player to previous position
        player["x"], player["y"] = prev_player_x, prev_player_y

def draw():
    # Clear screen
    pyxel.cls(0)

    # Draw player and enemy rectangles
    pyxel.rect(player["x"], player["y"], player["w"], player["h"], 8)
    pyxel.rect(enemy["x"], enemy["y"], enemy["w"], enemy["h"], 9)

def is_collision(obj1, obj2):
    # Rectangle collision detection
    return (
        obj1["x"] < obj2["x"] + obj2["w"]
        and obj1["x"] + obj1["w"] > obj2["x"]
        and obj1["y"] < obj2["y"] + obj2["h"]
        and obj1["y"] + obj1["h"] > obj2["y"]
    )

# Run the game
pyxel.run(update, draw)
