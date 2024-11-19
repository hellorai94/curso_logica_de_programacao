lado_1 = int(input("Lado 1: "))
lado_2 = int(input("Lado 2: "))
lado_3 = int(input("Lado 3: "))

tri = ((lado_1 < lado_2 + lado_3) and (lado_2 < lado_1 + lado_3) and (lado_3 < lado_1 + lado_2))
eq = (lado_1 == lado_2 == lado_3) 
esc = (lado_1 != lado_2) and (lado_2 != lado_3) and (lado_1 != lado_3)
iso = ((lado_1 == lado_2) and (lado_1 != lado_3)) or ((lado_3 == lado_2) and (lado_1 != lado_3)) or ((lado_1 == lado_3) and (lado_1 != lado_2))


print(f"É triângulo? {tri}.")
print(f"É equilátero? {eq}.")
print(f"É escaleno? {esc}.")
print(f"É isóceles? {iso}.")
