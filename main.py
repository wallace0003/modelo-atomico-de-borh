from funcoes import *

from math import sqrt

consBohr = 5.29 * (10 ** -11)
veloEletron = 2.187 * (10**6)
hJaule = 6.62607015 * (10**-34)
hEv = 4.1356677 * (10**-15)
mEletron = 9.10938356 * (10**-31)
c = 3e8
const_energia = 13.6 #(eV)
converte_eV_para_Joules = 1.60218e-19

#Ela não quer nenhum valor negativo!

def raioOrbita(n):
    raio = (n**2) * consBohr
    velocidade = veloEletron/n
    eCinetica = 13.6 / (n**2)
    ePotencial = -27.2 / (n**2)
    eTotal = -13.6 / (n**2)
    ondaBroglie = hJaule / (mEletron * velocidade)
    return raio, velocidade, eCinetica, ePotencial, eTotal, ondaBroglie


def calcular_foton(nI, nF):
    # Energia do fóton em eV
    energiaFotonEm_eV = const_energia * ((1 / nI**2) - (1 / nF**2))
    
    # Convertendo energia do fóton de eV para Joules
    energiaFotonJ = energiaFotonEm_eV * converte_eV_para_Joules
    
    # Frequência do fóton (ffóton)
    frequenciaFoton = energiaFotonJ / hJaule
    
    # Comprimento de onda do fóton (λfóton)
    comprimentoOndaFoton = (hJaule * c) / energiaFotonJ
    
    return energiaFotonEm_eV, energiaFotonJ, frequenciaFoton, comprimentoOndaFoton

def nPorFotonAbsorvido(n, foton, nInicial = True, fotonFrequencia = True):
    # n = n inicial ou n fínal do eletron
    # foton = frequencia ou comprimento (lambda) do fóton
    # nInicial(true): n = incial
    # fotonFrequencia(true): foton = Frequencia do fóton  
    
    nEnergia = -13.6/(n**2)
    nReturn = None
    energiaFoton = None
    
    # Cálculo da energia do fóton
    if(fotonFrequencia):
        energiaFoton = foton * hEv
        
    else:
        # foton como lambda
        energiaFoton = (hEv * c)/foton
        
    # Cálculo de n com base na energia do fóton
    if(nInicial):
        nReturn = nEnergia + energiaFoton
    else:
        nReturn = nEnergia - energiaFoton
    
    nReturnInicial = not(nInicial)
    nReturnInt = round(sqrt(13.6/abs(nReturn)))
    nReturn = round(sqrt(13.6/abs(nReturn)), 2)
    
    return nReturn, nReturnInt, nReturnInicial

def energiaPorComprimento(lambdaFoton):
    try:
        eEv = hEv*c/lambdaFoton
        eJ = hJaule*c/lambdaFoton
        return eEv,eJ

    except ZeroDivisionError:
        print("Impossível fazer está operação!")

def energiaPorFrequencia(frequencia):
    eEv = (hEv * frequencia)
    eJ = (hJaule * frequencia)
    return eEv, eJ

def energiaEv(efoton):
    comprimento = (hEv*c) / efoton
    frequencia = (efoton / hEv)
    return comprimento, frequencia

def energiaJ(efoton):
    comprimento = (hJaule*c) / efoton
    frequencia = (efoton / hJaule)
    return comprimento, frequencia

def nPorFotonEmitido(n, foton, nInicial=True, fotonFrequencia=True):
    nEnergia = -13.6/(n**2)
    energiaFoton = None

    # Cálculo da energia do fóton
    if fotonFrequencia:
        energiaFoton = foton * hEv
    else:
        # foton como lambda
        energiaFoton = (hEv * c) / foton

    # Cálculo de n com base na energia do fóton emitido
    if nInicial:
        nReturn = nEnergia - energiaFoton
    else:
        nReturn = nEnergia + energiaFoton
        
    nReturnInicial = not(nInicial)
    nReturnInt = round(sqrt(13.6/abs(nReturn)))
    nReturn = round(sqrt(13.6/abs(nReturn)), 2)

    return nReturn, nReturnInt, nReturnInicial

    

