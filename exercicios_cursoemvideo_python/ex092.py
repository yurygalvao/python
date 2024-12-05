cadastro = {}
while True:
    cadastro['nome'] = input('Nome: ')
    cadastro['idade'] = int(input('Ano de nascimento: '))
    cadastro['idade'] = 2024 - cadastro['idade'] 
    cadastro['ctps'] = int(input('Carteira de trabalho: (0 se não tiver)'))
    if cadastro['ctps'] == 0:
        break
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: '))
    cadastro['aposentadoria'] = cadastro['idade'] + 35
    break
for k, v in cadastro.items():
    print(f'{k} tem o valor de {v}')