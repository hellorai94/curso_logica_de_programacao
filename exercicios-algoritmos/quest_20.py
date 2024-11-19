# 20) Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou
# ÍMPAR.

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"{numero} é par.")
else:
    print(f"{numero} é ímpar.")
    