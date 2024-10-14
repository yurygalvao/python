from random import randint
computador = randint(0, 5)
jogador = int(input('Em que número eu pensei?'))
if jogador == computador:
    print('Você acertou!')
else:
    print(f'Você errou,o número pensado foi {computador}')