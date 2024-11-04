mais18 = homens = mulher20= 0
while True: 
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ')
    continuar = input('Quer continuar? [S/N] ')
    if continuar in 'Nn':
        break
    if idade >= 18:
        mais18 += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade <= 20:
        mulher20 += 1
print(f''' 
Total de pessoas com mais de 18 anos: {mais18}
Ao todo temos {homens} homens cadastrados
E temos {mulher20} mulheres com menos de 20 anos
''')