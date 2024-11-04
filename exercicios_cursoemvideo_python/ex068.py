from random import randint
cont = s = 0
while True:
    computador = randint(0, 10)
    n = int(input('Digite um número: '))
    pi = input('Par ou Ímpar? [P/I] ')
    if pi in 'Pp':
        s = computador + n
        if s % 2 == 0:
            print(f'Você jogou {n} e o computador {computador}')
            print('Você ganhou!')
            print('Jogue novamente!')
            cont += 1
        else:
            print(f'Você jogou {n} e o computador jogou {computador}')
            print('Você perdeu!')
            break
    if pi in 'Ii':
        s = computador + n
        if s % 2 == 1:
            print(f'Você jogou {n} e o computador jogou {computador}')
            print('Você ganhou!')
            print('Jogue novamente!')
            cont += 1
        else:
            print(f'Você jogou {n} e o computador jogou {computador}')
            print('Você perdeu!')
            break
print(f'Você ganhou {cont} vezes')