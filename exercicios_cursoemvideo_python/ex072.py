ns = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito' 'nove', 'dez')
while True:
    a = int(input('Digite um número de 0 a 10: '))
    if a >= 0 and a <= 10:
        print(f'{ns[a]}')
        break
    print('Tente novamente')