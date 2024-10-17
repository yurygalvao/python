produto = float(input('Qual o preço? '))
cdp = int(input('Como vai pagar? 1- A vista  2- A vista cartão  3-Em até 2x  4- 3x ou mais'))
if cdp == 1:
    print(f'O valor ficou de {produto - (produto * 10 / 100)}')
elif cdp == 2:
    print(f'O valor ficou de {produto - (produto * 5 / 100)}')
elif cdp == 3:
    print(f'O valor ficou de {produto}')
elif cdp == 4:
    print(f'O valor ficou de {produto + (produto * 20 / 100)}')
else:
    print('Condição de pagamnto inválida')