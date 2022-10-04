import pandas as pd
# import matplotlib.pyplot as plt

x = pd.read_csv(r"C:\Users\Fernando\Entra21\Teste-Git-Sanjo\Exercicios\panda1.csv")
# #x = pd.read_excel(r"C:\Users\Fernando\Entra21\Teste-Git-Sanjo\Exercicios\61110.xls")

# plt.pie(x['abril'], labels= x['meses'],autopct='%1.2f%%')
# plt.show()
x.columns = [a.replace("/"," ")for a in x.columns.to_list()]
print(x)


