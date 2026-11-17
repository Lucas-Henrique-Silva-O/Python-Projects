#Programa para calcular os números pares

while(True):
    q = int(input('Digite a quantidade de números pares que deve ser exibida: '))
    while(q <= 0):
        print('A quantidade deve ser maior do que zero!')
        q = int(input('Digite a quantidade de números pares que deve ser exibida: '))

    for i in range(1, (1+q)):
        if( (i % 2) == 0):
            print(f'{i}')

    r = int(input('Deseja continuar? [0 - NÃO/1 - SIM] '))
    while(r != 0 and r != 1):
        print('Respota inválida! 0 ou 1!')
        r = int(input('Deseja continuar? [0 - NÃO/1 - SIM] '))

    if(r == 0):
        print('Encerrando...')
        break
