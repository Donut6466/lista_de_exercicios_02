"""😀 Faça um programa que imprima:
Os números de 1 a 100.
Os números pares de 50 a 100.
Os números em contagem regressiva 10, 9, 8, 7,..., 1, 0 e Fogo!
Os números pares ou ímpares de 1 até um valor digitado pelo usuário,
que também deve informar se quer só os pares ou só os ímpares.
"""

def questao1():
    #letraA----------------
    print("----------------------------------------------------------------\nLetra A\n----------------------------------------------------------------")
    Anumber = 0
    while Anumber < 101:
        print(Anumber)
        Anumber = Anumber + 1
    #letraB----------------
    print("----------------------------------------------------------------\nLetra B\n----------------------------------------------------------------")
    Bnumber = 50
    while Bnumber < 101:
        print (Bnumber)
        Bnumber = Bnumber + 2
    #letraC----------------
    print("----------------------------------------------------------------\nLetra C\n----------------------------------------------------------------")
    Cnumber = 10
    while Cnumber > -1:
        print (Cnumber)
        Cnumber = Cnumber - 1
    print("e fogo!")
    #letraD----------------
    print("----------------------------------------------------------------\nLetra D\n----------------------------------------------------------------")
    Dnumber = 0
    DDnumber = int(input("Digite um número limite: "))
    while Dnumber < (DDnumber + 1):
        print (Dnumber)
        Dnumber = Dnumber + 2