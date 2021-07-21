class Fila:
    """Abstração de qualquer tipo de Fila:
        -Supermercados
        -Processos
        - ...
    """

    c_fila = []

    def __init__(self):
        self.s_fila = []

    @classmethod
    def c_entrar(cls, obj):
        cls.c_fila.append(obj)
        print(cls.c_fila)
