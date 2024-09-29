from math import sqrt

consBohr = 5.29 * (10 ** -11)
veloEletron = 2.187 * (10**6)
hJaule = 6.62607015 * (10**-34)
hEv = 4.1356677 * (10**-15)
mEletron = 9.10938356 * (10**-31)
c = 3e8

#Ela não quer nenhum valor negativo!

def raioOrbita(n):
    raio = (n**2) * consBohr
    velocidade = veloEletron/n
    eCinetica = 13.6 / (n**2)
    ePotencial = -27.2 / (n**2)
    eTotal = -13.6 / (n**2)
    ondaBroglie = hJaule / (mEletron * velocidade)
    return raio, velocidade, eCinetica, ePotencial, eTotal, ondaBroglie

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
    
    return nReturn, nReturnInt, nReturnInicial