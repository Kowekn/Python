from contas import Conta
import datetime

class ContaEspecial(Conta): #classe de HERANÇA
    def __init__(self,clientes,numero,saldo,limite):#ainda é preciso infromar cada um dos atributos
        Conta.__init__(self,clientes,numero,saldo) #sobrescever os atributos repetidos, importando-os da superclasse Conta, 
        self.limite = limite  #para regular o saque
    def sacar(self, valor): #método de mesmo nome, considerado override de métodos, quando sacar é chamado de ContaEspecial, 
        if (self.saldo + self.limite) < valor: #terá esse comportamento:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()]) #registrando no extrato
            return True