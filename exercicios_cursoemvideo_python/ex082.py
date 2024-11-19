lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    cont = input('Quer continuar? [S/N]').lower()
    if cont in 'n':
        break
print(f'A lista inteira é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')