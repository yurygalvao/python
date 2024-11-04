cont = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Os {cont} números somados deu {s}')