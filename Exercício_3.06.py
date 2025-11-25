# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 3 - Exercício 6

print(">>> Manipulador de Nomes <<<")
print("-" * 50)

# .strip() remove espaços extras no começo e fim
nome_completo = input("Digite seu nome completo: ").strip()

# O comando split() quebra o texto onde tem espaço e cria uma lista
# Ex: "Victor Hugo Carlim" vira ["Victor", "Hugo", "Carlim"]
partes_do_nome = nome_completo.split()

# Pega a primeira palavra (índice 0)
primeiro_nome = partes_do_nome[0]

# Pega a última palavra (índice -1 pega sempre o último item da lista em Python)
ultimo_nome = partes_do_nome[-1]

print("-" * 50)
print(f"Nome Original: {nome_completo}")
print(f"Primeiro Nome: {primeiro_nome}")
print(f"Último Nome:   {ultimo_nome}")
