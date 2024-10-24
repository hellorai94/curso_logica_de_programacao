# 9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$)
# e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.

real = float(input("Quanto reais (R$) você tem? "))
dolar = real / 5.71
print(f"R$ {real} equivale a $ {dolar:.2f}.")