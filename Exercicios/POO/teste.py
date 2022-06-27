
nome = input('Digite seu nome: ')
print(nome[0],nome[1],nome[2])
if (nome[0] and nome[1] and nome[2]) == ('.' or '-'):
    print('morse')
else:
    print('não é morse')
    print(type(nome))