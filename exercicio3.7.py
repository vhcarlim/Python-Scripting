# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 3 - Exercício 7

print(">>> Contador de Letras 'A' <<<")
print("-" * 50)
print("Instrução: Digite palavras uma por uma.")
print("Para ENCERRAR, apenas aperte ENTER sem digitar nada.")
print("-" * 50)

total_letras_a = 0

# Loop infinito (True) que só quebra com o comando break
while True:
    palavra = input("Digite uma palavra: ")

    # Se a palavra for vazia (usuário deu Enter sem escrever), para o loop
    if palavra == "":
        break
    
    # 1. Transforma tudo em minúsculo (.lower)
    # 2. Conta quantos 'a' existem (.count)
    qtd = palavra.lower().count('a')
    
    # Adiciona ao contador total
    total_letras_a = total_letras_a + qtd

print("-" * 50)
print(f"Total de letras 'A' (e 'a') encontradas: {total_letras_a}")