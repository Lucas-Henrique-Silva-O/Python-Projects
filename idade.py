from datetime import datetime, timedelta
#Programa que calcula a idade (os anos, os meses e os dias) a partir da data de nascimento da pessoa

while(True):
    ano_atual = datetime.now().year
    mes_atual = datetime.now().month
    dia_atual = datetime.now().day
    data_atual = datetime.now()
    

    ano = int(input('Digite o ano em que você nasceu: '))
    mes = int(input('Digite o mês em que você nasceu: '))
    while(mes <= 0 or mes > 12):
        print('Valor inválido para o mês! Entre 1 e 12!')
        mes = int(input('Digite o mês em que você nasceu: '))

    dia = int(input('Digite o dia em que você nasceu: '))
    #Listas para forçar o usuário a colocar dias válidos, conforme o número de meses
    meses_tum = [1, 3, 5, 7, 9, 11]
    meses_trinta = [4, 6, 8, 10, 12]
    if(mes == 2):
        if(ano % 4 == 0 and ano % 100 != 0):
            while(dia > 29 or dia <= 0):
                print('Valor inválido! Faixa de dias aceita: 1 a 29!')
                dia = int(input('Digite o dia em que você nasceu: '))
        elif(ano % 4 == 0 and ano % 100 == 0):
              if(ano % 400 == 0):
                    while(dia > 29 or dia <= 0):
                                    print('Valor inválido! Faixa de dias aceita: 1 a 29!')
                                    dia = int(input('Digite o dia em que você nasceu: '))
              else:
                     while(dia > 28 or dia <= 0):
                                     print('Valor inválido! Faixa de dias aceita: 1 a 28!')
                                     dia = int(input('Digite o dia em que você nasceu: '))

                    
    elif(mes in meses_tum):
        while(dia > 31 or dia <= 0):
                    print('Valor inválido! Faixa de dias aceita: 1 a 31!')
                    dia = int(input('Digite o dia em que você nasceu: '))
    elif(mes in meses_trinta):
         while(dia > 30 or dia <= 0):
                             print('Valor inválido! Faixa de dias aceita: 1 a 30!')
                             dia = int(input('Digite o dia em que você nasceu: '))

    

    #Cálculo da idade
    ano_idade = ano_atual - ano
    mes_idade = mes_atual - mes
    dia_idade = dia_atual - dia

    

    #Verificações para casos em que ano_idade e dia_idade forem negativos
    if(dia_idade < 0):
            mes_idade -= 1
            ult_dia_mes_antecessor = datetime(ano_atual, mes_atual, 1) - timedelta(days=1)
            numero_dias_mes_antecessor = ult_dia_mes_antecessor.day
            dia_idade += ult_dia_mes_antecessor.day
    if(mes_idade < 0):
           ano_idade -= 1
           mes_idade += 12

    print(f'Idade: {ano_idade}, {mes_idade} meses e {dia_idade} dias')

    r = int(input('Deseja continuar? 0 - NÃO/ 1 - SIM'))
    
    while(r!= 0 and r!= 1):
            r = int(input('Deseja continuar? 0 - NÃO/ 1 - SIM'))
    if(r == 0):
            break


