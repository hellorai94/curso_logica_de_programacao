# 16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
# fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
# já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
# quantos dias de vida um fumante perderá e exiba o total em dias.

cig_fumados = int(input("Quantos cigarros você fuma por dia?"))
anos_fumando = int(input("Há quantos anos você é fumante?"))
dias_perdidos = (((10 * cig_fumados) * (anos_fumando * 365)) / 1440)
print(f"Você perdeu {dias_perdidos:.2f} dias.")
