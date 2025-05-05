#Checkpoint02 05/05/2025
#Alunos: Breno Martins e Danilo Medrado

print("Olá, vamos calcular sua Média Anual?")
print("Favor inserir valores de 0 a 10.")
print()
print("Vamos começar pelas notas do primeiro semestre!")

SEM = 1
while SEM <= 2:

    CP1 = float(input("Qual a nota do Primeiro CheckPoint? "))
    CP2 = float(input("Qual a nota do Segundo CheckPoint? "))
    CP3 = float(input("Qual a nota do Terceiro CheckPoint? "))
    SP1 = float(input("Qual a nota da Primeira Sprint? "))
    SP2 = float(input("Qual a nota da Segunda Sprint? "))
    GS = float(input("Qual a nota do Global Solution? "))

    if CP1 <= CP2 and CP1 <= CP3:
        SOMA_CP = CP2 + CP3

    elif CP2 <= CP1 and CP2 <= CP3:
        SOMA_CP = CP1 + CP3

    else:
        SOMA_CP = CP1 + CP2

    MD40 = (SOMA_CP + SP1 + SP2) / 4

    if SEM == 1:
            MEDIASEM1 = (MD40 * 0.4) + (GS * 0.6)
    elif SEM == 2:
            MEDIASEM2 = (MD40 * 0.4) + (GS * 0.6)

    if SEM == 1:
        print()
        print("Vamos agora para as notas do segundo semestre!")
    SEM = SEM+1

MEDIAANU = MEDIASEM1*0.4 + MEDIASEM2*0.6

print()
print(f"Sua Média Anual é: {MEDIAANU:.1f}")