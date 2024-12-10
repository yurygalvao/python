def Area():
    altura = float(input('Altura: '))
    largura = float(input('Largura: '))
    mostrar = print(f'A área de um terreno de {altura} x {largura} é de {altura*largura}m2')
    return mostrar
Area()