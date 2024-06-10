class Cliente:
    def __init__(self,cpf,nome,endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
    def printar(self):
        print(f'{self.cpf}, {self.endereco}, {self.nome}')