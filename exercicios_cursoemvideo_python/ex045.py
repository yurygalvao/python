from random import randint
print('''
[1] - Pedra
[2] - Papel
[3] - Tesoura''')
computador = randint(1,3)
jogada = int(input('Qual a sua jogada?'))
print(f'A jogada do computador é {computador}')
if jogada < 1 or jogada > 3:
    print('Jogada inválida')
    
if jogada >= 1 and jogada <= 3:    
    if computador == 1:
        if jogada == 1:
            print('Empate')
        elif jogada == 2:
            print('Você ganhou!')
        else:
            print('Você perdeu!')
    elif computador == 2:
        if jogada == 1:
            print('Você perdeu!')
        elif jogada == 2:
            print('Empate')
        else:
            print('Você ganhou!')
    elif computador == 3:
        if jogada == 1:
            print('Você ganhou!')
        elif jogada == 2:
            print('Você perdeu!')
        else:
            print('Empate')