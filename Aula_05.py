# Escreva um programa que leia numeros inteiros do teclado.
# O programa deve ser os números até que o usuário digite 0
# No final da execução exiba a quantidade de números digitados,
# assim como a soma e a média aritimética

soma = 0
quant = 0
while True:
    x = int(input("Digite um número a ser somado ou 0 (zero) para encerrar a soma:"))
    if x == 0:
        break
    soma+=x
    quant+=1

print(f"A soma total dos números é: {soma}")
print(f"A quantidade de numeros somados foi: {quant}")
print(f"A média é: {soma/quant}")