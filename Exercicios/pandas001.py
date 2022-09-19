import pandas as pd

d = {'nome': ['Ana','Maria','José'],'Idade': [16,25,19], 'altura': [1.72,1.59,1.68]}

dados = pd.DataFrame(data= d)

print(dados)

dados.to_excel('exporta.xlsx', index = False)
