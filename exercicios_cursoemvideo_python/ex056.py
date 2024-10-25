idades = 0
media = 0
maior = 0
homem_velho = ''
mulher20 = ''
for i in range(1, 5):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo : [M/F] ').upper()
    idades += idade
    if i == 1 and sexo in 'Mm':
        maior = idade
        homem_velho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        homem_velho = nome
        if sexo in 'Ff' and idade < 20:
            mulher20 += 1
media = idades/4
print(f'A médias das idades é {media} anos.')
print(f'O homem mais velho é {homem_velho}.')
print(f'Tem {mulher20} mulheres abaixo de 20 anos')