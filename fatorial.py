while(True):
    numero = int(input('Digite um número natural igual ou maior do que zero: '))
    while(numero < 0):
        print('Número natural igual ou maior do que zero!')
        numero = int(input('Digite um número natural igual ou maior do que zero: '))


    fatorial = 1

    if(numero == 0 or numero == 1):
        fatorial = 1
    else:
        for i in range(1, (numero + 1)):
            fatorial *= i

    print(f'O resultado de {numero}! é {fatorial}')

    a = int(input('Deseja continuar? [1 - SIM / 0 - NÃO] '))

    while(a != 1 and a != 0):
        print('Resposta inválida! 1 ou 0!')
        a = int(input('Deseja continuar? [1 - SIM / 0 - NÃO] '))

    if(a == 0):
        print('Encerrando...')
        break



