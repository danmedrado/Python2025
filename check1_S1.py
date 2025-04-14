#CheckPoint 01 - 14/04/2025
#Alunos: Breno Martins & Danilo Medrado

print("Olá, vamos calcular sua Média Semestral?")
print("Favor inserir valores de 0 a 10.")

CP1 = float(input("Qual a nota do Primeiro CheckPoint? "))
CP2 = float(input("Qual a nota do Segundo CheckPoint? "))
CP3 = float(input("Qual a nota do Terceiro CheckPoint? "))
SP1 = float(input("Qual a nota da Primeira Sprint? "))
SP2 = float(input("Qual a nota da Segunda Sprint? "))
GS = float(input("Qual a nota do Global Solution? "))


maior = CP1
if CP2 >= CP1 and CP2 >= CP3:
    maior = CP2
if CP3 >= CP1 and CP3 >= CP2:
    maior = CP3

menor = CP1
if CP2 <= CP1 and CP2 <= CP3:
    menor = CP2
if CP3 <= CP1 and CP3 <= CP2:
    menor = CP3

meio = CP1
if CP1 >= CP2 >= CP3:
    meio = CP2
if CP1 >= CP3 >= CP2:
    meio = CP3

Media40 = ((maior + meio) + SP1 + SP2)/4
MediaFinal = Media40*0.4 + GS*0.6

print(f"Sua média semestral é: {MediaFinal:.1f}")