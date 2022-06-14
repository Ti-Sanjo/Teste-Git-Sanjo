# ex081.py

import random
import string

def gera_senha(tamanho = 5):
    tabela_ascii = string.ascii_letters
    op_numeros = string.digits
    op_pontuacao = string.punctuation
    op = tabela_ascii + op_numeros + op_pontuacao

    senha = ''

    for i in range (0 , tamanho):
        aux = random.choice(op)
        senha = senha + aux

    return senha

tamanho_senha = input('Informe quantos dígitos terá sua senha: ')

if tamanho_senha.isdigit():
    tamanho_senha = int(tamanho_senha)
else:
    print('Opção de entrada inválida..!')

x = gera_senha(tamanho_senha)
print(f'A senha gerada é: {x}')

