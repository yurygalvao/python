galera = []
dados = []
mai = men = 0
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]    
    galera.append(dados[:])
    dados.clear()
    resp = input('Quer continuar? [S/N] ').lower()
    if resp in 'n':
        break
print(f'Foram cadastradas {len(galera)} pessoas')
print(f'O maior peso foi {mai}Kg', end='')
for p in galera:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
        print()
print(f'O menor peso foi {men}', end='')
for p in galera:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()