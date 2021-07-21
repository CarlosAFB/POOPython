  ##Operadores Infixos

class Numero:
    
    def __init__(self, val):
        self.val = val 

    def __add__(self, other):
        return self.val + other

    def __radd__(self, other):
        return other + self.val

    def __sub__(self, other):
        pass

    def __lt__(self, other):
        pass