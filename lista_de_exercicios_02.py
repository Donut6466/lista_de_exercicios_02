def questao1():
    stnumber = int(input("Digite o primeiro número: "))
    ndnumber = int(input("Digite o segundo número: "))
    rdnumber = int(input("Digite o terceiro número: "))
    conjunto = stnumber == ndnumber == rdnumber

    if stnumber > ndnumber and stnumber > rdnumber:
        print(f"{stnumber} é o maior.")
    elif ndnumber > stnumber and ndnumber > rdnumber:
        print(f"{ndnumber} é o maior.")
    elif rdnumber > stnumber and rdnumber > ndnumber:
        print(f"{rdnumber} é o maior.")
    elif conjunto == True:
        print(f"Todos são iguais")
    else: print("Ocorreu um erro. Tente novamente.")
def questao2():
    salario = float(input("Digite seu salário: "))
    if salario > 1250.00:
        print(f"Seu aumento será de 10%, seu salário total passará a ser {salario + (salario*10)/100}.")
    elif salario <= 1250.00:
        print(f"Seu aumento será de 15%, seu salário total passará a ser {salario + (salario*15)/100}.")
    else: print("Ocorreu um erro. Tente novamente.")
def questao3():
    instalacao = input("Digite a letra que representa o tipo da sua instalação:\nR - Residencial\nC - Comercial\nI - Industrial\n")
    consumo = int(input("Digite a quantidade de kWh consumido: "))
    if instalacao == "R" or "r":
        if consumo <= 500:
            consumo = consumo * 0.40
        elif consumo > 500:
            consumo = consumo * 0.65
    elif instalacao == "C" or "c":
        if consumo <= 1000:
            consumo = consumo * 0.55
        elif consumo > 1000:
            consumo = consumo * 0.60
    elif instalacao == "I" or "i":
        if consumo <= 5000:
            consumo = consumo * 0.55
        elif consumo > 5000:
            consumo = consumo * 0.60
    else: print("Ocorreu um erro. Tente novamente.")
    print(f"Você deverá pagar {consumo} R$.")
def questao4():
    distancia = int(input("Digite a distância que pretende percorrer: "))
    if distancia <= 200:
        distancia = distancia * 0.50
    elif distancia > 200:
        distancia = distancia * 0.45
    else: print("Ocorreu um erro. Tente novamente.") 
    print(f"O valor a ser pago é {distancia} R$.")
def questao5():
    meses = int(input("Digite o mês de 1 à 12: "))
    match meses:
        case 1:
            print("Janeiro")
        case 2:
            print("Fevereiro")
        case 3:
            print("Março")
        case 4:
            print("Abril")
        case 5:
            print("Maio")
        case 6:
            print("Junho")
        case 7:
            print("Julho")
        case 8:
            print("Agosto")
        case 9:
            print("Setembro")
        case 10:
            print("Outubro")
        case 11:
            print("Novembro")
        case 12:
            print("Dezembro")
        case _:
            print("Ocorreu um erro. Tente novamente.")