from datetime import date
dn = int(input('Qual o ano do seu nascimento? '))
anoAtual = date.today().year
idadeAtual = anoAtual - dn
qa = dn + 18
if idadeAtual == 18:
    print('Vá se alistar imediatamente')
elif idadeAtual < 18:
    print(f'Você irá se alistar em {qa} faltam {qa - anoAtual} anos')
else:
    print(f'Você deveria ter se alistado em {qa}, ja se passaram {anoAtual - qa} anos')


