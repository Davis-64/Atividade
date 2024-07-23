class Carro:
    def __init__(self, modelo, chassi, marca, documento):
        self.modelo = modelo
        self.chassi = chassi
        self.marca = marca
        self._documento = documento

    def get_documento(self):
        return self._documento
    
class CarroEletrico(Carro):
    def __init__(self, modelo, chassi, marca, documento, bateriaCarga, localizacao):
        super().__init__(modelo, chassi, marca, documento)
        self.bateriaCarga = bateriaCarga
        self.__localizacao = localizacao

    def get_localizacao(self):
        return self.__localizacao