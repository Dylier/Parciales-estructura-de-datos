import conf

class Cola:
    def __init__(self):
        self.elementos = []

    def anadir(self, valor):
        self.elementos.append(valor)

    def eliminar(self):
        if self.elementos:
            self.elementos.pop(0)

    def pintar(self, canvas):
        x, y = 50, conf.largoVe//2
        for elemento in self.elementos:
            canvas.create_rectangle(x, y, x+60, y+40, fill="lightgreen")
            canvas.create_text(x+30, y+20, text=str(elemento))
            x += 70