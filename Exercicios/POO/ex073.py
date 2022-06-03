# ex073.py
"""
class Calcula:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b


    def analisa(self):
        for i in range(self.a,self.b): 
            if(i%7 == 0 and i%5 != 0):
                return i  
                #print(i, end=',')
                 
resultado = Calcula(200,2200)
print(resultado.analisa())"""

for i in range(200,2200): 
    if(i%7 == 0 and i%5 != 0): 
        print(i, end=',')

