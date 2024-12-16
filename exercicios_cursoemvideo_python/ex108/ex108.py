from  ex108 import moeda

n = int(input('Digite um valor:'))
print(f'o número é {moeda.moeda(n)}')
print(f'O dobro é {moeda.moeda(moeda.dobro(n))}, a metade é {moeda.moeda(moeda.metade(n))}')
print(f'Aumentando 10% fica {moeda.moeda(moeda.aumentar(n))} e diminuindo 10% fica {moeda.moeda(moeda.diminuir(n))}')