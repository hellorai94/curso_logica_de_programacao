# 13) Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o
# seu novo salário, com 15% de aumento.

salario = float(input("Qual seu salário(R$)?"))
salario_desc = salario * 0.85
print(f"Seu salário com desconto é R$ {salario_desc}")