print("""Autores:

Jônatas da Silva Gonçalves.
Wallace dos Santos Izidoro.
Pedro Henrique da Fonseca do Nascimento.
Vinícius do Nascimento Generoso.\n""")

print("""
Estudo do Modelo de Bohr e Cálculos Relacionados com Programação em Python

Este código em Python foi desenvolvido para realizar diversos cálculos relacionados ao modelo de Bohr, que descreve o comportamento
dos elétrons em átomos. Os cálculos são acessíveis por meio de um menu interativo, onde o usuário pode fornecer parâmetros específicos
e obter resultados pertinentes.

Funcionalidades: Entrada com N (Número Quântico): Calcula o raio da órbita do elétron, sua velocidade, energia cinética, energia potencial, 
energia total e comprimento de onda de De Broglie.

Entrada de N-inicial e N-final: Determina a energia, frequência e comprimento de onda de um fóton quando um elétron transita entre dois 
níveis quânticos.

Cálculo do Número Quântico em razão de um Fóton Absorvido: Identifica o número quântico final (ou inicial) com base na energia de um 
fóton absorvido, considerando a entrada como frequência ou comprimento de onda.

Cálculo do Número Quântico em razão de um Fóton Emitido: Semelhante ao cálculo anterior, mas para a energia de um fóton emitido.

Entrada de Energia de um Fóton: Permite calcular o comprimento de onda, frequência e energia em diferentes unidades (eV ou Joules) a 
partir de uma entrada de energia do fóton.

Limitações: Os cálculos são realizados corretamente apenas quando o usuário utiliza as unidades de medida solicitadas pelo algoritmo.

Breve Explicação: O modelo de Bohr é fundamental para entender como os elétrons se comportam em átomos, com níveis de energia quantizados. 
As transições entre esses níveis resultam na emissão ou absorção de fótons, cujas energias estão relacionadas ao número quântico. A programação
em Python automatiza esses cálculos, fornecendo uma interface que facilita a obtenção de propriedades atômicas a partir de valores iniciais como
números quânticos ou energia de fótons. Esse modelo é essencial para a compreensão de fenômenos como a espectroscopia e a estrutura atômica.
""")

print()

print("Calculadora do Modelo de Borh  em Python\n")

print("Caso deseje entrar com valores em notação científica, utilize o formato abaixo:")
print("1.23 x 10^4 --> 1.23e4\n")

