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
    
    nReturn = round(nReturn, 2)
    
    
    nReturnInicial = not(nInicial)
    nReturnInt = round(sqrt(13.6/abs(nReturn)))
    
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
        
    nReturn = round(nReturn, 2)

    nReturnInicial = not nInicial
    nReturnInt = round(sqrt(13.6 / abs(nReturn)))

    return nReturn, nReturnInt, nReturnInicial

    