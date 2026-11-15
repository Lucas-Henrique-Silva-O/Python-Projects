q = int(input('Digite quantos números você deseja somar: '))
while(q <= 0):
    print('A quantidade deve ser maior do que zero!')
    q = int(input('Digite quantos números você deseja somar: '))

soma = 0
for i in range(1, q+1):
    n = int(input(f'Digite o {i}º número: '))
    soma += n

print(f'A soma dos números é igual a {soma}.')