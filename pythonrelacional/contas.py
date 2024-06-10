import datetime
from extratos import Extrato

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes #self é necessário para armazenar os dados da instancia
        self.numero = numero
        self.saldo = saldo
        self.data = datetime.datetime.today()
        self.extrato = Extrato()
    
    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today()])

    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True
    
    def transfereValor(self,contaDestino,valor):
        if self.saldo < valor: #saldo do instanciado
            return ("Não existe saldo suficiente")
        else:
            contaDestino.depositar(valor) #vc seleciona qual a conta destino na hora e aqui ela faz o depósito
            self.saldo -= valor #o valor da conta instanciada é subtraído 
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()]) 
            return("Transferencia Realizada") #o de cima adiciona o registro da conta na lista de transações com o tipo, o valor e data
   
    def gerarsaldo(self):
        print(f'numero:{self.numero}, saldo: {self.saldo}')