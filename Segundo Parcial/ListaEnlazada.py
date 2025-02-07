import tkinter as tk
import nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def anadir(self, valor):
        nuevo = nodo.Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.hijoDer:
                actual = actual.hijoDer
            actual.hijoDer = nuevo

    def eliminar(self, valor):
        actual = self.cabeza
        previo = None
        while actual:
            if actual.valor == valor:
                if previo:
                    previo.hijoDer = actual.hijoDer
                else:
                    self.cabeza = actual.hijoDer
                return
            previo = actual
            actual = actual.hijoDer

    def pintar(self, canvas):
        x, y = 50, 100
        actual = self.cabeza
        while actual:
            canvas.create_oval(x, y, x+40, y+40, fill="yellow")
            canvas.create_text(x+20, y+20, text=str(actual.valor))
            if actual.hijoDer:
                canvas.create_line(x+40, y+20, x+50, y+20, arrow=tk.LAST)
            x += 50
            actual = actual.hijoDer