#Importando a função sqrt (que calcula raiz quadrada de um número)
#do módulo cmath, que trabalha com números complexos, indo além
#dos números reais
from cmath import sqrt

a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))

delta = (b * b) - (4 * a * c)
raiz_um = (-b + sqrt(delta)) / (2 * a)
raiz_dois = (-b - sqrt(delta)) / (2 * a)

#Estrutura condicional para exibir a equação quadrática

if c <= 0:
    print(f'{a}x² + {b}x + ({c}) = 0')
elif c > 0:
    print(f'{a}x² + {b}x + {c} = 0')

#Exibição dos valores das raízes obtidas
print(f'Primeira raiz: {raiz_um}')
print(f'Segunda raiz: {raiz_dois}')

