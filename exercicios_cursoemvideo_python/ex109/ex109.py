from ex109 import moeda

n = int(input('Digite um valor:'))
print(f'o número é {moeda.moeda(n, True)}')
print(f'O dobro é {moeda.dobro(n, True)}, a metade é {moeda.metade(n, True)}')
print(f'Aumentando 10% fica {moeda.aumentar(n, True)} e diminuindo 10% fica {moeda.diminuir(n, True)}')