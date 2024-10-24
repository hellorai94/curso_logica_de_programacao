# 19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua
# média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
# não um bom aproveitamento (se ficou acima da média 7.0).

nota_1 = float(input("Qual a 1ª nota do aluno?"))
nota_2 = float(input("Qual a 2ª nota do aluno?"))
media = (nota_1 + nota_2) / 2
if media >= 7:
    print(f"Aprovado. Sua média foi {media}.")
else:
    print(f"Reprovado. Sua média foi {media}.")