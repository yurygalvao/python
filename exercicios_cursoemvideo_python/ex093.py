jogador = {}
jogador['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador['nome']} disputou? '))
gol = []
total = 0
for i in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {i+1}? '))
    total += gols
    gol.append(gols)
jogador['gols'] = gol
jogador['total'] = total
print(jogador)
print()
print('-'*50)
print()
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print()
print('-'*50)
print()
print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')
for i, j in enumerate(gol):
    print(f'Na partida {i}, fez {j} gols.')
print(f'Foi um total de {jogador['total']}')