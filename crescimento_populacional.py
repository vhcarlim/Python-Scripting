# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 3 - Exercício 5

print(">>> Calculadora de Crescimento Populacional <<<")
print("-" * 50)

# Dados iniciais
pop_a = 5000000  # 5 milhões
taxa_a = 0.03    # 3%

pop_b = 7000000  # 7 milhões
taxa_b = 0.02    # 2%

anos = 0

print(f"Ano 0 -> País A: {pop_a} | País B: {pop_b}")

# Loop: Continua rodando enquanto a população de A for menor ou igual a B
while pop_a <= pop_b:
    # Aumenta a população baseada na taxa (População atual * taxa)
    pop_a = pop_a + (pop_a * taxa_a)
    pop_b = pop_b + (pop_b * taxa_b)
    
    anos = anos + 1 # Passou mais um ano

print("-" * 50)
print(f"Resultado alcançado em: {anos} anos.")
print(f"População Final A: {int(pop_a)}") # int() tira as casas decimais de pessoas
print(f"População Final B: {int(pop_b)}")

#resultado é 35 anos