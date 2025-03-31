velocidade = float(input("Qual a velocidade média do veículo?"))

if velocidade > 80:
    print("Vixe... Você foi multado(a)!")
    velocidade_amais = (velocidade - 80)*5
    print("O valor da sua multa é", velocidade_amais)
    print("Mais cuidado da próxima vez!")
else:
    print("Glória! Você não foi multado!")
