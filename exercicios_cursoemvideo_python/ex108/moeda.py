def dobro(n):
    d = n*2
    return d

def aumentar(n):
    a = n + (n*10/100)
    return a

def metade(n):
    m = n/2
    return m

def diminuir(n):
    d = n - (n*10/100)
    return d

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')