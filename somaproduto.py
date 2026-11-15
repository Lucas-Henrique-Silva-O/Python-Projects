#Importando a função prod para obter o produto dos termos inseridos pelo usuário
from math import prod

#Entrada para a quantidade de números
y = int(input('Digite a quantidade de números que você deseja somar e multiplicar: '))
#Criando uma lista para guardar os números inseridos pelo usuário
numeros = []
#Estrutura while para garantir que a quantidade seja maior do que zero
while( y <= 0):
    print('A quantidade deve ser maior do que zero!')
    y = int(input('Digite a quantidade de números que você deseja somar e multiplicar: '))



#For para inserir os números digitados pelo usuário na lsta criada
for i in range(0, y):
    n = int(input(f'Digite o {i+1}º: '))
    numeros.append(n)
#Função sum para somar todos os termos inseridos pelo usuário
soma = sum(numeros)
produto = prod(numeros)
print(f'A soma dos números inseridos é igual a {soma}.')
print(f'O produto dos números inseridos é igual a {produto}.')