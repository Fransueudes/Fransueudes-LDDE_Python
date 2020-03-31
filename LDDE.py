class No():
    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo

class LDDE():
    def __init__(self):
        self.prim = None
        self.ult = None
        self.quant = 0

    def inserirInicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.prim.ant = self.prim = No(None, valor, self.prim)
        self.quant += 1

    def inserirFim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, None)
        self.quant += 1

    def removerInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.prim.ant = None
        self.quant -= 1

    def removerFim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.ult = self.ult.ant
            self.ult.prox = None
        self.quant -= 1
           
    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info)
            aux = aux.prox
        
    def getPrim(self):
        return self.prim.info
    
    def getUlt(self):
        return self.ult.info
    
    def estaVazia(self):
        return self.quant == 0
        
    def inserirAposDet(self, valor1, valor2):
        aux = self.prim
        while aux.info != valor2:
             aux = aux.prox

        aux.prox = aux.prox.ant = No(aux, valor1, aux.prox)        
        self.quant += 1
                
    def remover(self, valor):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux = self.prim
            while aux.info != valor:
                aux = aux.prox
            if aux == self.prim:
                self.prim = self.prim.prox
                self.prim.ant = None
            elif aux == self.ult:
                self.ult = self.ult.ant
                self.ult.prox = None
            else:
                aux.ant.prox = aux.prox
                aux.prox.ant = aux.ant
        self.quant -= 1
        
    def showReverso(self):
        aux = self.ult
        while aux != None:
            print(aux.info)
            aux = aux.ant
