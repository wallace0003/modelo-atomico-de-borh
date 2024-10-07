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

def sequenciasSeries():
    print("Série de Lyman: [1,∞)")
    print("Série de  Balmer: [2,∞)")
    print("Série de Paschen: [3,∞)")
    print("Série de Brackett: [4,∞)")
    print("Série de  Pfund: [5,∞)")

def estadosExcitados():
    print("Estado fundamental N = 1")
    print("Primeiro estado excitado N = 2")
    print("Segundo estado excitado N = 3")
    print("Terceiro estado excitado N = 4")
    print("Assim sucessivamente...!")

def nPorVelocidade(velocidade):
    n = round(veloEletron/velocidade , 2)
    nInteiro = round(n, 0)
    return n, nInteiro

def nPorRaio(raio):
    n = sqrt(raio / consBohr)
    nFloat = round(n, 2)
    return nFloat, int(n)

def nPorEnergiaC(energiaC):
    n = sqrt(13.6 / energiaC)
    nFloat = round(n, 2)
    return nFloat, int(n)

def nPorEnergiaP(energiaP):
    n = -27.2/energiaP
    if(n < 0):
        n = n * -1
    
    n = sqrt(n)
    nFloat = round(n, 2)
    return nFloat, int(n)

def nPorEnergiaT(energiaT):
    n = -13.6 / energiaT
    if(n < 0):
        n = n * -1
    
    n = sqrt(n)
    nFloat = round(n, 2)
    return nFloat, int(n)

def dadosEnuciado():
    print("Orbita a uma distância X do núcleo...")
    print("Significa que X é o raio da orbita.")
    print()
    print("Obter a maior frequência de onda de uma série:")
    print("o N inicial = N inicial da série")
    print("N final = N tendendo a infinito, pode ser N(final) = 1.000.000")
    print("Obter a menor frequência de onda de uma série:")
    print("o N inicial = N inicial da série")
    print("N final = N incial + 1")
    print()
    print("Obter o maior comprimento de onda de uma série:")
    print("o N inicial = N inicial da série")
    print("N final =  N incial + 1")
    print("Obter o menor comprimento de onda de uma série:")
    print("o N inicial = N inicial da série")
    print("N final = N tendendo a infinito, pode ser N(final) = 1.000.000")
    print()

def classificacaoEletromag():
    print("Raios gama -> (λfóton) < 0.01 [nm]")
    print("Raios X ->  0.01 [nm] <= (λfóton) < 10 [nm]")
    print("Ultravioleta (UV) -> 10 [nm] <= (λfóton) < 400 [nm]")
    print("Visível (Vermelho – Violeta) -> 400 [nm] <= (λfóton) < 700 [nm]")
    print("Infravermelho (IR) -> 700 [nm] <= (λfóton) < 1.000.000 [nm]")
    print("Micro-ondas -> 1.000.000 [nm] <= (λfóton) < 1.000.000.000 [nm]")
    print("Ondas de Rádio -> (λfóton) >= 1.000.000.000 [nm]")

def tabelaConversoes():
    print("de rad/s -> rad/m = W(frequência angular)/Vluz = W/3x10^8")
    print()
    print("nm -> m  = nm * E-9")
    print("m -> nm = m * E+9")
    print("um -> m = um * E-6")
    print("m -> um = m * E+6")
    print("mc -> m  = mc * E-6")
    print("m -> mc = m * E+6") 
    print()
    print("Hz -> KHz = Hz *e-3")
    print("Khz -> Hz = Khz*e+3")
    print("Hz -> mHz = Hz * E-6")
    print("mHz -> Hz = mHz * E+6")
    print("Hz -> THz = Hz * E-12")
    print("THz -> Hz = THz * E+12")
    print("Hz -> GHz = Hz * E-9")
    print("GHz - > Hz = Hz * E+9")
    print()
    print("V/m -> MV/m = V/m * E-6")
    print("MV/m -> V/m = MV/m * E+6")
    print()
    print("mT -> T = mT * E-3")
    print("T -> mT = T * E+3")
    print("uT -> T = uT * E-6")
    print("T -> uT = T * E+6")

def transicoesHidrogenio():
    print("n=1 - n=2 -> Ef = 10.2 [eV]")
    print("n=1 - n=3 -> Ef = 12.09 [eV]")
    print("n=1 - n=4 -> Ef = 12.75 [eV]")
    print("n=1 - n=5 -> Ef = 13.06 [eV]")
    print("Se a energia do foton estiver entre esses intervalos:")
    print("Sim, o elétron fará um salto quântico.")
    print()
    print("Se a energia do foton > 13.6: ")
    print("Sim, mas o átomo seria ionizado.")
    print()
    print("Se a energia do foton for menor que os intervalos acima: ")
    print("Não é possível")
    