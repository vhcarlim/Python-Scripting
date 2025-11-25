# Aluno: Victor Hugo Carlim Pedroni dos Passos
# Disciplina: Python Scripting - Pós Graduação em Cibersegurança
# Lista 1 - Exercício 3: Elaborar um algoritmo que solicita ao usuário o nome de uma disciplina e suas  4 notas bimestrais. O algoritmo deve calcular a média destas notas, e uma  mensagem informando que a média da disciplina nome é média

print(">>> Cálculo de Média Escolar <<<")
print("-"*40)

# Entrada
nome_materia = input("Digite o nome da disciplina: ")

# Processamento: 4 notas em float
nota1 = float(input("Nota do 1º Bimestre: "))
nota2 = float(input("Nota do 2º Bimestre: "))
nota3 = float(input("Nota do 3º Bimestre: "))
nota4 = float(input("Nota do 4º Bimestre: "))

# Processamento: Soma tudo e divide por 4
media_final = (nota1 + nota2 + nota3 + nota4) / 4

# Saída
print("-"*40)
print(f"Disciplina: {nome_materia}")
print(f"Média Final: {media_final:.2f}") # .2f para formatar o número e aparecer apenas 2 casas decimais