
print('---'*15)
print('Calculadora com números reais')
print('---'*15)

while(True):
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))

    print('Escolha a operação desejada:')
    print('0 - SUBTRAÇÃO')
    print('1 - ADIÇÃO')
    print('2 - MULTIPLICAÇÃO')
    print('3 - DIVISÃO')
    print('4 - POTENCIAÇÃO')
    choice = int(input('Digite a sua escolha: '))

    while( choice < 0 or choice > 4):
        print('Escolha inválida! 0 a 4!')
        choice = int(input('Digite a sua escolha: '))

    if(choice == 0):
        diferenca = n1 - n2
        print(f'A diferença entre {n1} e {n2} é {diferenca}.')
        print(f'{n1} - {n2} = {diferenca}.')
    elif(choice == 1):
        soma = n1 + n2
        print(f'A soma de {n1} com {n2} é igual a {soma}.')
        print(f'{n1} + {n2} = {soma}.')
    elif(choice == 2):
        produto = n1 * n2
        print(f'O produto de {n1} por {n2} é igual a {produto}.')
        print(f'{n1} * {n2} = {produto}.')
    elif(choice == 3):
        quociente = n1 / n2
        print(f'{n1} dividido por {n2} é igual a {quociente}.')
        print(f'{n1} / {n2} = {quociente}.')
    elif(choice == 4):
        potencia = n1 ** n2
        print(f'{n1} elevado a {n2} é igual a {potencia}.')
        print(f'{n1} ^ {n2} = {potencia}.')

    print('0 - CONTINUAR')
    print('1 - PARAR')
    c = int(input('Deseja continuar ou parar: '))
    while( c != 0 and c != 1):
        print('Opção inválida! 0 ou 1!')
        print('0 - CONTINUAR')
        print('1 - PARAR')
        c = int(input('Deseja continuar ou parar: '))

    if(c == 1):
        break

