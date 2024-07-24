from classe import Carro, CarroEletrico

carro1 = Carro('Uno', 'Chassi do Fiat Uno', 'Fiat', '3.999.0')
print(carro1.chassi)
print(carro1.marca)
print(carro1.modelo)
print(carro1.get_documento())

carro2 = CarroEletrico('Cybertruck', 'Chassi do Cybertruck', 'Tesla', '3.999.0', 400, 'Doutor Severiano - RN')
print(carro2.chassi)
print(carro2.marca)
print(carro2.modelo)
print(carro2.get_documento())
print(carro2.bateriaCarga)
print(carro2.get_localizacao())
