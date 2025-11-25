# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 3 - Exercício 2

print(">>> Buscador de Números (Resto 5 na divisão por 11) <<<")
print("-" * 50)

# O range(1000, 2000) vai de 1000 até 1999 (o último não conta)
for numero in range(1000, 2000):
    
    # Verifica se o resto da divisão por 11 é igual a 5
    if numero % 11 == 5:
        print(f"Número encontrado: {numero}")

print("-" * 50)
print("fim")
