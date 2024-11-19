print("-------------------------------")
print("       CRIANÇA ESPERANÇA       ")
print("-------------------------------")
print("Muito obrigado por ajudar      ")
print(" [1] para doar R$1O.")
print(" [2] para doar R$2O.")
print(" [3] para doar R$3O.")
print(" [4] para doar outros valores.")
print(" [5] para cancelar.")

escolha = int(input("Escolha: "))
valor = 0

if escolha == 1:
    valor = 10
elif escolha == 2:
    valor = 20
elif escolha == 3:
    valor = 30
elif escolha == 4:
    valor = int(input("Qual o valor da doação? R$"))

print("-------------------------------")
print(f"Sua doação foi de R$ {valor}")
print("Muito obrigado!!")
print("-------------------------------")
