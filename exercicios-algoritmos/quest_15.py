# 15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o
# salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25
# por hora trabalhada.

dias_trabalhados = int(input("Quantos dias o funcionário trabalhou?"))
salario = (8 * dias_trabalhados) * 25
print(f"O salário do funcionário é de R$ {salario:.2f}.")
