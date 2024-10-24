# 12) Crie um programa que leia o preço de um produto, calcule e mostre o seu
# PREÇO PROMOCIONAL, com 5% de desconto.

preco = float(input("Qual o valor do produto? "))
preco_desc = preco * 0.95

print(f"R$ {preco} com 5% de desconto fica R$ {preco_desc}.")
