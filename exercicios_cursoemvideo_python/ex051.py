p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = p + 10 * r
for i in range(p, d, r):
    print(i)