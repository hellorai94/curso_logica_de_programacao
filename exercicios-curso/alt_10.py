massa = float(input("Qual o seu peso? "))
altura = float(input("Qual sua altura? "))

imc = (massa / (altura ** 2) )
print(f"Seu imc é {imc}.")
if imc >= 18.5 and imc < 25:
    print("Você está no seu peso ideal!")
else:
    print("Você não está a faixa de peso ideal!.")