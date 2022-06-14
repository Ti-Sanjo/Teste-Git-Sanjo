# ex077.py

def compara():

    palavra1 = input('Digite a 1ª palavra ou frase:')
    palavra2 = input('Digite a 2ª palavra ou frase:')

    print (len(palavra1))
    print (len(palavra2))

    if len(palavra1) > len(palavra2):
        print (palavra1)
    elif len(palavra2) > len(palavra1):
        print(palavra2)
    else:
        print(palavra1, palavra2)

x = compara()


