from funcoes import *

while True:
    print("Opções de entrada abaixo: ")
    print("-" * 30)
    print()

    print("1 - Entrada de N")
    print("2 - Entrado do N-inicial e N-final")
    print("3 - N inicial ou final em razão de um fóton absorvido")
    print("0 - Sair.")
    print()

    opcao = str(input("Opção: "))
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
        print(f"Efóton (em eV): {energiaFotonEm_eV_Notacao} eV")
        print(f"Efóton (em Joules): {energiaFotonJ_Notacao} J") #No questionario nao tem mais eu coloquei só pra garantir
        print(f"Frequência do fóton (ffóton): {frequenciaFoton_Notacao} Hz")
        print(f"Comprimento de onda do fóton (λfóton): {comprimentoOndaFoton_Notacao} m")
        print()

    elif(opcao == "3"):
        n = float(input("Digite o valor de N (Inicial ou final): "))
        nOpcao = input("1. N incial / 2. N Final: ")
        if(nOpcao == "1"):
            nOpcao = True
        elif(nOpcao == "2"):
            nOpcao = False
        else:
            print("Entrada inválida.")
            print()
            
        while(True):
            fotonOpcao = input("Os dados do fóton serão em Frequência(f)(1), ou  em Comprimento de Onda(λ)(2)?: ")
            if(fotonOpcao == "1"):
                fotonOpcao = True
                foton = float(input("Digite a frequência do fóton (Hz): "))
                break
            elif(fotonOpcao == "2"):
                fotonOpcao = False
                foton = float(input("Digite o comprimento do fóton (m): "))
                break
            else:
                print("Entrada inválida, digite novamente.")
                
        
        nReturn, nReturnInt, nReturnInicial = nPorFotonAbsorvido(n, foton, nOpcao, fotonOpcao)
        
        if (nReturnInicial):
            inicialOuFinal = "Inicial"
        else:
            inicialOuFinal = "Final"
        
        print()
        print(f"Energia do Número quântico {inicialOuFinal} (N): {round(nReturn, 2)} [eV]")
        print(f"Número Quântico {inicialOuFinal}: {nReturnInt}")
        print()
        
    elif(opcao == "0"):
        print("Saindo...")
        break
    
    else:
        print("Opção inválida.")