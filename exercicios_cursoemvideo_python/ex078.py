lista = []
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
print(f'Os valores digitados foi {lista}')
print(f'O maior valor foi {mai} nas posições')
for i, v in enumerate(lista):
    if v == mai:
        print(i)
print(f'O menor valor foi {men} nas posições')
for i, v in enumerate(lista):
    if v == men:
        print(i)