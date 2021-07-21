

class Pizza:

    pedacos = 8

    def __init__(self, sabor):
        self.sabor = sabor

    def pegar_pedacos(self):
        '''Metodo de Instância'''
        self.pedacos -= 1

    @classmethod
    def mudar_tamanho(cls, pedacos):
        cls.pedacos = pedacos

    @staticmethod
    def ingredientes():
        return 'Ingredientes'


class Mussarela(Pizza):

    @staticmethod
    def ingredientes():
        return ['queijo', 'cebola','mussarela']

class Queijo(Pizza):
    pass

class Frango(Pizza):
    pass

class Portuguesa(Pizza,Queijo):
    pass


