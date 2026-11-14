from math import sqrt


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


