def maior(*num):
    cont = maior = 0
    for valor in num:
        print(f'{valor} ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor foi {maior}')
maior(1, 4, 8)