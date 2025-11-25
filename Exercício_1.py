# Aluno: Victor Hugo Carlim Pedroni dos Passos
# Disciplina: Python Scripting - Pós Graduação em Cibersegurança
# Lista 1 - Exercício 1: Elaborar um algoritmo que solicita dois números ao usuário e exibe a soma
# destes números

print(" Calculadora de Soma Simples ")
print("-"*30) # cria uma linha de separação

# Solicita os números com float
variavel_1 = float(input("digite o primeiro número: "))
variavel_2 = float(input("digite o segundo número: "))

# Calcula a soma
soma = variavel_1 + variavel_2

# Exibe o resultado
print("-"*30) # cria uma linha de separação
print(f"A soma dos números é: {soma}")