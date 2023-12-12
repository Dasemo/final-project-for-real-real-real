from app import App
import pyxel 

app = App(255, 255)
app.start_screen = True # This function creates the startscreen and 

def update():
    if app.start_screen:
        if pyxel.btn(pyxel.KEY_P):
            app.start_screen = False
    else:
        app.update()
        
def draw():
    if app.start_screen:
        pyxel.cls(0)
        pyxel.text(85, 100, "Mario Bros. Classic", pyxel.COLOR_WHITE)
        pyxel.text(90, 120, "Press P to start", pyxel.COLOR_WHITE)
    else:
        app.draw()
        
pyxel.run(update, draw)
pyxel.run(app.update, app.draw)
