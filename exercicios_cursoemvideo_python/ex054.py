from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
    dn = int(input('Qual a data de nascimento? '))
    idade = atual - dn
    if idade >= 18:
        print('É maior')
        totmaior+=1
    else:
        print('É menor')
        totmenor+=1
