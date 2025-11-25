# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 3 - Exercício 8

print(">>> Conversor: Binário para Decimal <<<")
print("-" * 50)

# Recebe como string
binario = input("Digite um número binário: ")

decimal = 0
potencia = 0

# [::-1] inverte o texto.
for digito in binario[::-1]:
    if digito == '1':
        # Se for 1, soma 2 elevado à potência atual
        decimal = decimal + (2 ** potencia)
    elif digito != '0':
        print(f"Aviso: '{digito}' não é binário! O cálculo pode dar errado.")
    
    # Aumenta a potência para o próximo dígito (0 -> 1 -> 2...)
    potencia = potencia + 1

print("-" * 50)
print(f"Binário Original: {binario}")
print(f"Decimal Calculado: {decimal}")
