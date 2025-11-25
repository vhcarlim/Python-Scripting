# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 2 - Exercício 3

print(">>> Jogo de Par ou Ímpar <<<")
print("-"*40)

# Entrada
escolha_j1 = input("Jogador 1, você quer PAR ou IMPAR? (P/I): ").upper()

# Entradas dos valores
num_j1 = int(input("Jogador 1, digite seu número (1 a 5): "))
num_j2 = int(input("Jogador 2, digite seu número (1 a 5): "))

print("-"*40)

# Validação dos valores
if (num_j1 < 1 or num_j1 > 5) or (num_j2 < 1 or num_j2 > 5):
    print("ERRO: Os valores devem ser entre 1 e 5")
    print("Esta rodada não valeu!")

else:
    # 2. Processamento do Jogo
    soma = num_j1 + num_j2
    resto = soma % 2
    
    print(f"Soma dos dedos: {num_j1} + {num_j2} = {soma}")

    # Verifica quem ganhou
    if resto == 0:
        print(f"Resultado: {soma} é PAR!")
        if escolha_j1 == "P":
            print(">>> Jogador 1 VENCEU! <<<")
        else:
            print(">>> Jogador 2 VENCEU! <<<")
            
    else:
        print(f"Resultado: {soma} é ÍMPAR!")
        if escolha_j1 == "I":
            print(">>> Jogador 1 VENCEU! <<<")
        else:
            print(">>> Jogador 2 VENCEU! <<<")
