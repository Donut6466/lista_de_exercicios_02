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