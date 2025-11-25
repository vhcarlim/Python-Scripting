# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 3 - Exercício 3

print(">>> Pedra, Papel e Tesoura (Melhor de X) <<<")
print("-" * 50)

# Pontos para ganhar o jogo
pontos_para_vencer = int(input("Quantos pontos para vencer o jogo? "))

placar_j1 = 0
placar_j2 = 0

print(f"\nO jogo vai até {pontos_para_vencer} pontos. Valendo!")

# O Loop roda enquanto ninguém tiver atingido a pontuação máxima
while placar_j1 < pontos_para_vencer and placar_j2 < pontos_para_vencer:
    print("-" * 50)
    print(f"Placar Atual: J1 [{placar_j1}] x [{placar_j2}] J2")
    
    # Entradas (pedra, papel ou tesoura)
    j1 = input("Jogador 1 (pedra, papel, tesoura): ").strip().lower()
    j2 = input("Jogador 2 (pedra, papel, tesoura): ").strip().lower()

    if j1 == j2:
        print(">> Empate nesta rodada!")
    
    # Vitória do Jogador 1
    elif (j1 == "pedra" and j2 == "tesoura") or \
         (j1 == "papel" and j2 == "pedra") or \
         (j1 == "tesoura" and j2 == "papel"):
        print(">> Ponto para o Jogador 1!")
        placar_j1 = placar_j1 + 1 # Soma 1 ponto
        
    # J2 ganhou
    else:
        print(">> Ponto para o Jogador 2!")
        placar_j2 = placar_j2 + 1 # Soma 1 ponto

# Fim do Loop
print("=" * 50)
print(f"PLACAR FINAL: J1 [{placar_j1}] x [{placar_j2}] J2")

if placar_j1 > placar_j2:
    print("PARABÉNS! O Jogador 1 é o CAMPEÃO!")
else:
    print("PARABÉNS! O Jogador 2 é o CAMPEÃO!")