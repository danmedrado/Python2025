velocidade = float(input("Qual a velocidade do veículo ao passar pelo radar?"))

if velocidade > 80:
    print("Vixe... Você foi multado(a)!")
    multa = (velocidade-80) * 5
    print(f"O valor da sua multa é R$ {multa:.2f}")
    print("Mais cuidado da próxima vez!")
else:
    print("Glória! Você não foi multado!")
