import pandas as pd
# import matplotlib.pyplot as plt

# x = pd.read_excel(r"C:\Users\Fernando\Entra21\Teste-Git-Sanjo\Exercicios\pandas1.xlsx")
# #x = pd.read_excel(r"C:\Users\Fernando\Entra21\Teste-Git-Sanjo\Exercicios\61110.xls")

# plt.pie(x['abril'], labels= x['meses'],autopct='%1.2f%%')
# plt.show()

# print(x)
# print(x['meses'],[3])

dados = [[0,'Sanjo','Qual curso?',6],
         [0,'Senior','Qual curso?',8],
         [1,'Ailos','Qual curso?',8],
         [0,'Arvoredo','Qual curso?',9]]

#dados = [[0,'Sanjo','Qual curso?',9]]

df = pd.DataFrame(dados, columns=['crb','ans','que','qid'])

def verifica(base8,empresa):
    ret = 'None'
    for a,b in base8.items():
        if (a == empresa):
            ret = b
    return ret

base8 = {'Senior':'Empresa1',
'Sanjo':'Empresa2',
'Ailos':'Empresa3',
'Arvoredo':'Empresa4'}

print(df)

df[(df['qid'].isin([8]))]
#novo_nome = verifica (base8,df['ans'].values[3])
novo_nome = verifica (base8,'Sanjo')
print(novo_nome)


