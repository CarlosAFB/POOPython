from POOLive import Fila

superpercado = Fila()

superpercado.entrar('Pedro')
superpercado.entrar('José')
superpercado.entrar('Gean')

print(superpercado.fila)

superpercado.sair()
superpercado.sair()

print(superpercado.fila)


