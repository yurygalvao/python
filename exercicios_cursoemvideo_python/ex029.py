velocidadeCarro = int(input('Qual a sua velocidade?'))
velocidadePermitida = 80
if velocidadeCarro <= velocidadePermitida:
    print('Tenha um bom dia e dirija com cuidado!')
else:
    print(f'Você foi multado, o valor da multa é de {(velocidadeCarro - velocidadePermitida) *7} reais.')