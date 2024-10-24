# 3) Crie um programa que leia o nome e o salário de um funcionário, mostrando no
# final uma mensagem.
# Ex:
# Nome do Funcionário: Maria do Carmo
# Salário: 1850,45
# O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.

nome_funcionario = input("Qual nome do funcionário? ")
salario = float(input("Qual salário do funcionário? "))

print(f"O nome do funcionário é {nome_funcionario}.")
print(f"O salário de {nome_funcionario} é R$ {salario}.")