while True:
    print("Menu: ")
        
    print("-" * 30)

    print("1 - Dados do elétron a partir de N")
    print("2 - Dados do fóton emitido/absorvido a partir de N-inicial e N-final")
    print("3 - N inicial ou final em razão de um fóton absorvido")
    print("4 - N inicial ou final em razão de um fóton emitido")
    print("5 - Energia do fóton a partir da frequência (f) ou comprimento de onda (λ)")
    print("6 - Dados de frequência (f) e comprimento de onda (λ) do fóton a partir da energia")
    print("0 - Sair.")
    print()

    opcao = str(input("Digite o número da opção desejada: "))
    print()
    
    if(opcao == "1"):
        n = float(input("Digite o valor de N: "))
        raio, velocidade, eCinetica, ePotencial, eTotal, ondaBroglie = raioOrbita(n)
        raioNotacao = "{:.4e}".format(raio)
        velocidadeNotacao = "{:.4e}".format(velocidade)
        eCineticaNotacao = "{:.4e}".format(eCinetica)
        ePotencialNotacao = "{:.4e}".format(ePotencial)
        eTotalNotacao = "{:.4e}".format(eTotal)
        ondaBroglieNotacao = "{:.4e}".format(ondaBroglie)
        
        print()
        print(f"Rn (Raio da órbita) = {raioNotacao} [m]")
        print(f"Vn (Velocidade) = {velocidadeNotacao} [m/s]")
        print(f"Kn (energia cinética) = {eCineticaNotacao} [eV]")
        print(f"Un (energia potencia) = {ePotencialNotacao} [eV]")
        print(f"En (energia total) = {eTotalNotacao} [eV]")
        print(f"λn (comprimento de onda de De Broglie do elétron) = {ondaBroglieNotacao} [m]")
        print()

    elif(opcao == "2"):
        nI = float(input("Digite o valor de N-inicial: "))
        nF = float(input("Digite o valor de N-final: "))

        energiaFotonEm_eV, energiaFotonJ, frequenciaFoton, comprimentoOndaFoton = calcular_foton(nI, nF)

        if energiaFotonEm_eV < 0 or energiaFotonJ < 0 or frequenciaFoton < 0 or comprimentoOndaFoton < 0:
            energiaFotonEm_eV = abs(energiaFotonEm_eV)
            energiaFotonJ = abs(energiaFotonJ)
            frequenciaFoton = abs(frequenciaFoton)
            comprimentoOndaFoton = abs(comprimentoOndaFoton)

        energiaFotonEm_eV_Notacao = "{:.4e}".format(energiaFotonEm_eV) 
        energiaFotonJ_Notacao = "{:.4e}".format(energiaFotonJ)
        frequenciaFoton_Notacao = "{:.4e}".format(frequenciaFoton)
        comprimentoOndaFoton_Notacao = "{:.4e}".format(comprimentoOndaFoton)

        

        print()
        print(f"Efóton (em eV): {energiaFotonEm_eV_Notacao} [eV]")
        print(f"Efóton (em Joules): {energiaFotonJ_Notacao} [J]") #No questionario nao tem mais eu coloquei só pra garantir
        print(f"Frequência do fóton (ffóton): {frequenciaFoton_Notacao} [Hz]")
        print(f"Comprimento de onda do fóton (λfóton): {comprimentoOndaFoton_Notacao} [m]")
        print()

    elif(opcao == "3"):
        
        nOpcao = input("1 -> N incial / 2 -> N Final: ")
        if(nOpcao == "1"):
            nOpcao = True
            n = float(input("Digite o valor de N (Inicial): "))
        elif(nOpcao == "2"):
            nOpcao = False
            n = float(input("Digite o valor de N (Final): "))
        else:
            print("Entrada inválida.")
            print()
            continue
            
        while(True):
            fotonOpcao = input("Dados do fóton em Frequência(Hz) -> 1 / Dados do fóton em Comprimento de Onda(m) -> 2: ")
            if(fotonOpcao == "1"):
                fotonOpcao = True
                foton = float(input("Digite a frequência do fóton [Hz]: "))
                break
            elif(fotonOpcao == "2"):
                fotonOpcao = False
                foton = float(input("Digite o comprimento de onda do fóton [m]: "))
                break
            else:
                print("Entrada inválida, digite novamente.")
                
        try:
            nReturn, nReturnInt, nReturnInicial = nPorFotonAbsorvido(n, foton, nOpcao, fotonOpcao)
        
            if (nReturnInicial):
                inicialOuFinal = "Inicial"
            else:
                inicialOuFinal = "Final"
            
            print()
            print(f"Número quântico {inicialOuFinal} (N): {nReturn}")
            print(f"Número Quântico {inicialOuFinal} (N Inteiro): {nReturnInt}")
            print()
            
        except:
            print("Valor inválido")
            print()
    
    elif(opcao == "4"):
        nOpcao = input("1 -> N incial / 2 -> N Final: ")
        if(nOpcao == "1"):
            nOpcao = True
            n = float(input("Digite o valor de N (Inicial): "))
        elif(nOpcao == "2"):
            nOpcao = False
            n = float(input("Digite o valor de N (Final): "))
        else:
            print("Entrada inválida.")
            print()
            continue

        while(True):
            fotonOpcao = input("Dados do fóton em Frequência(Hz) -> 1 / Dados do fóton em Comprimento de Onda(m) -> 2: ")
            if(fotonOpcao == "1"):
                fotonOpcao = True
                foton = float(input("Digite a frequência do fóton [Hz]: "))
                break
            elif(fotonOpcao == "2"):
                fotonOpcao = False
                foton = float(input("Digite o comprimento de onda do fóton [m]: "))
                break
            else:
                print("Entrada inválida, digite novamente.")
        
        try:
            nReturn, nReturnInt, nReturnInicial = nPorFotonEmitido(n, foton, nOpcao, fotonOpcao)
            
            if nReturnInicial:
                inicialOuFinal = "Inicial"
            else:
                inicialOuFinal = "Final"

            print()
            print(f"Número quântico {inicialOuFinal} (N): {nReturn}")
            print(f"Número Quântico {inicialOuFinal} (N Inteiro): {nReturnInt}")
            print()
        except:
            print("Valor inválido")
            print()


    elif(opcao == "5"):
        ffOuLamf = str(input("1 -> Ffóton(Frequência do fóton) | 2 -> λFóton(comprimento de onda do fóton): "))
        while(ffOuLamf != "1" and ffOuLamf != "2"):
            print("Digitação inválida, digite apenas 1 ou 2")
            ffOuLamf = str(input("1 -> Ffóton(frequência do fóton) | 2 -> λFóton(comprimento de onda do fóton)"))

        if(ffOuLamf == "1"):
            frequenciaFoton = float(input("Digite o Ffóton(frequência do fóton) [Hz]: "))
            eEv, eJ = energiaPorFrequencia(frequenciaFoton)
            eEvNotacao = "{:.4e}".format(eEv) 
            eJNotacao = "{:.4e}".format(eJ)
            print()
            print(f"Efóton(Energia do fóton): {eEvNotacao} [eV]")
            print(f"Efóton(Energia do fóton): {eJNotacao} [J]")
            print()

        elif(ffOuLamf == "2"):
            lambdaFoton = float(input("Digite o λFóton(comprimento de onda do fóton)[m]: "))
            eEv, eJ = energiaPorComprimento(lambdaFoton)
            eEvNotacao = "{:.4e}".format(eEv) 
            eJNotacao = "{:.4e}".format(eJ) 
            print()
            print(f"Efóton(Energia do fóton): {eEvNotacao} [eV]")
            print(f"Efóton(Energia do fóton): {eJNotacao} [J]")
            print()

    elif(opcao == "6"):
        print("Digite a opção que deseja.")
        uniEfoton = str(input("1 -> Efóton[eV] | 2 -> Efóton[J]: "))
        while(uniEfoton != "1" and  uniEfoton != "2"):
            print("Digitação inválida, digite apenas 1 ou 2")
            uniEfoton= str(input("1 -> Efóton[eV] | 2 -> Efóton[J]: "))

        if(uniEfoton == "1"):
            efoton = float(input("Digite Efóton(Energia do fóton) [eV]: "))
            comprimento, frequencia = energiaEv(efoton)
            comprimentoNotacao = "{:.4e}".format(comprimento) 
            frequenciaNotacao = "{:.4e}".format(frequencia) 
            print()
            print(f"λFóton (comprimento de onda do fóton): {comprimentoNotacao} [m]")
            print(f"Ffóton (frequência do fóton): {frequenciaNotacao} [Hz]")
            print()

        elif(uniEfoton == "2"):
            efoton = float(input("Digite Efóton(Energia do fóton) [J]: "))
            comprimento, frequencia =energiaJ(efoton)
            comprimentoNotacao = "{:.4e}".format(comprimento) 
            frequenciaNotacao = "{:.4e}".format(frequencia) 
            print()
            print(f"λFóton (comprimento de onda do fóton): {comprimentoNotacao} [m]")
            print(f"Ffóton (frequência do fóton): {frequenciaNotacao} [Hz]")
            print()


        
    elif(opcao == "0"):
        print("Saindo...")
        break
    
    else:
        print("Opção inválida.")