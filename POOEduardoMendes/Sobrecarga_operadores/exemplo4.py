
class ListaLO():
    def __init__(self, l):
        self.l =l or []
    
    def __add__(self, val):
        #Soma todos os itens da lista com val
        return ListaLO([x + val for x in self.l])

    def __lshift__(self, val):
        #Fazer .apoend na lista usando <<
        self.l.append(val)

    def __rshift__(self, pos):
        """Remove um item com >>"""
        return self.l.pop(pos)
    
    def __neg__(self):
        return ListaLO(reversed(self.l))

    def __iadd__(self, val):
        #Soma todos os itens  da lista  com val e mantem no obj
        self.l =  ListaLO([x + val for x in self])