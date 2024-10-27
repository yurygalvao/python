pt = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = pt
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -- ', end='')
        termo += razão
        cont += 1
    mais = int(input('Quer mostrar mais quantos termos?'))
print(f'{total} termos foram mostrados')