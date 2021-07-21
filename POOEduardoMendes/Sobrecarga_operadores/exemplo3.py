
class ListaLO(list):
    def __add__(self, val):
        #Soma todos os itens da lista com val
        return ListaLO([x + val for x in self])

    def __lshift__(self, val):
        #Fazer .apoend na lista usando <<
        self.append(val)

    def __rshift__(self, pos):
        """Remove um item com >>"""
        return self.pop(pos)
    
    def __neg__(self):
        return ListaLO(reversed(self))