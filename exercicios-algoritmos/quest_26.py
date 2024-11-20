# 26) Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
# na tela uma das mensagens abaixo:
# - O primeiro valor é o maior
# - O segundo valor é o maior
# - Não existe valor maior, os dois são iguais

valor_1 = int(input("Qual valor 1?"))
valor_2 = int(input("Qual valor 2?"))

if valor_1 > valor_2:
    print("O primeiro valor é o maior.")
elif valor_2 > valor_1:
    print("O segundo valor é o maior")
else:
    print("Não existe valor maior, os dois são iguais")

    