#class ContaCliente:

 #   def __init__(self, numero, IOF, IR, valorinvestido, taxarendimento):
 #       self.numero = numero
  #      self.IOF = IOF
  #      self.IR = IR
   #     self.valorinvestido = valorinvestido
  #      self.taxarendimento = taxarendimento

  #  def CalculoRendimento(self):
  #      self.valorinvestido += (self.valorinvestido * self.taxarendimento)
  #      self.valorinvestido = (self.valorinvestido - (self.taxarendimento * self.IOF* self.IR))

 #   def Extrato(self): 
  #      print (f"O saldo atual da conta {self.numero} é {self.valorinvestido:10.2f}")
from abc import ABC, abstractmethod #classes abstratas
class ContaCliente(ABC):
    def __init__(self,numero,IOF,IR,valorinvestido,taxarendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorinvestido = valorinvestido
        self.taxarendimento = taxarendimento
    @abstractmethod
    def CalculoRendimento(self): #essa classe serve para dizer o método presente em suas subclasses 
        pass

     