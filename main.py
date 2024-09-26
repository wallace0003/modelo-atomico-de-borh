from funcoes import *

while True:
    print("Opções de entrada abaixo: ")
    print("-" * 30)
    print()

    print("1 - Entrada de N")
    print("0 - Sair.")

    opcao = str(input("Opção: "))

    if(opcao == "1"):
         n = float(input("Digite o valor de N: "))
         raio, velocidade, eCinetica, ePotencial, eToral, ondaBroglie = raioOrbita(n)

         raioNotacao = "{:.4e}".format(raio)
         velocidadeNotacao = "{:.4e}".format(velocidade)
         eCineticaNotacao = "{:.4e}".format(eCinetica)
         ePotencialNotacao = "{:.4e}".format(ePotencial)
         eTotalNotacao = "{:.4e}".format(eToral)
         ondaBroglieNotacao = "{:.4e}".format(ondaBroglie)

         print()
         print(f"Rn (Raio da órbita) = {raioNotacao} [m]")
         print(f"Vn (Velocidade) = {velocidadeNotacao} [m/s]")
         print(f"Kn (energia cinética) = {eCineticaNotacao} [eV]")
         print(f"Un (energia potencia) = {ePotencialNotacao} [eV]")
         print(f"En (energia total) = {eTotalNotacao} [eV]")
         print(f"λn (comprimento de onda de De Broglie do elétron) = {ondaBroglieNotacao} [m]")
         print()



    if(opcao == "0"):
        print("Saindo...")
        break