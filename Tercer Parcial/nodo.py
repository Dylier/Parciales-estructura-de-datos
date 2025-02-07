class Nodo:
    def __init__(self, val):
        self.hijoIzq = None
        self.valor = val
        self.hijoDer = None
        self.nivel = 0
        self.posX = 400
        self.posY = 100
        self.largo = 40
        self.parX = 0

        self.posXPapi = 0
        self.posYPapi = 0
        self.posXMia = 0
        self.posYMia = 0

    def pintar(self, canvas):
        canvas.create_oval(
            self.posX, self.posY,
            self.posX + self.largo, self.posY + self.largo,
            outline="black", fill="lightblue"
        )
        centroX = self.posX + self.largo / 2
        centroY = self.posY + self.largo / 2
        canvas.create_text(
            centroX, centroY, 
            text=str(self.valor), 
            fill="black", font=("Arial", 12)
        )
        if self.posXPapi != 0 or self.posYPapi != 0:
            canvas.create_line(self.posXPapi, self.posYPapi, self.posXMia, self.posYMia, fill="black")

    def imprimir(self):
        print(f"valor {self.valor} nivel {self.nivel}")
