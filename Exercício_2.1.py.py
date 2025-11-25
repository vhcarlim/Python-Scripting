# Aluno: Victor Hugo Carlim Pedroni dos Passos
# Disciplina: Python Scripting - Pós Graduação em Cibersegurança
# Lista 2 - Exercício 1

print(">>> Calculadora de Peso Ideal <<<")
print("-"*40)

# Entrada
altura = float(input("Digite sua altura : "))
sexo = input("Digite o sexo (M para Masculino, F para Feminino): ").upper() #letra maiúscula

print("-"*40)

# Estrutura Condicional
if sexo == "M":
    # Fórmula para homens: (72.7 * h) - 58
    peso_ideal = (72.7 * altura) - 58
    print(f"Sexo: Masculino")
    print(f"Peso Ideal estimado: {peso_ideal:.2f} kg")

elif sexo == "F":
    # Fórmula para mulheres: (62.1 * h) - 44.7
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Sexo: Feminino")
    print(f"Peso Ideal estimado: {peso_ideal:.2f} kg")

else:
    # Caso o usuário digite algo que não seja M nem F
    print("Erro: digite apenas M ou F")