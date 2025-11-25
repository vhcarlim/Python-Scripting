# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 3 - Exercício 9

print(">>> Conversor: Decimal para Hexadecimal <<<")
print("-" * 50)

# Entrada do número decimal
decimal = int(input("Digite um número inteiro: "))
numero_inicial = decimal 

# String auxiliar para mapear os restos (0-15) para caracteres Hex
# Índice 0 é '0', índice 10 é 'A', índice 15 é 'F'
tabela_hex = "0123456789ABCDEF"

hexadecimal = ""

# Lógica de Divisões Sucessivas
if decimal == 0:
    hexadecimal = "0"
else:
    while decimal > 0:
        resto = decimal % 16  # Pega o resto da divisão por 16
        
        # O resto indica qual caractere pegar na tabela
        # Ex: se resto for 10, pega tabela_hex[10] que é 'A'
        digito = tabela_hex[resto]
        
        # Adiciona o dígito à ESQUERDA do resultado (ordem inversa)
        hexadecimal = digito + hexadecimal
        
        # Atualiza o número dividindo por 16 (divisão inteira //)
        decimal = decimal // 16

print("-" * 50)
print(f"Decimal: {numero_inicial}")
print(f"Hexadecimal: {hexadecimal}")
