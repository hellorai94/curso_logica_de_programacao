# 7) Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a
# sua terça parte.
# Ex:
# Digite um número: 3.5
# O dobro de 3.5 é 7.0
# A terça parte de 3.5 é 1.16666

numero = float(input("Digite um número real: "))
dobro = numero * 2
terca = numero / 3
print(f"O dobro de {numero} é {dobro}.")
print(f"A terça parte de {numero} é {terca}.")
