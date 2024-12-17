def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('ERRO! Digite um número válido')
            continue
        else:
            return n
        
def leiaReal(msg):
    while True:
        try:
            n = float(input(msg))
        except:
            print('ERRO! Digite um número válido')
            continue
        else:
            return n 
        

n = leiaInt('Digite um número inteiro: ')
c = leiaReal('Digite um número real:')
print(f'O número interio foi {n} e o real foi {c}')