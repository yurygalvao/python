r1 = float(input('Digite o segmento: '))
r2 = float(input('Digite o segmento: '))
r3 = float(input('Digite o segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma triângulo')
else:
    print('Nâo forma triângulo')

if r1 == r2 == r3:
    print('Equilátero')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Isósceles')
else:
    print('Escaleno')