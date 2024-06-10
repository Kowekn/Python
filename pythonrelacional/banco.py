from cliente import ContaCliente
from extratos import Extrato


class Banco():
    def __init__(self, codigo,nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def adicionaconta(self,contacliente):
        self.contas.append(contacliente)

    def calcularendimentomensal(self):
        for c in self.contas:
            c.CalculoRendimento() 
    def imprimesaldocontas(self):
        for c in self.contas:
            c.Extrato()
