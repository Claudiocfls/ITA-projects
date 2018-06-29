# interface
class FabricaDeCarro:
    def criarCarroSedan(self):
        raise NotImplemented()
    def criarCarroPopular(self):
        raise NotImplemented()

class FabricaFiat(FabricaDeCarro):
    def criarCarroSedan(self):
        siena = Siena()
        return siena
    def criarCarroPopular(self):
        palio = Palio()
        return palio

# interface
class CarroPopular:
    def get_info(self):
        raise NotImplemented()

# interface
class CarroSedan:
    def get_info(self):
        raise NotImplemented()

class Siena(CarroSedan):
    def get_info(self):
        print("esse é um siena, um carro sedan!")

class Palio(CarroPopular):
    def get_info(self):
        print("esse é um pálio, um carro popular!")

if __name__ == '__main__':
    fabrica = FabricaFiat()
    carro = fabrica.criarCarroPopular()
    carro2= fabrica.criarCarroSedan()
    carro.get_info()
    carro2.get_info()
