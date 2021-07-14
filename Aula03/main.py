from random import randint

class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Metodo de Instancia
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # Metodo de Classe
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    #Metodo Estático
    @staticmethod
    def gera_id():
        rand = randint(1000, 1999)
        return rand


# p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.nome, p1.idade)
# print(p1.idade)
p1.get_ano_nascimento()

print(Pessoa.gera_id())
print(p1.gera_id())