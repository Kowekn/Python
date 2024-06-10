import datetime

class Extrato:
    def __init__(self): 
        self.transacoes = [] 
    def extrato(self, numeroconta):
        print(f'Extrato : {numeroconta}')
        for p in self.transacoes: #aqui ele pega o p objeto
            print(f'{p[0]:15s} {p[1]:10.2f} {p[2]:10s} {p[3].strftime("%d/%m/%y")}')  #p é o valor do objeto e nao sua posicao na lista
            #os objetos estão em forma de lista, onde cada linha tem sua conta correspondente
            #o for faz a listagem de todas as transações, onde p é o número da transação, 1ª, 2ª transação e assim por diante
            

