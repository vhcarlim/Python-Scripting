# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 4 - Exercício 2

print(">>> Conversor Espacial - Frota Alfa <<<")
print("-" * 50)

# 1. Base de Dados (Copiado do PDF)
# Esses valores representam quanto vale 1 Ano-Luz em cada unidade
fatores_conversao = {
    "pc": 0.31,           # Parsec
    "al": 1.0,            # Ano-Luz (Base)
    "ae": 63241.09,       # Unidade Astronômica
    "ml": 525960.23,      # Minuto-Luz
    "sl": 31557609.92     # Segundo-Luz
}

lista_unidades = [
    "Parsec (pc)", 
    "Ano-Luz (al)", 
    "Unidade Astronômica (ae)", 
    "Minuto-Luz (ml)", 
    "Segundo-Luz (sl)"
]

# 2. Exibindo as opções
print("Unidades disponíveis:")
for item in lista_unidades:
    print(f"- {item}")

print("-" * 50)

# 3. Entrada de Dados
try:
    valor = float(input("Valor a ser convertido: "))
    # .strip().lower() garante que funcione mesmo se digitar com espaço ou maiúscula
    unidade_origem = input("Converter de (sigla): ").strip().lower()
    unidade_destino = input("Converter para (sigla): ").strip().lower()

    # 4. Verificação e Cálculo
    if unidade_origem in fatores_conversao and unidade_destino in fatores_conversao:
        
        # Recupera os fatores do dicionário
        fator_de = fatores_conversao[unidade_origem]
        fator_para = fatores_conversao[unidade_destino]
        
        # Cálculo: (Valor * Fator Destino) / Fator Origem
        # Explicação: Primeiro transformamos em Anos-Luz, depois para o destino
        valor_convertido = valor * (fator_para / fator_de)
        
        print("-" * 50)
        print(f"Conversão: {valor} {unidade_origem} = {valor_convertido:.4f} {unidade_destino}")
        
    else:
        print("\nERRO: Uma das siglas digitadas não existe no sistema.")

except ValueError:
    print("\nERRO: O valor digitado não é um número válido.")

print("-" * 50)
print("Fim da transmissão da Frota Alfa.")
