# ex074.py

class Calculadora:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def div(self):
        return self.a / self.b
    def mult(self):
        return self.a * self.b

operacao = Calculadora(int(input('1º nº: ')),int(input('2º nº: ')))
operador = (input('Digite uma das operações: soma = + ,subtração = - ,divisão = / ,multiplicação = * :'))
print(operador, end='')
if operador == '+':
    print(f' A soma é {operacao.soma()}')
if operador == '-':
    print(f' A subtração é {operacao.sub()}')
if operador == '/':
    print(f' A divisão é {operacao.div()}')
if operador == '*':
    print(f' A multiplicação é {operacao.mult()}')