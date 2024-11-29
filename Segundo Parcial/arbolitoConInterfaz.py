import tkinter as tk
import arbol

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gráfica Árbol")
        self.geometry(f"{500}x{500}")
        self.canvas = tk.Canvas(self, width=500, height=500, bg="white")
        self.canvas.pack()

        self.dibujar_arbol()

    def dibujar_arbol(self):
        arbol.Arbol.pintar(self.canvas, arbol.Arbol.raiz)

v = Ventana()
v.dibujar_arbol()