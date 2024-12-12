def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            ok = True
            valor = int(n)
        else:
            print('ERRO! Digite um número')
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')