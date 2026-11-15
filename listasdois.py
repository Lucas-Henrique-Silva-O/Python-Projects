#Programa para exibir os números divisíveis por um número natural n

n = int(input('Qual número natural não-nulo você deseja usar como divisor? '))
while(n <= 0):
    print('O número deve ser maior do que zero!')
    n = int(input('Qual número natural não-nulo você deseja usar como divisor? '))


q = int(input(f'Qual deve ser o maior valor da lista dos números divisíveis por {n}? '))
while( q <= 0):
    print('A quantidade deve ser maior do que 0!')
    q = int(input(f'Qual deve ser o maior valor da lista dos números divisíveis por {n}? '))

divisiveis = list(filter(lambda x: x % n == 0, range(q+1)))

print(f'A lista dos números divisíveis por {n} é {divisiveis}.')


#numeros_pares_dois = list(filter(lambda x: x % 2 == 0, range(10)))