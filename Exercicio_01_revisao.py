#12. Escreva um programa que receba 2 valores do tipo
# inteiro x e y, e calcule o valor de z:
# z = (x2 + y2) / (x – y)2

#x = int(input("x = "))
#y = int(input("y = "))
#z = (x**2 + y**2) / (x - y)**2
#print("z =",z)


#Valores decimais

x = float(input("x = "))
y = float(input("y = "))
z = (x**2 + y**2) / (x - y)**2
print(f"z =",{z:.2f})