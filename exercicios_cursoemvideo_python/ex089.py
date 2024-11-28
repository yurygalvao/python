ficha = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) /2
    ficha.append([nome, [nota1, nota2], media])
    resp = input('Quer continuar? [S/N] ').lower()
    if resp in 'n':
        break
print(f'{'No.':<4}{'Nome':<10}{'Média':>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar nota de qul aluno? (999 interrompe) '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')