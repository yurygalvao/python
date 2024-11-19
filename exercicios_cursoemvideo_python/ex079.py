lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Esse valor não pode ser adicionado')
    cont = input('Quer continuar? [S/N]').strip().lower()
    if cont in 'n':
        break
lista.sort()
print(f'{lista}')