# 6) Faça um programa que leia um número inteiro e mostre o seu antecessor e seu
# sucessor.
# Ex:
# Digite um número: 9
# O antecessor de 9 é 8
# O sucessor de 9 é 10

numero = int(input("Digite um número inteiro: "))
antecessor = numero - 1
sucessor = numero + 1
print(f"O antecessor é {antecessor}.")
print(f"O sucessor é {sucessor}.")
