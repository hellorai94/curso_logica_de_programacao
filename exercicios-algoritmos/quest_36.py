# 36) Um programa de vida saudável quer dar pontos atividades físicas que podem
# ser trocados por dinheiro. O sistema funciona assim:
# - Cada hora de atividade física no mês vale pontos
# - até 10h de atividade no mês: ganha 2 pontos por hora
# - de 10h até 20h de atividade no mês: ganha 5 pontos por hora
# - acima de 20h de atividade no mês: ganha 10 pontos por hora
# - A cada ponto ganho, o cliente fatura R$0,05 (5 centavos)
# Faça um programa que leia quantas horas de atividade uma pessoa teve por mês,
# calcule e mostre quantos pontos ela teve e quanto dinheiro ela conseguiu ganhar.

horas_mes = int(input("Quantas horas de atividade física você fez no mês? "))

if horas_mes <= 10:
    pontos = 2 * horas_mes
elif horas_mes <= 20:
    pontos = 5 * horas_mes
else:
    pontos = 10 * horas_mes

valor_recebido = pontos * 0.05

print(f"Você teve {pontos} pontos e conseguiu ganhar R${valor_recebido:.2f}.")