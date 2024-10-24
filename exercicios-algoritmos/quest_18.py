# 18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade
# dela e depois mostre se ela pode ou não votar.

ano_nasc = int(input("Qual seu ano de nascimento?"))
idade = 2024 - ano_nasc

if idade > 15:
    print("Opa. Você pode votar.")
else:
    print("Ops. Você não pode votar.")
