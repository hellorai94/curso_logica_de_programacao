# 25) [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta.
# Analise seus comprimentos e diga se é possível formar um triângulo com essas
# retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento
# de cada lado deve ser menor que a soma dos outros dois.

lado_1 = int(input("Lado 1: "))
lado_2 = int(input("Lado 2: "))
lado_3 = int(input("Lado 3: "))

if ((lado_1 < lado_2 + lado_3) and (lado_2 < lado_1 + lado_3) and (lado_3 < lado_1 + lado_2)):
    print("É um triângulo.")
else:
    print("Não é um triâgulo.")

