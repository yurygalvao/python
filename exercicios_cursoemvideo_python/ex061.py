pt = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = pt
cont = 1
while cont <= 10:
    print(f'{termo} -- ', end='')
    termo += razão
    cont += 1
