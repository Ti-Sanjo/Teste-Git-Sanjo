import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_excel(r"C:\Users\Fernando\Entra21\Teste-Git-Sanjo\Exercicios\pandas1.xlsx")
#x = pd.read_excel(r"C:\Users\Fernando\Entra21\Teste-Git-Sanjo\Exercicios\61110.xls")

plt.pie(x['abril'], labels= x['meses'],autopct='%1.2f%%')
plt.show()

print(x)
print(x['meses'],[3])


