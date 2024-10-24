ano_atual = int(input("Em que ano estamos?"))
ano_nasc = int(input("Em qual ano você nasceu?"))
idade = ano_atual - ano_nasc
print(f"Você tem {idade} anos.")

if idade > 17:
    print("Você é maior de idade.")
else:
    print("Sortudo.")

    