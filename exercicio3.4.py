# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 3 - Exercício 4

print(">>> Ordenador de Números <<<")
print("-" * 50)

lista_numeros = []

# 1. Loop para pedir os 5 números
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(num)

print("-" * 50)
print(f"Lista Original: {lista_numeros}")

# 2. Usando Laços para Ordenar (Lógica Bubble Sort)
# Esse loop vai até o penúltimo item
for i in range(len(lista_numeros) - 1):
    # Esse loop compara o item atual com o próximo
    for j in range(len(lista_numeros) - 1 - i):
        # Se o número atual for MAIOR que o próximo, eles trocam de lugar
        if lista_numeros[j] > lista_numeros[j+1]:
            temp = lista_numeros[j]
            lista_numeros[j] = lista_numeros[j+1]
            lista_numeros[j+1] = temp

# 3. Exibindo o resultado
print(f"Lista Ordenada: {lista_numeros}")
print("-" * 50)