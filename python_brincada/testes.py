"""
class classe1 :
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print("opa1")
    
    def cu(self):
        return self.nome + " tem " + self.idade + " de idade" 

class classe2(classe1):
    def __init__(self, nome, idade, pedra):
        super().__init__(nome, idade)
        self.pedra = pedra
        print("opa2")
    
    #def cu(self):
     #   return classe1.cu(self) + " " + self.pedra
       

class classe3(classe1):
    def __init__(self, nome, idade, pena):
        super().__init__(nome, idade)
        self.pena = pena
        print("opa3")
    
    def cu(self):
        #return classe1.cu(self) + " " + self.pena
        return self.pena

opa1 = classe2("p1", "2", "p3")
opa2 = classe3("p2", "3", "p4")
print(opa1.cu())
print(opa2.cu())
"""
#prices
"""
def opa(list):
    x = list[0]
    z = list[0]
    for items in list:
        y = list[items]
        if y < x:
            x = list[items]
        if y > z:
            z = list[items]
    print(z - x)

opa([3,3,4,5,3,7,8,10,3,4,7])



#l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
l = [[["ops"],["14", "23", "35", "hello"]], [["ssas"],["2", "7", "soos", "ooo"]]]
for p in l:
   # print(p[0], p[1], p[2], p[3])
    print(p[0][0][2]) #qual(quais) itens dos itens p da lista, o valor de p é o item da lista l,
                        #o primeiro [] informa qual item da lista l de valor p (crescente ja que é um for)
                            #o
"""
"""
import os

x = open("opa.txt", "r")

for linha in x:
    #print(linha.strip())
    print(repr(linha))

x.close()
"""
"""
print("opa"+ "\\n")
"""
"""
import os

try:
    os.rmdir("diretoriopapapapapapasdkaspsda")
except Exception as erro:
    print("1")
except OSError as erro:
    print("2")
except FileNotFoundError as erro:
    print("3")

"""