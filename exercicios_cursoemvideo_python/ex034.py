salario = float(input('Qual o seu salário? '))
if salario <= 1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario *10/100)
print(f'Seu novo salário é de {novo} reais')