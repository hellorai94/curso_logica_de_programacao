# 11) Desenvolva uma lógica que leia os valores de A, B e C de uma equação do
# segundo grau e mostre o valor de Delta.

# Δ = b2 – 4ac

valor_a = float(input("Qual valor de a?"))
valor_b = float(input("Qual valor de b?"))
valor_c = float(input("Qual valor de c?"))

delta = ((valor_b ** 2) - (4 * valor_a * valor_c))
print(f"O valor de delta é {delta}.")