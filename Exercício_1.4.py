# Aluno: Victor Hugo Carlim Pedroni dos Passos
# Disciplina: Python Scripting - Pós Graduação em Cibersegurança
# Lista 1 - Exercício 4: Elaborar um algoritmo que solicita o nome de um produto, seu valor e quantidade, informando o valor de compra calculado

print(">>> Caixa de Supermercado <<<")
print("-"*40)

# Dados da compra
produto = input("Nome do produto: ")
quantidade_compra = int(input("Quantidade levada: ")) 
valor_unitario = float(input("Valor unitário (R$): "))

# Cálculo do valor total
valor_total = quantidade_compra * valor_unitario

# Resultado
print("-"*40)
print(f"Produto: {produto}")
print(f"Valor Total da Compra: R$ {valor_total:.2f}")
