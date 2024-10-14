d = float(input('Quantos km tem a sua viagem? '))
if d <= 200:
    print(f'O preço da passagem é {d*0.5} reais.')
else:
    print(f'O preço da sua passagem é {d*0.45} reais.')