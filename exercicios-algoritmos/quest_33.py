# 33) Escreva um programa para aprovar ou não o empréstimo bancário para a compra
# de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
# em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
# ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Qual o valor da casa?"))
salario_comprador = float(input("Qual o salário do comprador?"))
anos_pagar = int(input("Em quantos anos você pretende pagar? "))

salario_percentual = salario_comprador * 0.3
prestacao_mensal = (valor_casa / (anos_pagar * 12))

if prestacao_mensal > salario_percentual:
    print(f"Empréstimo negado. Presta mensal R${prestacao_mensal:.2f} é maior que 30% do salário R${salario_percentual:.2f}.")
else:
    print(f"Empréstimo aprovado. A prestação mensal será de R${prestacao_mensal:.2f}.")
