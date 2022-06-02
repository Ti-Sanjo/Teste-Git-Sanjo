class Carros:
    nome = 'Default'

    def __init__(self):
        self.nome = 'Peugeout'

print(Carros.nome)

carro = Carros()

print(carro.nome)