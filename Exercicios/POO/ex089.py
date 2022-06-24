
texto = 'Caminhando e cantando e seguindo a canção Somos todos iguais, braços dados ou não Nas escolas, nas ruas, campos, construções Caminhando e cantando e seguindo a canção'

print(f'{len(texto)} total de caracteres.')

txt_sem_Pontuacao = ''
for i in texto:
    if i.isalpha() or i ==' ':
        txt_sem_Pontuacao += i

print(f'{len(txt_sem_Pontuacao)} total de caracteres, depois da limpeza.')

palavras = txt_sem_Pontuacao.split()
print(palavras)
print(f'{len(palavras)} total de palavras')

conta_palavras = {}
for palavra in palavras:
    conta_palavras[palavra] = conta_palavras.get(palavra, 0) + 1
    '''if palavra not in conta_palavras:
        conta_palavras[palavra] = 0
    
    conta_palavras[palavra] +=1'''
    
print(f'{(conta_palavras)} total de ocorrências')
print(f'{len(conta_palavras)} total de ocorrências')