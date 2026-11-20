#Programa para calcular tabuada de números inteiros

numero = int(input('Digite um número inteiro para ver sua tabuada: '))
print(f'TABUADA DO {numero}: ')

for i in range(0, 11):
    print(f'{numero} x {i} = {numero * i}')