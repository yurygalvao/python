def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = input('Função ou biblioteca > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!')
