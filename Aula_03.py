#exercicio1
'''
velocidade = float(input("Qual a velocidade do veículo ao passar pelo radar?"))

if velocidade > 80:
    print("Vixe... Você foi multado(a)!")
    multa = (velocidade-80) * 5
    print(f"O valor da sua multa é R$ {multa:.2f}")
    print("Mais cuidado da próxima vez!")
else:
    print("Glória! Você não foi multado!")
'''

#exercicio2

'''
nota1 = float(input("Quanto você tirou no primeiro Checkpoint?"))
nota2 = float(input("Qual foi sua nota do segundo Checkpoint?"))
nota3 = float(input("E o terceiro Checkpoint, tirou quanto?"))

if nota1 > nota2 and nota1 > nota3:
    print(f"Sua maior nota foi {nota1}")
if nota2 > nota1 and nota2 > nota3:
    print(f"Sua maior nota foi {nota2}")
if nota3 > nota1 and nota3 > nota2:
    print(f"Sua maior nota foi {nota3}")

if nota1 < nota2 and nota1 < nota3:
    print(f"Sua menor nota foi {nota1}")
if nota2 < nota1 and nota2 < nota3:
    print(f"Sua menor nota foi {nota2}")
if nota3 < nota1 and nota3 < nota2:
    print(f"Sua menor nota foi {nota3}")
'''

#exercicio2 simplificado

nota1 = float(input("Quanto você tirou no primeiro Checkpoint?"))
nota2 = float(input("Qual foi sua nota do segundo Checkpoint?"))
nota3 = float(input("E o terceiro Checkpoint, tirou quanto?"))

maior = nota1
if nota2 >= nota1 and nota2 >= nota3:
    maior = nota2
if nota3 >= nota1 and nota3 >= nota2:
    maior = nota3

menor = nota1
if nota2 <= nota1 and nota2 <= nota3:
    menor = nota2
if nota3 <= nota1 and nota3 <= nota2:
    menor = nota3

meio = nota1
if nota1 >= nota2 >= nota3:
    meio = nota2
if nota1 >= nota3 >= nota2:
    meio = nota3

print(f"Sua maior nota foi {maior}")
print(f"Sua menor nota foi {menor}, portanto não será considerada")
print(f"Assim. sua média do semestre é {(maior + meio)/2}")

if (maior + meio)/2 >= 6:
    print("Você está aprovado!")
else:
    print("Você foi reprovado!")


