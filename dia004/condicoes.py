# Condiconais

idade = 18

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

nota = 8

if nota >= 7:
    resultado = "Aprovado"
elif nota >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print(f"Nota: {nota} - {resultado}")

# Mais de uma condição
tem_ingresso = True

if idade >= 18 and tem_ingresso:
    print("Entrada liberada")
else:
    print("Entrada não liberada")
