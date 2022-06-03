# ex068.py

class Pessoa:
    def __init__(self,nome,idade,sexo=False,altura=False,escolaridade=False):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura
        self.escolaridade = escolaridade

pessoa1 = Pessoa('Fernando', 40,'M',1.68)
pessoa2 = Pessoa('Tania', 49,'F',1.59,'Relações Públicas')
pessoa3 = Pessoa('Maria', 25,'F',1.61)

print(pessoa1.nome,pessoa1.idade,pessoa1.sexo,pessoa1.altura,pessoa1.escolaridade)
print(pessoa2.nome,pessoa2.idade,pessoa2.sexo,pessoa2.altura,pessoa2.escolaridade)
print(pessoa3.nome,pessoa3.idade,pessoa3.sexo,pessoa3.altura,pessoa3.escolaridade)