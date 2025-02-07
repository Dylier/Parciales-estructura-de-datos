import tkinter as tk
import conf
import arbol
import nodo

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Estructuras de Datos")
        self.geometry(f"{750}x{650}")

        # Menú de selección
        self.estructura_var = tk.StringVar(value="Arbol")
        opciones = ["Arbol", "Pila", "Cola", "Lista"]
        self.menu_estructura = tk.OptionMenu(self, self.estructura_var, *opciones)
        self.menu_estructura.place(x=10, y=10)  # Usando place

        # Crear lienzos para cada estructura
        self.canvas_arbol = tk.Canvas(self, width=conf.anchoVe, height=conf.largoVe, bg="white")
        self.canvas_arbol.place(x=10, y=50) # Usando place, ajusta las coordenadas
        self.canvas_pila = tk.Canvas(self, width=200, height=180, bg="lightgray") # Tamaño ajustado
        self.canvas_pila.place(x=520, y=50) # Usando place, ajusta las coordenadas
        self.canvas_cola = tk.Canvas(self, width=200, height=180, bg="lightblue") # Tamaño ajustado
        self.canvas_cola.place(x=520, y=240) # Usando place, ajusta las coordenadas
        self.canvas_lista = tk.Canvas(self, width=200, height=180, bg="lightgreen") # Tamaño ajustado
        self.canvas_lista.place(x=520, y=430) # Usando place, ajusta las coordenadas


        # Entrada para el valor del nodo
        self.entrada_valor = tk.Entry(self, width=20)
        self.entrada_valor.place(x=10, y=570)  # Usando place

        # Botones
        self.boton_añadir = tk.Button(self, text="Añadir", command=self.accion_añadir, width=15)
        self.boton_añadir.place(x=150, y=570)  # Usando place

        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.accion_eliminar, width=15)
        self.boton_eliminar.place(x=270, y=570)  # Usando place

        self.boton_reiniciar = tk.Button(self, text="Reiniciar", command=self.accion_reiniciar, width=15)
        self.boton_reiniciar.place(x=390, y=570)  # Usando place

        # Estructuras de datos
        self.arbolito = arbol.Arbol()
        self.pila = []
        self.cola = []
        self.lista = []

    def dibujar_estructuras(self):
        self.canvas_arbol.delete("all")
        self.canvas_pila.delete("all")
        self.canvas_cola.delete("all")
        self.canvas_lista.delete("all")
        self.arbolito.pintar(self.canvas_arbol, self.arbolito.raiz)

        # Dibujar pila (ajustado para place)
        for i, val in enumerate(reversed(self.pila)):
            self.canvas_pila.create_rectangle(10, 10 + i * 30, 110, 40 + i * 30, fill="red")
            self.canvas_pila.create_text(60, 25 + i * 30, text=str(val))

        # Dibujar cola (ajustado para place)
        for i, val in enumerate(self.cola):
            self.canvas_cola.create_rectangle(10, 10 + i * 30, 110, 40 + i * 30, fill="blue")
            self.canvas_cola.create_text(60, 25 + i * 30, text=str(val))

        # Dibujar lista (ajustado para place)
        for i, val in enumerate(self.lista):
            self.canvas_lista.create_rectangle(10, 10 + i * 30, 110, 40 + i * 30, fill="green")
            self.canvas_lista.create_text(60, 25 + i * 30, text=str(val))

    def accion_añadir(self):
        valor = self.entrada_valor.get()
        if valor.isdigit():
            valor = int(valor)
            estructura = self.estructura_var.get()
            if estructura == "Arbol":
                self.arbolito.anadir(self.arbolito.raiz, nodo.Nodo(valor))
            elif estructura == "Pila":
                self.pila.append(valor)
            elif estructura == "Cola":
                self.cola.append(valor)
            elif estructura == "Lista":
                self.lista.append(valor)
            self.dibujar_estructuras()
            self.entrada_valor.delete(0, 'end')
        else:
            print("Ingrese un valor numérico válido")

    def accion_eliminar(self):
        estructura = self.estructura_var.get()
        if estructura == "Arbol":
            valor = self.entrada_valor.get()
            if valor.isdigit():
                self.arbolito.raiz = self.arbolito.eliminar(int(valor))
        elif estructura == "Pila" and self.pila:
            self.pila.pop()
        elif estructura == "Cola" and self.cola:
            self.cola.pop(0)
        elif estructura == "Lista" and self.lista:
            valor = self.entrada_valor.get()
            if valor.isdigit():
                valor = int(valor)
                if valor in self.lista:
                    self.lista.remove(valor)
        self.dibujar_estructuras()
        self.entrada_valor.delete(0, 'end')

    def accion_reiniciar(self):
        self.arbolito = arbol.Arbol()
        self.pila = []
        self.cola = []
        self.lista = []
        self.dibujar_estructuras()

class Main:
    def __init__(self):
        v = Ventana()
        v.dibujar_estructuras()
        v.mainloop()

Main()
