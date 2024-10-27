from random import randint
numero_aleatorio = randint(0, 10)
tentativa = 1
chute = int(input('Digite seu chute: '))
if chute >= 0 and chute <= 10:
    while chute != numero_aleatorio:
        if chute > numero_aleatorio:
            print('Menos, tente outra vez')
            chute = int(input('Digite seu chute: '))
            tentativa += 1
        else:
            print('Mais, tente outra vez')
            chute = int(input('Digite seu chute: '))
            tentativa += 1
    print(f'Parabéns, vocẽ acertou com {tentativa} tentativas')
else:
    print('Chute inválido')