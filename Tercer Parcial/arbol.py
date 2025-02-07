import conf

class Arbol:
    def __init__(self):
        self.raiz = None
    
    def imprimir(self, cabeza):
        if cabeza != None:
            self.imprimir(cabeza.hijoIzq)
            self.imprimir(cabeza.hijoDer)
            cabeza.imprimir()
        
    def pintar(self, canvas, cabeza):
        if cabeza is not None:
            self.pintar(canvas, cabeza.hijoIzq)
            self.pintar(canvas, cabeza.hijoDer)
            cabeza.pintar(canvas)

    def anadir(self, padre, nuevo):
        if self.raiz is None:
            self.raiz = nuevo
            self.raiz.posY = conf.coorri
            self.raiz.posX = conf.anchoVe//2
            self.raiz.nivel = 1
            d = 2 ** self.raiz.nivel
            anchura = conf.anchoVe // d
            self.raiz.parX = anchura

            self.raiz.posYPapi = self.raiz.posY
            self.raiz.posXPapi = self.raiz.posX
            self.raiz.posXMia = self.raiz.posX
            self.raiz.posYMia = self.raiz.posY

        else:
            if padre is not None:
                if padre.valor > nuevo.valor:
                    if padre.hijoIzq is None:
                        padre.hijoIzq = nuevo
                        nuevo.posY = padre.posY + conf.coorri
                        nuevo.nivel = padre.nivel + 1
                        nuevo.parX = padre.parX // 2
                        nuevo.posX = padre.posX - nuevo.parX

                        nuevo.posXPapi = padre.posX + 20
                        nuevo.posYPapi = padre.posY + 40
                        nuevo.posXMia = nuevo.posX + 20
                        nuevo.posYMia = nuevo.posY
                    else:
                        self.anadir(padre.hijoIzq, nuevo)
                else:
                    if padre.hijoDer is None:
                        padre.hijoDer = nuevo
                        nuevo.posY = padre.posY + conf.coorri
                        nuevo.nivel = padre.nivel + 1
                        nuevo.parX = padre.parX // 2
                        nuevo.posX = padre.posX + nuevo.parX

                        nuevo.posXPapi = padre.posX + 20
                        nuevo.posYPapi = padre.posY + 40
                        nuevo.posXMia = nuevo.posX + 20
                        nuevo.posYMia = nuevo.posY
                    else:
                        self.anadir(padre.hijoDer, nuevo)

    def eliminar(self, valor):
        def eliminar_nodo(padre, nodo, valor):
            print(f"Revisando nodo {nodo.valor}")
            if nodo is None:
                return None
            
            if valor < nodo.valor:  
                print(f"Revisando nodo hijo izq {nodo.hijoIzq.valor}")
                nodo.hijoIzq = eliminar_nodo(nodo, nodo.hijoIzq, valor)
            elif valor > nodo.valor:  
                print(f"Revisando nodo hijo der {nodo.hijoDer.valor}")
                nodo.hijoDer = eliminar_nodo(nodo, nodo.hijoDer, valor)
            else:  
                print("Nodo encontrado, eliminando ...")
                if nodo.hijoIzq is None and nodo.hijoDer is None:
                    print("No tienen hijos, devolviendo valor vacio")
                    return None

                
                if nodo.hijoIzq is None:
                    return nodo.hijoDer
                elif nodo.hijoDer is None:
                    return nodo.hijoIzq

                sucesor = self.obtener_minimo(nodo.hijoDer)
                nodo.valor = sucesor.valor  
                nodo.hijoDer = eliminar_nodo(nodo, nodo.hijoDer, sucesor.valor)  
            return nodo

        self.raiz = eliminar_nodo(None, self.raiz, valor)
        return self.raiz

    def obtener_minimo(self, nodo):
        actual = nodo
        while actual.hijoIzq is not None:
            actual = actual.hijoIzq
        return actual
