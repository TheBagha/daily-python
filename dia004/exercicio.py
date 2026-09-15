# Exercício: classificar uma pessoa pela idade

print("----- Classificação por idade -----")

idade = int(input("Digite sua idade: "))

if idade < 0:
    print("A idade não pode ser negativa.")
elif idade <= 12:
    print("Você é uma criança.")
elif idade <= 17:
    print("Você é um adolescente.")
elif idade <= 59:
    print("Você é um adulto.")
else:
    print("Você é uma pessoa idosa.")
