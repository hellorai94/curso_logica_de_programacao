# 32) [DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
# jogador vai tentar descobrir qual foi o valor sorteado.

computador = 3

num_jogador = int(input("Escolha um número de 1 a 5. "))

if num_jogador == computador:
    print(f"Acertou! O número é {computador}")
elif num_jogador > computador:
    print(f"O número é menor que {num_jogador}.")
elif num_jogador < computador:
    print(f"O número é maior que {num_jogador}.")

