n = int(input('Qual número quer converter?'))
base = int(input('1 - Binário  2 - Octal  3 - Hexadecimal : '))
if base == 1:
    print(f'{n} convertido para binário é {bin(n)[2:]}')
elif base == 2:
    print(f'{n} convertido para Octal é {oct(n)[2:]}')
elif base == 3:
    print(f'{n} convertido para Hexadecimal é {hex(n)[2:]}')
else:
    print('Erro na conversão escolhida')