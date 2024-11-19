nota_um = float(input("Nota 1: "))
nota_dois = float(input("Nota 2: "))

media = (nota_um + nota_dois) / 2

if media >= 9:
    aproveitamento = "A"
elif media >= 8:
    aproveitamento = "B"
elif media >= 7:
    aproveitamento = "C"
elif media >= 6:
    aproveitamento = "D"
elif media >= 5:
    aproveitamento = "E"
else:
    aproveitamento = "F"

print(f"A média é: {media:.2f}.")
print(f"Aproveitamento: {aproveitamento}.")


