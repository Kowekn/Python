from contas import Conta
from poupanca import Poupanca

class Remunerada(Conta, Poupanca): 
    def __init__(self, taxaremuneracao, clientes, numero, saldo):
        Conta.__init__(self,clientes,numero,saldo) 
        Poupanca.__init__(self,taxaremuneracao) 
        self.taxaremuneracao = taxaremuneracao

    def remuneraConta(self):
        self.saldo += self.saldo * (self.taxaremuneracao/30)
        self.saldo -= self.taxaremuneracao