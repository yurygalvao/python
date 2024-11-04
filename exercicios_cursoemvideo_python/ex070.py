total = maisde1000 = barato = cont = baratonome = 0
while True:
    nome = input('Nome do produto: ')
    preço = float(input('Preço: '))
    total += preço
    if cont == 0:
        barato = preço
        baratonome = nome
        cont += 1
    elif cont > 0 and preço < barato:
        barato = preço
        baratonome = nome
    if preço >= 1000:
        maisde1000 += 1
    continuar = input('Quer continuar? [S/N] ')
    if continuar in 'Nn':
        break
print(f""" 
O total da compra foi {total} reais
Temos {maisde1000} produtos custando 1.000
O produto mais barato foi {baratonome} e custou {barato} reais
""")

