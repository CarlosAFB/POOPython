class Pizzaria:
    def __init__(self):
        self._forno = Forno()

    def pedido(self, pizza):
        self._forno.assar(pizza)

class Forno:
    def __init__(self):
        self.pizzas = []
        self.lenha = None

    def assar(self):
        if not self.lenha:
            print()