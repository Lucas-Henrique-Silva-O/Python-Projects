
#Programa para calcular a média de um número inserido pelo usuário de notas

while(True):
    #Variável para guardar as notas
    total = 0
    #Quantidade de notas
    qn = int(input('Quantidade de notas: '))
    while(qn <= 0):
        print('Quantidade de notas deve ser maior do que zero (0)!')
        qn = int(input('Quantidade de notas: '))

    for i in range(0, qn):
        nota = float(input(f'Digite a {i+1}ª nota: '))
        total += nota

    media = total / qn
    print(f'A sua média é {media}.')
    response = input('Deseja continuar? [Y/N] ').upper().strip()
    while(response != 'Y' and response != 'N'):
        print('A sua resposta deve ser Y ou N!')
        response = input('Deseja continuar? [Y/N] ').upper().strip()

    if(response == 'N'):
        break
    




