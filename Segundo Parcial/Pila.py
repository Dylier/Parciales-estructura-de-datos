import conf

class Pila:
    def __init__(self):
        self.elementos = []

    def anadir(self, valor):
        self.elementos.append(valor)

    def eliminar(self):
        if self.elementos:
            self.elementos.pop()

    def pintar(self, canvas):
        x, y = conf.anchoVe//2, 50
        for elemento in reversed(self.elementos):
            canvas.create_rectangle(x-30, y, x+30, y+40, fill="lightblue")
            canvas.create_text(x, y+20, text=str(elemento))
            y += 50