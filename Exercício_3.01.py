# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 3 - Exercício 1

print(">>> Calculadora de Decaimento Radioativo <<<")
print("-" * 40)

# Entrada da massa inicial
massa = float(input("Digite a massa inicial (em gramas): "))
tempo_total = 0 # O tempo começa em zero

# Salva a massa original só para mostrar no final
massa_original = massa

# Loop: Continua dividindo enquanto a massa for maior ou igual a 0.5g
while massa >= 0.5:
    massa = massa / 2
    tempo_total = tempo_total + 50 # Passaram-se mais 50 segundos

print("-" * 40)
print(f"Massa Inicial: {massa_original} g")
print(f"Massa Final: {massa:.4f} g") # .4f mostra 4 casas decimais para ver números pequenos
print(f"Tempo Necessário: {tempo_total} segundos")

# Extra: Converter para minutos e segundos se quiser
minutos = tempo_total // 60
segundos_rest = tempo_total % 60
print(f"Tempo Formatado: {minutos} min e {segundos_rest} seg")
