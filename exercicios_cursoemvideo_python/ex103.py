def ficha(a='<desconhecido>', b=0):
    print(f'O {a} fez {b} gol(s)')

jogador = input('Nome do jogador: ')    
gols = input('Gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    ficha(b = gols)
else:
    ficha(jogador, gols)
