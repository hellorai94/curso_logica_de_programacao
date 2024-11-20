# 27) Crie um programa que leia duas notas de um aluno e calcule a sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média até 4.9: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))

media = (nota_1 + nota_2) / 2

if media <= 4.9:
    print("REPROVADO.")
elif media <= 6.9:
    print("RECUPERAÇÃO.")
elif media >= 7:
    print("APROVADO.")