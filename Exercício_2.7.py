# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 2 - Exercício 7

print(">>> Formatador de Datas <<<")
print("-" * 40)

# Solicitando os dados
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês (1-12): "))
ano = int(input("Digite o ano (4 dígitos): "))

# Menu de opções
print("\nComo você quer ver a data?")
print("1 - Simples (10/08/1990)")
print("2 - Abreviada (10/ago/1990)")
print("3 - Completa (10 de agosto de 1990)")
opcao = int(input("Escolha (1-3): "))

print("-" * 40)

# Lista auxiliar para os nomes dos meses
nomes_meses = ["", "janeiro", "fevereiro", "março", "abril", "maio", "junho",
               "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

nomes_abrev = ["", "jan", "fev", "mar", "abr", "mai", "jun",
               "jul", "ago", "set", "out", "nov", "dez"]

if opcao == 1:
    # Formato: dd/mm/aaaa
    print(f"Data: {dia:02d}/{mes:02d}/{ano}")

elif opcao == 2:
    # Formato: dd/mmm/aaaa
    nome_mes = nomes_abrev[mes]
    print(f"Data: {dia:02d}/{nome_mes}/{ano}")

elif opcao == 3:
    # Formato: dd de mês de aaaa
    nome_mes = nomes_meses[mes]
    print(f"Data: {dia} de {nome_mes} de {ano}")

else:
    print("Opção inválida! Escolha 1, 2 ou 3.")