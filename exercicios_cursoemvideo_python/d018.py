from math import radians, sin, cos, tan
angulo = float(input('Qual o Ângulo?'))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tg = tan(radians(angulo))
print(f'O ângulo de {angulo}º tem seno de {seno:.2f}, cosseno de {cos:.2f} e tangente de {tg:.2f}.')