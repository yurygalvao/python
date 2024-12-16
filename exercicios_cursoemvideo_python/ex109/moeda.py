def dobro(n=0, format=False):
    d = n*2
    return d if format is False else moeda(d)

def aumentar(n=0, taxa=0, format=False):
    a = n + (n*taxa/100)
    return a if format is False else moeda(a)

def metade(n=0, format=False):
    m = n/2
    return m if format is False else moeda(m)

def diminuir(n=0, taxa=0, format=False):
    d = n - (n*taxa/100)
    return d if format is False else moeda(d)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')