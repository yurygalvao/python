import math
catetoo = float(input('Cateto oposto: '))
catetoa = float(input('Cateto adjacente: '))
catetooo = catetoo**2
catetoao = catetoa**2
hip = catetooo + catetoao
hipp = hip**(1/2)
print(f'A hipotenusa é {hipp}')