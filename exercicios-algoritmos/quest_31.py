# 31) [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)

escolha_1 = int(input("1-PEDRA\n2-PAPEL\n3-TESOURA\n"))
escolha_2 = int(input("1-PEDRA\n2-PAPEL\n3-TESOURA\n"))

if escolha_1 == 1 and escolha_2 == 1:
    print("Empate!")
elif escolha_1 == 1 and escolha_2 == 2:
    print("Papel ganha de pedra! 2 ganhou.")
elif escolha_1 == 1 and escolha_2 == 3:
    print("Pedra ganha de tesoura! 1 ganhou.")
elif escolha_1 == 2 and escolha_2 == 1:
    print("Papel ganha de pedra! 1 ganhou.")
elif escolha_1 == 2 and escolha_2 == 2:
    print("Empate!")
elif escolha_1 == 2 and escolha_2 == 3:
    print("Tesoura ganha de papel! 2 ganhou.")
elif escolha_1 == 3 and escolha_2 == 1:
    print("Pedra ganha de tesoura! 2 ganhou.")
elif escolha_1 == 3 and escolha_2 == 2:
    print("Tesoura ganha de papel! 2 ganhou.") 
elif escolha_1 == 3 and escolha_2 == 3:
    print("Empate.")


