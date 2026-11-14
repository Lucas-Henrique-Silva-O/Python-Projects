from math import sqrt
from cmath import sqrt

print(' 0 - RAÍZES REAIS')
print(' 1 - RAÍZES COMPLEXAS')
escolha = int(input('Você quer que sejam calculadas apenas raízes reais ou ' \
'incluir complexas não imaginárias puras também?[0/1] '))

while(escolha < 0 or escolha > 1):
    print('Escolha inválida! 0 ou 1!')
    escolha = int(input('Você quer que sejam calculadas apenas raízes reais ou' \
    'incluir complexas não imaginárias puras também?[0/1] '))

if(escolha == 0):
    while(True):
        a = float(input('Digite o coeficiente a: '))
        b = float(input('Digite o coeficiente b: '))
        c = float(input('Digite o coeficiente c: '))

        delta = (b * b) - (4 * a * c)


        if(c >= 0):
            print(f'{a}x² + {b}x + {c} = 0')
        else:
            print(f'{a}x² + {b}x + ({c}) = 0')
    
        if(delta == 0):
            raiz= -(b) / (2 * a)
            print(f'Ambas as raízes da equação são: {raiz}')
        elif(delta > 0):
            raiz_um = -(b) + sqrt(delta) / (2 * a)
            raiz_dois = -(b) - sqrt(delta) / (2 * a)
            print(f'Primeira raiz da equação: {raiz_um}.')
            print(f'Segunda raiz da equação: {raiz_dois}.')
        else:
            print('A equação não possui raízes reais.')
        
        p = input('Deseja continuar?[Y/N] ').strip().upper()
        

        while(p != 'Y' and p != 'N'):
            print('Opção inválida! Y ou N')
            p = input('Deseja continuar?[Y/N] ').strip().upper()

        if(p == 'N'):
            print('Programa parando...')
            break;
else:
    while(True):
        a = float(input('Digite o coeficiente a: '))
        b = float(input('Digite o coeficiente b: '))
        c = float(input('Digite o coeficiente c: '))

        delta = (b * b) - (4 * a * c)
        raiz_um = (-b + sqrt(delta)) / (2 * a)
        raiz_dois = (-b - sqrt(delta)) / (2 * a)

        if c <= 0:
            print(f'{a}x² + {b}x + ({c}) = 0')
        elif c > 0:
            print(f'{a}x² + {b}x + {c} = 0')

        print(f'Primeira raiz: {raiz_um}')
        print(f'Segunda raiz: {raiz_dois}')


        #Usando os métodos strip e upper para garantir que o usuário digite Y ou N
        p = input('Deseja continuar?[Y/N] ').strip().upper()
        

        while(p != 'Y' and p != 'N'):
            print('Opção inválida! Y ou N')
            p = input('Deseja continuar?[Y/N] ').strip().upper()

        if(p == 'N'):
            print('Programa parando...')
            break;


