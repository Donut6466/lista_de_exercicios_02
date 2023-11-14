"""
Questão 1
    Azul, Verde, Amarelo, Vermelho
        1 - Mover o Azul do H1 para o H2;
        2 - Mover o Verde do H1 para o H3;
        3 - Mover o Azul do H2 para o H3;
        4 - Mover o Amarelo do H1 para o H2;
        5 - Mover o Azul do H3 para o H1;
        6 - Mover o Verde do H3 para o H2;
        7 - Mover o Azul do H1 para o H2;
        8 - Mover o Vermelho do H1 para o H3;
        9 - Mover o Azul do H2 para o H3;
        10 - Mover o Verde do H2 para o H1;
        11 - Mover o Azul do H3 para o H1;
        12 - Mover o Amarelo do H2 para o H3;
        13 - Mover o Azul do H1 para o H2;
        14 - Mover o Verde do H1 para o H3;
        15 - Mover o Azul do H2 para o H3.

Questão 2

    A) 255 .
    B) 2^n-1 .

Questão 3
    São necessários 5 copos para equilibrar a garrafa.

Questão 4
    A mulher de Basílio.
Questão 5
    Você precisaria tirar apenas um elemento de cada pote. 
    Escolha um fruto do pote rotulado como "Ambas". 
    Se for uma maçã, troque os rótulos dos potes "Maçãs" e "Laranjas". 
    Se for uma laranja, os rótulos já estão corretos. 
    Em apenas um movimento, os potes estarão rotulados corretamente.
Questão 6
    Ted é um cavaleiro.
    Ben é um patife.
    Lil é um patife.
Questão 7
    A)  São uma sequência de passos.
        Suas partes são entrada, processamento e saída.
    B)  Linguagem natural, fluxograma e pseudocódigo.
    c)  1 - Solicitar ao usuário a temperatura em Celsius.
        2 - Aplicar a fórmula 
        3 - Verificar se a temperatura em Fahrenheit está acima de 100.
        4 - Exibir "Você está com febre" ou "Relaxa, tá tudo bem" conforme necessário.
Questão 8
    A)  Linguagem explicada usada com um idioma.
    B)  Números binários, 0 ou 1 .
    C)  Linguagem em que permite o usuário conversar com uma máquina.
    D)  O compilador traduz o código-fonte por linha enquanto o interpretador traduz o código-fonte por inteiro.
Questão 9
    Linguagem de Baixo Nível:
        Linguagens mais próximas da linguagem de máquina. -- Assembly
    Linguagem de Alto Nível:
        Linguagens mais distantes da linguagem de máquina. -- Python
Questão 10
    x = 2
    x = 6
    resultado = x * y
    A diferença existe pelo mesmo motivo que existe o português e o inglês.
Questão 11
    Atribuição, Entrada/Saída, Condicionais, Loops, Operações Aritméticas e funções.
    Em Python não há declaração de variável.
Questão 12
    Váriaveis são caixas que guardam informações.
    customer-list é permitido no Python enquanto os restantes não por conterem caracteres especiais.
Questão 13
    São valores que não se alteram.
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
def questao27():
    soma = (2+2+2)
    produto = (soma*-6)
    produto /= 10
    print(produto)
def questao28():
    nome = input("Digite o nome do vendedor: ")
    salario = float(input("Digite o salário fixo do vendedor: "))
    vendas = float(input("Digite o faturamento total de vendas efetuadas: "))
    processo = (vendas * 15/100)
    resultado = (salario + processo)
    print(f"TOTAL = {resultado}R$")
def questao29():
    raio = float(input("Digite o raio de sua esfera: "))
    pi = 3.14159
    esfera = (4/3) * pi * raio ** 3
    print(esfera)
def questao30():
    base = int(input("Digite a base: "))
    lado = int(input("Digite o lado ou a base menor: "))
    altura = int(input("Digite o raio ou a altura: "))
    triangulo = (base * altura) / 2
    circulo = 3.14159 * (altura ** 2)
    trapezio = ((base + lado) * altura) /2
    quadrado = lado * lado
    retangulo = base * lado
    print(f"Confira as respectivas áreas abaixo\nTriângulo: {triangulo}\nCirculo: {circulo}\nTrapézio: {trapezio}\nQuadrado: {quadrado}\nRetângulo: {retangulo}")
def questao31():
    x = 10 % 3 * 10 ** 2 + 1 -10 * 4/2
    print(f"A solução da equação é: {x}")
def questao32():
    km = float(input("Digite a distância percorrida em km: "))
    l = float(input("Digite o total de combustível em litros: "))
    resultado = (km / l)
    print(f"O consumo médio foi {resultado}km/l")
def questao33():
    tempo = int(input("Digite em horas o tempo gasto na viagem: "))
    velocidade = float(input("Digite a velocidade média durante a viagem: "))
    distancia = (velocidade * tempo)
    resultado = (distancia / 12)
    print(resultado)
def questao34():
    dias = int(input("Digite a quantidade de dias: "))
    horas = int(input("Digite a quantidade de horas: "))
    minutos = int(input("Digite a quantidade de minutos: "))
    segundos = int(input("Digite a quantidade de segundos: "))
    resultado = (dias * 86400 + horas + 60 + minutos * 60)
    print(f"O total de segundos são: {segundos + resultado}")
def questao35():
    import math
    lado = float(input("Digite o lado do quadrado: "))
    perimetro = (lado * 4)
    area = (lado * 2)
    diagonal = (math.sqrt(2)) * lado
    print(f"O perimetro do quadrado é: {perimetro}")
    print(f"A área do quadrado é: {area}")
    print(f"A diagonal do quadrado é: {diagonal}")
def questao36():
    valor = int(input("Digite o valor: "))
    notas100 = notas50 = notas20 = notas10 = nota5 = nota2= nota1= 0
    while valor != 0:
        if valor >=100:
            notas100 += 1
            valor -=100
        elif valor >=50:
            notas50 += 1
            valor -=50
        elif valor >=20:
            notas20 += 1
            valor -=20
        elif valor >=10:
            notas10 += 1
            valor -=10
        elif valor >=5:
            nota5 += 1
            valor -=5
        elif valor >=2:
            nota2 += 1
            valor -=2
        elif valor >=1:
            nota1 += 1
            valor -=1
        else:
            nota1 += 1
            valor -= 1
    print("O valor foi:", valor)
    print("Notas de 100:", notas100)
    print("Notas de 50:", notas50)
    print("Notas de 20:", notas20)
    print("Notas de 10:", notas10)
    print("Notas de 5", nota5)
    print("Notas de 2:", nota2)
    print("Notas de 1:", nota1)
def questao37():
    dsegundos = int(input("Digite o tempo de duração em segundos do evento na fábrica: "))
    horas = dsegundos // 3600
    minutos = (dsegundos % 3600) // 60
    segundos = dsegundos % 60
    print(horas, ":", minutos, ":", segundos )
def questao38():
    idade = int(input("Diga sua idade em dias:"))
    anos = idade // 365
    meses = (idade % 365) // 30
    dias = (idade % 365) % 30
    resultado1 = (anos)
    resultado2 = (meses)
    resultado3 = (dias)
    print(resultado1, "anos", resultado2, "meses", resultado3, "dias")
def questao39():
    valor = float(input("Digite o valor"))
    valorcent = int(valor * 100)
    notas100 = notas50 = notas20 = notas10 = notas5 = notas2 = 0
    moedas1 = moedas050 = moedas025 = moedas010 = moedas005 = moedas001 = 0
    while valorcent != 0:
        if valorcent >=10000:
            notas100 += 1
            valorcent -=1000
        elif valorcent >=5000:
            notas50 += 1
            valorcent -=5000
        elif valorcent >=2000:
            notas20 += 1
            valorcent -=2000
        elif valorcent >=1000:
            notas10 += 1
            valorcent -=1000
        elif valorcent >=500:
            notas5 += 1
            valorcent -=500
        elif valorcent >=200:
            notas2 += 1
            valorcent-=200
        elif valorcent >=100:
            moedas1 += 1
            valorcent -=100
        elif valorcent >= 50:
            moedas050 += 1
            valorcent -=50
        elif valorcent >=25:
            moedas025 += 1
            valorcent -= 25
        elif valorcent >= 10:
            moedas010 += 1
            valorcent -= 10
        elif valorcent >= 5:
            moedas005 += 1
            valorcent -= 5
        else:
            moedas001 +=1
            valorcent -= 1
            
    print(f"Notas de 100: {notas100}")
    print(f"Notas de 50: {notas50}")
    print(f"Notas de 20: {notas20}")
    print(f"Notas de 10: {notas10}")
    print(f"Notas de 5 {notas5}")
    print(f"Notas de 2: {notas2}")
    print(f"Notas de 1: {moedas1}")
    print(f"Notas de 0,50 {moedas050}")
    print(f"Notas de 0,25 {moedas025}")
    print(f"Notas de 0,10 {moedas010}")
    print(f"Notas de 0,05 {moedas005}")
    print(f"Moedas de 0,01 {moedas001}")
def questao40():
    a = 3 < 2 ** 3 and 3 == 3  #**  <   ==
    b = 0 != 4 or(3/3 == 1 and (5 +1)/3 ==2) #!=    /   ==
    print(a, b)
def questao41():
    salario = float(input("Digite seu salário: "))
    imposto = (salario>1200.00 and True)
    print("Paga imposto?", imposto)
def questao42():
    a = [1, 10, 5]
    b = [2, 3, 1]
    c = [True, False, True]
    d = [False, True, True]
    resultado = (a > b and c or not d)
    print(resultado)
def questao43():
    materia1 = float(input("Digite a nota da primeira matéria: "))
    materia2 = float(input("Digite a nota da segunda matéria: "))
    materia3 = float(input("Digite a nota da terceria matéria: "))
    faltas = int(input("Digite a quantidade de faltas totais: "))
    media = (materia1 + materia2 +materia3) / 3
    aulasm = 10
    aulast = 3 * aulasm
    frequencia = ((aulasm - faltas) / aulast) * 100
    resultado = media >= 7 and frequencia >= 75
    print("Aluno aprovado?", resultado)