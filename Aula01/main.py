from pessoa import Pessoa

p1 = Pessoa('Pedro', 22)
p2 = Pessoa('João', 32)

p1.falar('POO')
p1.comer('Carne')
p2.comer('Sorvete')


print(p1.ano_atual)
print(p2.ano_atual)
print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())