# Clase para el mapa
import pyxel
class Map:
    def __init__(self):
        self.drawing = [
            [0, 240, 0, 48, 104, 16, 16],  # Bloque de brick
            [0, 0, 0, 64, 104, 8, 8],  # Bloque azul
            [0, 0, 0, 80, 104, 16, 16], #Tubería recta
            [0, 0, 0, 0, 104, 16, 16]  #POW
        ]

    def draw(self):
        for i in range(len(self.drawing)):
            a = 0
            for e in range(33):
                pyxel.blt(a, self.drawing[0][1], self.drawing[0][2], self.drawing[0][3], self.drawing[0][4], self.drawing[0][5], self.drawing[0][6])# suelo
                a = a + 8
            a = 0
            for xd in range(11):
                pyxel.blt(a, self.drawing[1][1] + 184, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])#primer nivel izquierda
                a = a + 8
            a = 255
            for xd in range(12):
                pyxel.blt(a, self.drawing[1][1] + 184, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])#primer nivel derecha
                a = a - 8
            pyxel.blt(239, 223, self.drawing[2][2], self.drawing[2][3], self.drawing[2][4], self.drawing[2][5], self.drawing[2][6]) #Tuberia derecha
            pyxel.blt(0, 223, self.drawing[2][2], self.drawing[2][3], self.drawing[2][4], -self.drawing[2][5], self.drawing[2][6])  #Tuberia izquierda
            pyxel.blt(120, 184, self.drawing[3][2], self.drawing[3][3], self.drawing[3][4], self.drawing[3][5], self.drawing[3][6])  #POW
            a = 0
            for xd in range(4):
                pyxel.blt(a, self.drawing[1][1] + 136, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])#primer nivel izquierda
                a = a + 8
            a = 255
            for xd in range(5):
                pyxel.blt(a, self.drawing[1][1] + 136, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])#primer nivel izquierda
                a = a - 8
            a = 0
            for xd in range(11):
                pyxel.blt(a, self.drawing[1][1] + 72, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])#primer nivel izquierda
                a = a + 8
            a = 255
            for xd in range(12):
                pyxel.blt(a, self.drawing[1][1] + 72, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])#primer nivel izquierda
                a = a - 8
            a = 64
            for xd in range(16):
                pyxel.blt(a, self.drawing[1][1] + 120, self.drawing[1][2], self.drawing[1][3], self.drawing[1][4], self.drawing[1][5], self.drawing[1][6])#primer nivel izquierda
                a = a + 8
            
            