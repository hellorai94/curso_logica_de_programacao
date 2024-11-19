# 24) Faça um algoritmo que pergunte a distância que um passageiro deseja
# percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para
# viagens até 200Km e R$0.45 para viagens mais longas.

dist_km = float(input("Qual distância você deseja percorrer? "))

if dist_km <= 200:
    preco = dist_km * 0.5
else:
    preco = dist_km * 0.45
print(f"O preço a ser pago por percorrer {dist_km} será de R${preco:.2f}.")
