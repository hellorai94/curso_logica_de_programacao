# 10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e
# mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
# sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

largura = float(input("Qual a largura da parede?"))
altura = float(input("Qual a altura da parede?"))

area = largura * altura
quant_tinta = area / 2
print(f"A área a ser pintada é {area}m² e a quantidade de tinta necessária são {quant_tinta} litros.")