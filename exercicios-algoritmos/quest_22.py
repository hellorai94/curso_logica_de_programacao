# 22) Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
# situação em relação ao alistamento militar.
# - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o
# alistamento.
# - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do
# alistamento.

ano_nasc = int(input("Qual seu ano de nascimento?"))

idade = 2024 - ano_nasc

if idade >= 18:
    anos_passados = idade - 18
    print(f"Já se passaram {anos_passados} anos do seu período de alistamento.")
else: 
    anos_faltando = 18 - idade
    print(f"Faltam {anos_faltando} anos para o seu período de alistamento.")
    