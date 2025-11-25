# Aluno: Victor Hugo Carlim Pedroni dos Passos
# Disciplina: Python Scripting - Pós Graduação em Cibersegurança
# Lista 1 - Exercício 5: Estender o exercício 4 anterior informando que para pagamento à vista tem 15% de desconto, calculando e exibindo este valor

print(">>> Caixa com Desconto (À Vista) <<<")
print("-"*40)

# Entradas
produto = input("Nome do produto: ")
quantidade_compra = int(input("Quantidade levada: "))
valor_unitario = float(input("Valor unitário (R$): "))

# Processamento
total_bruto = quantidade_compra * valor_unitario

# Calculando 15% de desconto
valor_desconto = total_bruto * 0.15
total_final = total_bruto - valor_desconto

# Saída
print("-" * 40)
print(f"Produto: {produto}")
print(f"Total Original: R$ {total_bruto:.2f}")
print(f"Desconto (15%): - R$ {valor_desconto:.2f}")
print(f"Valor a Pagar: R$ {total_final:.2f}")