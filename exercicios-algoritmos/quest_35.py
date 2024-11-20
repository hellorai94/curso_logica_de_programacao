# 35) Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O
# aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para
# carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa
# que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e
# quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a
# tabela a seguir:
# - Carros populares (aluguel de R$90 por dia)
# - Até 100Km percorridos: R$0,20 por Km
# - Acima de 100Km percorridos: R$0,10 por Km
# - Carros de luxo (aluguel de R$150 por dia)
# - Até 200Km percorridos: R$0,30 por Km
# - Acima de 200Km percorridos: R$0,25 por Km

tipo_carro = int(input("Escolha o carro:1-Popular\n2-Luxo\n"))
dias_aluguel = int(input("Serão quantos dias de aluguel? "))
km_percorridos = float(input("Foram quantos km percorridos? "))

if tipo_carro == 1:
    if km_percorridos <= 100:
        valor = (90 * dias_aluguel) + (0.2 * km_percorridos)
    else:
        valor = (90 * dias_aluguel) + (0.1 * km_percorridos)
elif tipo_carro == 2:
    if km_percorridos <= 200:
        valor = (150 * dias_aluguel) + (0.3 * km_percorridos)
    else:
        valor = (150 * dias_aluguel) + (0.25 * km_percorridos)
print(f"O valor a ser pago é de R${valor:.2f}.")