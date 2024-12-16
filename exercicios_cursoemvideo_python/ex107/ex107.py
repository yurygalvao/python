from ex107 import moeda

n = int(input('Digite um valor:'))
print(f'o número é {n}')
print(f'O dobro é {moeda.dobro(n)}, a metade é {moeda.metade(n)}')
print(f'Aumentando 10% fica {moeda.aumentar(n)} e diminuindo 10% fica {moeda.diminuir(n)}')