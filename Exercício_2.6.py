# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 2 - Exercício 6

import math # para fazer raiz quadrada

print(">>> Calculadora de Bhaskara <<<")
print("-" * 40)

# Entrada dos coeficientes
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

# Calcular o Delta (b² - 4ac)
delta = (b ** 2) - (4 * a * c)

print("-" * 40)
print(f"Valor de Delta: {delta}")

# Analisar o Delta para encontrar as raízes
if delta < 0:
    print("O Delta é negativo. A equação não possui raízes reais.")

elif delta == 0:
    # Apenas uma raiz
    raiz = (-b) / (2 * a)
    print("O Delta é zero. A equação possui apenas uma raiz real:")
    print(f"X = {raiz:.2f}")

else:
    # Duas raízes (Delta positivo)
    # math.sqrt calcula a raiz quadrada
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    
    print("A equação possui duas raízes reais:")
    print(f"X1 = {raiz1:.2f}")
    print(f"X2 = {raiz2:.2f}")