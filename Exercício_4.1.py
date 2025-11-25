# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 4 - Exercício 1

print(">>> Sistema Restaurante Boca Feliz <<<")
print("-" * 50)

# 1. Dados iniciais (fornecidos no PDF)
estoque = {
    'pao': 10,
    'hamburguer': 12,
    'tomate': 5,
    'bacon': 5,
    'ovo': 5
}

cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}

# 2. Loop principal do atendimento
while True:
    print("\n--- Cardápio ---")
    # Mostra as chaves do dicionário (nomes dos lanches)
    for lanche in cardapio:
        print(f"- {lanche}")
    
    print("-" * 50)
    pedido = input("O que deseja pedir (0 para sair)? ").strip().lower()

    # Critério de saída
    if pedido == '0':
        print("Encerrando o sistema... Até logo!")
        break

    # Verifica se o lanche existe no cardápio
    if pedido not in cardapio:
        print("ERRO: Item não localizado no cardápio!")
    
    else:
        # Recupera a lista de ingredientes necessários para esse lanche
        ingredientes_necessarios = cardapio[pedido]
        
        # Passo A: Verificar se TEM tudo no estoque
        pode_preparar = True
        
        for ing in ingredientes_necessarios:
            # Se o ingrediente não existe no estoque ou a quantidade é 0
            if estoque[ing] <= 0:
                pode_preparar = False
                print(f"Infelizmente acabou o ingrediente: {ing}")
                # Não usamos break aqui para mostrar todos os que faltam, se houver mais de um
        
        # Passo B: Se pode preparar, baixamos o estoque e entregamos
        if pode_preparar:
            for ing in ingredientes_necessarios:
                estoque[ing] -= 1 # Diminui 1 unidade
            
            print(f">>> Um {pedido} saindo no capricho!!!")
