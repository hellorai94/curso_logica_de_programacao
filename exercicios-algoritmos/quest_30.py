# 30) [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo
# de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais
# - ESCALENO: todos os lados diferentes

lado_1 = int(input("Lado 1: "))
lado_2 = int(input("Lado 2: "))
lado_3 = int(input("Lado 3: "))

tri = ((lado_1 < lado_2 + lado_3) and (lado_2 < lado_1 + lado_3) and (lado_3 < lado_1 + lado_2))

if tri:
    if (lado_1 == lado_2 == lado_3):
        tipo = "Equilátero"
    elif (lado_1 != lado_2) and (lado_2 != lado_3) and (lado_1 != lado_3):
        tipo = "Escaleno"
    else:
        tipo = "Isósceles"
    print(f"O triângulo é {tipo}.")

else:
    print("Não é um triângulo.")



