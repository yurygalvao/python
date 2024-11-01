resp = 'S'
maior = menor = cont = soma = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = input('Quer continuar? [S/N]').upper().strip()[0]
media = soma/cont
print(f'A média entre os números foi {media}, o maior número foi {maior} e o menor foi {menor}')