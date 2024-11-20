# 37) Uma empresa precisa reajustar o salário dos seus funcionários, dando um
# aumento de acordo com alguns fatores. Faça um programa que leia o salário atual,
# o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa.
# No final, mostre o seu novo salário, baseado na tabela a seguir:
# - Mulheres
# - menos de 15 anos de empresa: +5%
# - de 15 até 20 anos de empresa: +12%
# - mais de 20 anos de empresa: +23%
# - Homens
# - menos de 20 anos de empresa: +3%
# - de 20 até 30 anos de empresa: +13%
# - mais de 30 anos de empresa: +25%

salario_atual = float(input("Qual o salário atual do funcionário? "))
genero = int(input("1-Feminino\n2-Masculino\n"))
anos_trabalhados = int(input("Há quantos anos o funcionário trabalha na empresa? "))

if genero == 1:
    if anos_trabalhados < 15:
        salario = salario_atual * 1.05
    elif anos_trabalhados <= 20:
        salario = salario_atual * 1.12
    else:
        salario = salario_atual * 1.23
elif genero == 2:
    if anos_trabalhados < 20: 
        salario = salario_atual * 1.03
    elif anos_trabalhados <= 30:
        salario = salario_atual * 1.13
    else:
        salario = salario_atual * 1.25
print(f"O salário atualizado é de R${salario}.")