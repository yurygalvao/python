num = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Você digitou os valores {num}')
print(f'O 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O primeiro valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O número 3 não aparece')
for n in num:
    if n % 2 == 0:
        print(n)