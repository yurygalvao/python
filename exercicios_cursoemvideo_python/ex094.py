galera = []
pessoa ={}
soma = media = 0
while True:
    pessoa.clear
    pessoa['nome'] = input('Nome:')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    while True:
        pessoa['sexo'] = input('Sexo: [M/F] ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Apenas M ou F.')
    galera.append(pessoa.copy()) 
    while True:
        resp = input('Quer continuar? [S/N]').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Apenas S ou N')
    if resp == 'N':
        break

print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A média de idade é de {media}')
print('As mulheres cadastradas foram: ' end='')
for p in galera:
    if p['sexo'] =='F':
        print(f'p{"nome"}, ')
print('Lista de pessoas que estão acima da média: ' end='')
for p in galera:
    if p['idade'] > media:
        print(f'p["nome"]')