import nodo
import arbol
import random
import conf
import tkinter as tk

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gráfica Árbol")
        self.geometry(f"{conf.anchoVe}x{conf.largoVe}")
        self.canvas = tk.Canvas(self, width=conf.anchoVe, height=conf.largoVe, bg="white")
        self.canvas.pack()

    def dibujar_arbol(self, arbolito):
        arbolito.pintar(self.canvas, arbolito.raiz)

class main():
    arbolin = arbol.Arbol()
    for _ in range(10):
        arbolin.anadir(arbolin.raiz, nodo.Nodo(random.randint(1,10)))
    arbolin.imprimir(arbolin.raiz)
    v = Ventana()
    v.dibujar_arbol(arbolin)
    v.mainloop()
    
main()