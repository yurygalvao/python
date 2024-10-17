vdc = float(input('Valor da casa: '))
salario = float(input('Qual o seu salário? '))
parcelamento = float(input('Em quantos anos quer parcelar? '))
parcela = (vdc/(parcelamento * 12))
porcentagem = salario * 30/100
if parcela <= porcentagem:
    print('Aprovado')
else:
    print('Reprovado')