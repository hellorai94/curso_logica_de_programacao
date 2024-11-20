# 29) Desenvolva um programa que leia o nome de um funcionário, seu salário,
# quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
# acordo com a tabela a seguir:
# - Até 3 anos de empresa: aumento de 3%
# - entre 3 e 10 anos: aumento de 12.5%
# - 10 anos ou mais: aumento de 20%

nome_funcionario = input("Qual o nome do funcionário? ")
salario = float(input("Qual o salário? "))
anos_trabalhados = float(input(f"Quantos anos {nome_funcionario} trabalha na empresa?"))

if anos_trabalhados < 3:
    salario = salario * 1.03
elif anos_trabalhados < 10:
    salario = salario * 1.125
else:
    salario = salario * 1.2

print(f"O novo salário é de R$ {salario:.2f}.")
