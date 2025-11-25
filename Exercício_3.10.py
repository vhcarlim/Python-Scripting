# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 3 - Exercício 10

from datetime import date

print(">>> Calculadora de Intervalo entre Datas <<<")
print("-" * 50)

# Função auxiliar para não repetir o código de input duas vezes
def ler_data(nome_data):
    print(f"\nDigite a {nome_data}:")
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))
    return date(ano, mes, dia)

# 1. Entrada das duas datas
print("Vamos calcular a distância entre duas datas.")
data_1 = ler_data("Primeira Data")
data_2 = ler_data("Segunda Data")

# 2. Cálculo da diferença
# Ao subtrair dois objetos 'date', o Python gera um 'timedelta'
diferenca = data_2 - data_1

# A função abs() garante que o número seja positivo, 
# mesmo que o usuário digite a data mais recente primeiro.
qtd_dias = abs(diferenca.days)

# 3. Saída
print("-" * 50)
# Formatando a data para o padrão brasileiro (dia/mês/ano)
d1_str = data_1.strftime('%d/%m/%Y')
d2_str = data_2.strftime('%d/%m/%Y')

print(f"Data 1: {d1_str}")
print(f"Data 2: {d2_str}")
print(f"\nDiferença calculada: {qtd_dias} dias")
print("(O cálculo já considerou automaticamente os anos bissextos no caminho)")
