# 23) Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
# para todos, mas especialmente para mulheres. Faça um programa que leia nome,
# sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo
# que:
# - Homens ganham 5% de desconto
# - Mulheres ganham 13% de desconto

nome = input("Qual o seu nome?")
sexo = input("Qual o seu sexo?\nF - Mulheres\nM - Homem\n").lower()
valor_compras = float(input("Qual o valor das compras?"))

if sexo == "f":
    valor_desconto = valor_compras * 0.87
    print(f"O valor com desconto é R$ {valor_desconto}")
else:
    valor_desconto = valor_compras * 0.95
    print(f"O valor com desconto é R$ {valor_desconto}")