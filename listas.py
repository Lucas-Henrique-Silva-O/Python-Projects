#Programa para gerar uma determinada quantidade de números pares e ímpares

k = int(input('Quantos números pares e ímpares você deseja que sejam exibidos? '))
while(k <= 0):
    print('A quantidade deve ser maior do que zero!')
    k = int(input('Quantos números pares e ímpares você deseja que sejam exibidos? '))



# Gerando as listas usando o valor inserido pelo usuário
pares = [l for l in range(k) if l % 2 == 0]
impares = [p for p in range(k) if p % 2 != 0]



print(f'Lista de números pares: {pares}')
print(f'Lista de números ímpares: {impares}')

