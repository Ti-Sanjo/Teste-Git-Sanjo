# pessoa_v3.py

class Pessoa_v3:
    def __init__(self,nome,idade,sexo=False,altura=False):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura

pessoa1 = Pessoa_v3('Adriano', 47,'M',1.90)
pessoa2 = Pessoa_v3('Karina', 45)

print(pessoa1.nome,pessoa1.idade,pessoa1.sexo,pessoa1.altura)
print(pessoa2.nome,pessoa2.idade,pessoa2.sexo,pessoa2.altura)
