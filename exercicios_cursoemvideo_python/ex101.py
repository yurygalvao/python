import datetime
anoAtual = datetime.date.today().year
def voto():
    dataDeNascimento = int(input('Data de nascimento: '))
    poder = ''
    idade = anoAtual - dataDeNascimento
    if idade < 16:
        poder = 'Não pode votar'
    elif 16 <= idade < 18 or idade >= 65:
        poder = 'Voto opcional'
    elif 18 <= idade < 65:
        poder = 'Voto obrigatório'
    print(f'Com {idade} anos. {poder}')

voto()