cont = 0
soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
    cont += 1
print(f'Foram somados {cont} números dando em {soma}')