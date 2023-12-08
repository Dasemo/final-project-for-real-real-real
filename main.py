from app import App
import pyxel 
# We create the board and that's all
app = App(255, 255)
pyxel.run(app.update, app.draw)
