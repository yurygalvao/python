jogadores = []
jogador = {}
gols = []
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols fez na partida {i+1}? '))) 
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Apenas S ou N')
    if resp == 'N':
        break
print(jogadores)
