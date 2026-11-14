#Programa que calcula operações dentre as disponíveis com dois números inteiros

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print(" 0 - SOMA")
print(" 1 - SUBTRAÇÃO")
print(" 2 - MULTIPLICAÇÃO")
print(" 3 - DIVISÃO")
print(" 4 - DIVISÃO INTEIRA")
print(" 5 - MÓDULO (RESTO DA DIVISÃO)")
print(" 6 - POTENCIAÇÃO")
print(" 7 - RADICIAÇÃO")

choice = int(input("Sua escolha de operação: "))

while(choice > 7 or choice < 0):
    choice = int(input("Sua escolha de operação: "))

# Estrutura match que funciona como se fosse um switch case, mas in Python

match choice:
    case 0:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    case 1:
        diferenca = n1 - n2
        print(f'{n1} - {n2} = {diferenca}')
    case 2:
        produto = n1 * n2
        print(f'{n1} * {n2} = {produto}')
    case 3:
        quociente = n1 / n2
        print(f'{n1} / {n2} = {quociente}')
    case 4:
        quociente_inteiro = n1 // n2
        print(f'{n1} // {n2} = {quociente_inteiro}')
    case 5:
        resto = n1 % n2
        print(f'{n1} % {n2} = {resto}')
    case 6:
        fator = n1 ** n2
        print(f'{n1} ** ({n2}) = {fator}')
    case 7:
        raiz = n1 ** (1/n2)
        print(f'{n1} ** (1/{n2}) = {raiz}')



