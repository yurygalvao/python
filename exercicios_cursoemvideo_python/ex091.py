from random import randint
from operator import itemgetter
ranking = []
jogadas = { 'jogador1' : randint(1,6),
            'jogador2' : randint(1,6),
            'jogador3' : randint(1,6),
            'jogador4' : randint(1,6)}
print('Valores sorteados: ')
for k, v in jogadas.items():
    print(f'{k} tirou {v} no dado')
print('-'*30)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')