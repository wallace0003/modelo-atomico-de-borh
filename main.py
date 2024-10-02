from funcoes import *

print("""Autores:

Jônatas da Silva Gonçalves.
Wallace dos Santos Izidoro.
Pedro Henrique da Fonseca do Nascimento.
Vinícius do Nascimento Generoso.\n""")

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
        uniEfoton = str(input("1 -> Efóton[eV] | 2 -> Efóton[J]"))
        while(uniEfoton != "1" and  uniEfoton != "2"):
            print("Digitação inválida, digite apenas 1 ou 2")
            uniEfoton= str(input("1 -> Efóton[eV] | 2 -> Efóton[J]"))

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