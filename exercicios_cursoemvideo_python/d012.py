valor = float(input('Qual o valor do produto?'))
desconto = (valor * 5)/100
vcd = valor - desconto
print(f'O produto custa {valor} reais, com desconto de 5% fica {vcd} reais')