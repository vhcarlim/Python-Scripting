# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 2 - Exercício 4

print(">>> Calculadora de Pagamento <<<")
print("-" * 40)

# Entrada do valor do produto
preco_etiqueta = float(input("Valor do produto (R$): "))

# Menu de opções para o usuário saber o que digitar
print("\nEscolha a condição de pagamento:")
print("1 - À vista (Dinheiro/Cheque) -> 10% de desconto")
print("2 - À vista (Cartão de Crédito) -> 15% de desconto")
print("3 - Em 2x (Sem juros) -> Preço Normal")
print("4 - Em 2x (Com juros) -> 10% de juros")

codigo = int(input("\nDigite o código da opção (1 a 4): "))
print("-" * 40)

# Processamento condicional
if codigo == 1:
    # 10% de desconto
    desconto = preco_etiqueta * 0.10
    total = preco_etiqueta - desconto
    print(f"Condição: À vista (Dinheiro/Cheque)")
    print(f"Desconto aplicado: R$ {desconto:.2f}")
    print(f"Valor Final: R$ {total:.2f}")

elif codigo == 2:
    # 15% de desconto
    desconto = preco_etiqueta * 0.15
    total = preco_etiqueta - desconto
    print(f"Condição: À vista (Cartão)")
    print(f"Desconto aplicado: R$ {desconto:.2f}")
    print(f"Valor Final: R$ {total:.2f}")

elif codigo == 3:
    # Preço normal (sem juros)
    total = preco_etiqueta
    parcela = total / 2
    print(f"Condição: 2x Sem Juros")
    print(f"Valor Final: R$ {total:.2f}")
    print(f"Valor da Parcela: 2x de R$ {parcela:.2f}")

elif codigo == 4:
    # 10% de juros
    juros = preco_etiqueta * 0.10
    total = preco_etiqueta + juros
    parcela = total / 2
    print(f"Condição: 2x Com Juros (10%)")
    print(f"Juros adicionado: R$ {juros:.2f}")
    print(f"Valor Final: R$ {total:.2f}")
    print(f"Valor da Parcela: 2x de R$ {parcela:.2f}")

else:
    print("ERRO: Código de pagamento inválido!")
