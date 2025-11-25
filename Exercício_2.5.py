# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 2 - Exercício 5

print(">>> Calculadora de Passagens Aéreas <<<")
print("-" * 40)

# Destinos
print("Escolha o destino:")
print("1 - Região Norte")
print("2 - Região Nordeste")
print("3 - Região Centro-Oeste")
print("4 - Região Sul")
destino = int(input("Digite o número da região (1-4): "))

# Tipo de Viagem
print("\nTipo de viagem:")
print("1 - Apenas Ida")
print("2 - Ida e Volta")
tipo_viagem = int(input("Digite o número do tipo (1 ou 2): "))

print("-" * 40)
valor = 0

# Cálculo do valor baseado no destino e tipo de viagem
if destino == 1: # Norte
    regiao = "Norte"
    if tipo_viagem == 1:
        valor = 500.00
    elif tipo_viagem == 2:
        valor = 900.00
    else:
        print("Tipo de viagem inválido!")

elif destino == 2: # Nordeste
    regiao = "Nordeste"
    if tipo_viagem == 1:
        valor = 350.00
    elif tipo_viagem == 2:
        valor = 650.00
    else:
        print("Tipo de viagem inválido!")

elif destino == 3: # Centro-Oeste
    regiao = "Centro-Oeste"
    if tipo_viagem == 1:
        valor = 350.00
    elif tipo_viagem == 2:
        valor = 600.00
    else:
        print("Tipo de viagem inválido!")

elif destino == 4: # Sul
    regiao = "Sul"
    if tipo_viagem == 1:
        valor = 300.00
    elif tipo_viagem == 2:
        valor = 550.00
    else:
        print("Tipo de viagem inválido!")

else:
    print("Região inválida! Escolha entre 1 e 4.")
    valor = 0 # Para não imprimir preço errado

# Só mostra o resultado se o valor for maior que 0
if valor > 0:
    tipo_texto = "Apenas Ida" if tipo_viagem == 1 else "Ida e Volta"
    print(f"Destino: Região {regiao}")
    print(f"Viagem: {tipo_texto}")
    print(f"Valor Total: R$ {valor:.2f}")