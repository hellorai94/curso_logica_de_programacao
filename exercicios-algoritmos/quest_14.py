# 14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
# um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
# sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

km_rodados = float(input("Quantos KM você percorreu?"))
dias = int(input("Por quantos dias o carro ficou alugado?"))
valor_pagar =((km_rodados * 0.2) + (dias * 90))
print(f"O valor a pagar é R$ {valor_pagar:.2f}.")
