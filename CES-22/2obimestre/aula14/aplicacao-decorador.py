
# classe abstrata
class Lanche:
    def mostraIngredientes(self):
        print("Ingredientes:")
        for k,v in self.ingredientes.items():
            print("  %s" % k, end=": ")
            print(v, end="\n")

    def mostraPreco(self):
        print("esse Lanche custa %d reais!" % self.preco)

# classe concreta
class Bauru(Lanche):
    def __init__(self):
        self.preco = 5
        self.ingredientes = {'pao':'frances','recheio':['presunto']}

# classe abstrata
class decoradorLanche(Lanche):
    def __init__(self, Lanche, ingrediente_adicional, preco_adicional):
        self.lanche = Lanche
        self.ingredientes = Lanche.ingredientes
        self.preco = Lanche.preco
        self.ingrediente_adicional = ingrediente_adicional
        self.preco_adicional = preco_adicional

    def mostraIngredientes(self):
        ingredientes = self.ingredientes
        ingredientes['recheio'].append(self.ingrediente_adicional)
        print("Ingredientes:")
        for k,v in ingredientes.items():
            print("  %s" % k, end=": ")
            print(v, end="\n")

    def mostraPreco(self):
        preco = self.preco + self.preco_adicional
        print("esse Lanche custa %d reais!" % preco)
        

# classe concreta
class queijo(decoradorLanche):
    def __init__(self, Lanche):
        super().__init__(Lanche, 'queijo', 1)

class batataPalha(decoradorLanche):
    def __init__(self, Lanche):
        super().__init__(Lanche, 'batata palha', 1)

class molho(decoradorLanche):
    def __init__(self, Lanche):
        super().__init__(Lanche, 'molho', 1)

class frango(decoradorLanche):
    def __init__(self, Lanche):
        super().__init__(Lanche, 'filé de frango', 2)

if __name__=='__main__':
    # cria um lanche básico
    lanche = Bauru()
    lanche.mostraIngredientes()
    lanche.mostraPreco()
    
    # adiciona condimentos para esse mesmo lanche
    lanche = queijo(lanche)

    lanche.mostraIngredientes()
    lanche.mostraPreco()
