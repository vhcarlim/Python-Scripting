# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 2 - Exercício 2

print(">>> Calculadora de IMC <<<")
print("-"*40)

# Entradas
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Processamento: Fórmula IMC = peso / altura²
imc = peso / (altura ** 2)

print("-"*40)
print(f"Seu IMC é: {imc:.2f}")

# Classificação
if imc < 18.5:
    print("Situação: Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Situação: Peso normal")
elif imc >= 25 and imc < 30:
    print("Situação: Acima do peso")
else:
    print("Situação: Obeso")
