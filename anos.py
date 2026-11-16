from datetime import datetime

ano_atual = datetime.now().year

ano = int(input('Digite o ano em que você nasceu: '))
while(ano <= 0):
    print('O ano deve ser maior do que 0!')
    ano = int(input('Digite o ano em que você nasceu: '))

idade = ano_atual - ano
print(f'Sua idade é {idade} anos.')





