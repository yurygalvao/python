numero = int(input('Digite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'Analisando o número {numero}')
print(f'Unidade é {u}')
print(f'Dezena é {d}')
print(f'Centena é {c}')
print(f'Milhar é {m}')

