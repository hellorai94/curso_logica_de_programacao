# 21) Faça um algoritmo que leia um determinado ano e mostre se ele é ou não
# BISSEXTO.

ano = int(input("Digite um ano: "))

if ano % 400 == 0:
    print(f"{ano} é bissexto.")
elif ano % 4 == 0 and (ano % 100) != 0:
    print(f"{ano} é bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")


