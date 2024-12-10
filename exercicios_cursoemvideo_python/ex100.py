from random import randint
lista = []
def sorteia():
    for i in range(0, 5):
        lista.append(randint(0,9))
    print(lista)
def somaPar():
    pares = 0
    for i in lista:
        if i % 2 == 0:
            pares += i
    print(f'A soma dos pares foi {pares}')
sorteia()
somaPar()