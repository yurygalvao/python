n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''[1] Soma
    [2] Multiplicação
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')
    opção = int(input('Qual a sua opção?'))
    if opção == 1:
        print(f'A soma de {n1} + {n2} = {n1 + n2}')
    elif opção == 2:
        print(f'A multiplicação de {n1} * {n2} = {n1 * n2}')
    elif opção == 3:
        if n1 > n2:
            print(f'O maior é {n1}')
        elif n2 > n1:
            print(f'O {n2} é maior')
        else:
            print('Os números são iguais')
    elif opção == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        break
    else:
        print('Opção inválida, tente novamente')
print('Acabou!')