# 17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
# 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
# o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida

vel_carro = float(input("Qual velocidade do carro?"))

if vel_carro > 80:
    multa = vel_carro - 80
    valor_multa = 5 * multa
    print(f"Você foi multado e o valor da multa é de R$ {valor_multa}.")
else:
    print(f"Continue respeitando as leis de trânsito.")