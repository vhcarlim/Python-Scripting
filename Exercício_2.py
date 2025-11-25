# Aluno: Victor Hugo Carlim Pedroni dos Passos
# Disciplina: Python Scripting - Pós Graduação em Cibersegurança
# Lista 1 - Exercício 2: Elaborar um algoritmo que solicita ao usuário seu ano de nascimento e calcula
# sua idade com relação ao ano de 2020, sendo que o usuário já fez aniversário
# neste ano

print(">>> Calculadora de Idade (Base 2020) <<<")
print("-"*40)

# Entrada
ano_de_nascimento = int(input("Digite o ano em que você nasceu: "))

# Processamento
idade_calculada = 2020 - ano_de_nascimento

# Saída
print("-"*40)
print(f"Sua idade (considerando o ano de 2020) é: {idade_calculada} anos")