print("===============Departamento de Transito===============")

ano_atual = int(input("Em que ano estamos?"))
ano_nasc = int(input("Em qual ano você nasceu?"))

idade = ano_atual - ano_nasc
print("===============STATUS===============")
print(f"Idade: {idade} anos.")
if idade > 17: 
    print("Apto a tirar a carteira.")
else:
    print("Não apto a tirar a carteira.")
    

