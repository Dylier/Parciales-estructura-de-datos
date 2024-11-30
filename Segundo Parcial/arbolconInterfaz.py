import nodo
import arbol
import random
import conf
import tkinter as tk

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Árbol Binario")
        self.geometry(f"{conf.anchoVe}x{conf.largoVe}")

        # Crear el lienzo para el árbol
        self.canvas = tk.Canvas(self, width=conf.anchoVe, height=conf.largoVe - 100, bg="white")
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Entrada para el valor del nodo
        self.entrada_valor = tk.Entry(self, width=20)
        self.entrada_valor.pack(side=tk.LEFT, padx=10, pady=10)

        # Botones
        self.boton_añadir = tk.Button(self, text="Añadir Nodo", command=self.accion_añadir)
        self.boton_añadir.pack(side=tk.LEFT, padx=10, pady=10)

        self.boton_eliminar = tk.Button(self, text="Eliminar Nodo", command=self.accion_eliminar)
        self.boton_eliminar.pack(side=tk.LEFT, padx=10, pady=10)

        self.boton_reiniciar = tk.Button(self, text="Reiniciar Árbol", command=self.accion_reiniciar)
        self.boton_reiniciar.pack(side=tk.LEFT, padx=10, pady=10)

        self.boton_imprimir = tk.Button(self, text="Imprimir Árbol", command=self.accion_imprimir)
        self.boton_imprimir.pack(side=tk.LEFT, padx=10, pady=10)

    def dibujar_arbol(self, arbolito):
        self.canvas.delete("all")
        arbolito.pintar(self.canvas, arbolito.raiz)

    def accion_añadir(self):

        valor = self.entrada_valor.get()
        if valor.isdigit():
            arbolito.anadir(arbolito.raiz, nodo.Nodo(int(valor)))
            self.dibujar_arbol(arbolito)
            self.entrada_valor.delete(0, 'end')
        else:
            messagebox.showerror("Error", "Ingrese un valor numérico válido.")

    def accion_eliminar(self):
        valor = self.entrada_valor.get()
        if valor.isdigit():
            arbolito.raiz = arbolito.eliminar(arbolito.raiz, int(valor))
            self.dibujar_arbol(arbolito)
            self.entrada_valor.delete(0, 'end')
        else:
            messagebox.showerror("Error", "Ingrese un valor numérico válido.")

    def accion_reiniciar(self):
        global arbolito
        arbolito = arbol.Arbol()
        self.dibujar_arbol(arbolito)

    def accion_imprimir(self):
        arbolito.imprimir(arbolito.raiz)

arbolito = arbol.Arbol()


class main():
    arbolin = arbol.Arbol()
    for _ in range(10):
        arbolin.anadir(arbolin.raiz, nodo.Nodo(random.randint(1,10)))
    arbolin.imprimir(arbolin.raiz)
    v = Ventana()
    v.dibujar_arbol(arbolin)
    v.mainloop()
    
main()

