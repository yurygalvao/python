lista = []
pares = []
impares = []
for i in range (1,8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    lista.append(pares)
    lista.append(impares)
print(f'Os pares foram: {lista[0]}')
print(f'Os ímpares foram: {lista[1]}')