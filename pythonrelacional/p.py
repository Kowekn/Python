from contas import Conta
from clientes import Cliente
from extratos import Extrato
from poupanca import Poupanca
from remunerada import Remunerada
from contaespecial import ContaEspecial
from banco import Banco
from cliente import ContaCliente
from comum import ContaComum
from cremunerada import ContaRemunerada

cliente1 = Cliente(12646, "pedro", "penis")
cliente2 = Cliente(12344, "joana", "pp")
cliente3 = Cliente(98797, "ssi", "lau")
conta1 = Conta([cliente1, cliente2], 777, 0)
conta2 = Conta([cliente2, cliente3], 888, 0) 
conta3 = Conta([cliente1, cliente3], 999, 0)

conta1.depositar(1000)
conta2.depositar(2000)
conta3.depositar(3000)

banco1 = Banco(999,"teste")
contacliente1 = ContaCliente (1,0.01,0.1,1000,0.05)
contacomum1 = ContaComum(2,0.01,0.1,2000,0.05)
contaremunerada1 = ContaRemunerada(3,0.01,0.1,2000,0.05)


