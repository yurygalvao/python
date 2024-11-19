lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    cont = input('Quer continuar? [S/N]').lower()
    if cont in 'n':
        break
print(f'Você digitou {len(lista)} números')
lista.sort(reverse=True)
print(f'Em ordem decrescente {lista}')
if 5 in lista:
    print('Tem o 5')
else:
    print('Não tem o 5')    