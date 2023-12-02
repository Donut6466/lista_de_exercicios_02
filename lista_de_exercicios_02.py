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
def questao6():
    A = float(input("Digite o valor A: "))
    B = float(input("Digite o valor B: "))
    C = float(input("Digite o valor C: "))
    equilatero = A == B == C
    eita = ((B**2) + (C**2))
    opa = (A**2)
    if A >= (B + C):
        print("Não forma triângulo.")
    else:
        if opa == eita:
            print("Triângulo retângulo.")
        elif opa > eita:
            print("Triângulo obtusângulo.")
        elif opa < eita:
            print("Triângulo acutangulo.")
    if equilatero == False and A == B or A == C or B == C:
            print("Triângulo isosceles.")
    elif equilatero == True:
        print("Triângulo equilatero.")
def questao7():
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))
    C = int(input("Digite o valor de C: "))
    D = int(input("Digite o valor de D: "))
    if (B > C) and (D > A) and (C + D > A + B) and (C > 0) and (D > 0) and ((A % 2)==0):
        print ("Valores aceitos.")
    else:
        print("Valores não aceitos.")
def questao8():
    print("A duração mínima é de 1 minuto e a duração máxima é de 24 horas.")
    hinicial = int(input("Digite a hora inicial: "))
    minicial = int(input("Digite o minuto inicial: "))
    hfinal = int(input("Digite a hora final: "))
    mfinal = int(input("Digite o minuto final: "))
    hduracao = hinicial - hfinal
    if hduracao < 1:
        hduracao = hduracao * (-1)
    mduracao = minicial - mfinal
    if mduracao < 1:
        hduracao = hduracao * (-1)
    totalduracao = hduracao + mduracao
    if totalduracao > 24:
        print("A duração tem que ser menor.")
    elif totalduracao < 1:
        print("A duração tem que ser maior.")
    else: print(f"O jogo durou {hduracao} horas e {mduracao} minutos.")
def questao9():
    import random
    computador = random.randint(0, 2)
    if computador == 0:
        texto = 'pedra'
    elif computador == 1:
        texto = 'papel'
    else:
        texto = 'tesoura'
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()
    if (jogador == 'pedra' and texto == 'tesoura') or \
    (jogador == 'tesoura' and texto == 'papel') or \
    (jogador == 'papel' and texto == 'pedra'):
        print('Jogador venceu!')
    else:
        print('Computador venceu!')
    if jogador == texto:
        print('Empate!')
def questao10():
    import random
    numero_secreto = random.randint(1, 100)
    palpite = 0
    while palpite != numero_secreto:
        palpite = int(input("Digite seu palpite (entre 1 e 100): "))
        if palpite > numero_secreto:
            print("Tente um número menor.")
        elif palpite < numero_secreto:
            print("Tente um número maior.")
    print(f"Parabéns!! Você acertou o número secreto: {numero_secreto}")