"""
Questão 1
    Azul, Verde, Amarelo, Vermelho
        1 - Mover o Azul do H1 para o H2
        2 - Mover o Verde do H1 para o H3
        3 - Mover o Azul do H2 para o H3
        4 - Mover o Amarelo do H1 para o H2
        5 - Mover o Azul do H3 para o H1
        6 - Mover o Verde do H3 para o H2
        7 - Mover o Azul do H1 para o H2
        8 - Mover o Vermelho do H1 para o H3
        9 - Mover o Azul do H2 para o H3
        10 - Mover o Verde do H2 para o H1
        11 - Mover o Azul do H3 para o H1
        12 - Mover o Amarelo do H2 para o H3
        13 - Mover o Azul do H1 para o H2
        14 - Mover o Verde do H1 para o H3
        15 - Mover o Azul do H2 para o H3

Questão 2

    A) 255
    B) 2^n-1

Questão 3

Questão 4

Questão 5

Questão 6

Questão 7

Questão 8

Questão 9

Questão 10

Questão 11

Questão 12

Questão 13

"""
def questao14():
    print ("Hello World")
    print ("Hello","World")
    print ("Hello!\n My name is John")
    print ("Hello!\t My name is John")
    #print ("Um dia, ela disse: "Estarei aqui por você".")
def questao15():
    hino = """Desce o Sol atrás dos montes
    E a tarde já chegou
    Calma e quieta vem a noite
    Mais um dia terminou
    Já se foi com sua luta
    Logo a negra noite vem
    Mas é doce a lembrança
    Perto está o lar de além"""
    contando = len(hino)
    print("O trecho possui",contando,"letras")
def questao16():
    macas = 5
    laranjas = 10
    frutas = macas + laranjas
    macas = 20
    frutas = macas + laranjas
    print(frutas)
def questao17():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    print("Seu nome é",nome,"e você tem",idade,"anos")
def questao18():
    numero = input("Digite um número: ")
    print("O número escolhido foi",numero,".")
def questao19():
    escolha = input("Digite o número para qual país gostaria de visitar hoje:\n1 - Paris\n2 - França\n3 - Brasil\n")
    escolhi = int(escolha)
    if escolhi == 1:
        print("Vai pra Paris né, seu safado!")
    elif escolhi == 2:
        print("Mimimi vai pra França porque pode né?")
    elif escolhi == 3:
        print("Se for por causa de praia, vou te dar um murro. Bem vindo ao Brasil!")
    else:
        print("Ocorreu um erro, selecione uma opção válida.")
def questao20():
    letras = [2.7, 27, False, "False", "0.0", -21, 99999999, "None", None]
    print(letras)
    escolha = input("escolha e 0 a 9 para descobrir o tipo da variável ")
    escolhi = int(escolha)
    print(type(letras[escolhi]))
def questao21():
    a = True
    cona = str(a)
    b = 3
    conb = float(b)
    c = 3.8
    conc = str(c)
    d = 0.5
    cond = int(d)
    e = "4"
    cone = int(e)
    print(cona, conb, conc, cond, cone)
def questao22():
    calculos = [2.25 - 1, 3.0 * 3, 2 * 4, 2.0 ** 4, 2 / 2.0, 6 / 4, 6 % 4, 4 % 2, round(0.58)]
    print(calculos)
def questao23():
    a = input("Digite o primeiro valor: ")
    cona = int(a)
    b = input ("Digite o segundo valor: ")
    conb = int(b)
    soma = cona + conb
    print("Seu resultado é:",soma)
def questao24():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    resultado = (nota1 * 1 + nota2 * 2 + nota3 *3) / 6
    print(f"Sua media ponderada é {resultado}.")
def questao25():
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    C = int(input("Digite o terceiro valor: "))
    d = int(input("Digite o quarto valor: "))
    resultado = a * b - C * d #Não há necessidade de parênteses pois as multiplicações tem prioridade.
    print(resultado)
def questao26():
    nome = input("Digite o Nome do funcionário: ")
    matricula = input("Digite a matrícula do funcionário :")
    horas = int(input("Digite o número de horas trabalhadas pelo mesmo: "))
    salario = float(input("Digite o salário do mesmo: "))
    print(f"O funcionário {nome}, matrícula {matricula} possui {horas} de serviço com {salario} R$ de salário")