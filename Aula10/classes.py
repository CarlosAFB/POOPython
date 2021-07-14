class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclass = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclass} Falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclass} Comprando...')


class Aluno(Pessoa):
    def estudando(self):
        print(f'{self.nomeclass} Estudando...')
