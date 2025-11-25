# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 2 - Exercício 8

from datetime import datetime, timedelta

print(">>> Calculadora de Tempo e Datas <<<")
print("-" * 40)

# Entrada de dados
try:
    print("Digite a data inicial:")
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))
    hora = int(input("Hora: "))
    minuto = int(input("Minuto: "))
    segundo = int(input("Segundo: "))

    # Validação e criação do datetime
    data_atual = datetime(ano, mes, dia, hora, minuto, segundo)
    
    print("-" * 40)
    print(f"Data Atual: {data_atual.strftime('%d/%m/%Y %H:%M:%S')}")
    print("-" * 40)

    # Menu de adição
    print("O que você deseja acrescentar?")
    print("1 - Dias")
    print("2 - Horas")
    print("3 - Minutos")
    print("4 - Segundos")
    
    opcao = int(input("Opção: "))
    qtd = int(input("Qual a quantidade a adicionar? "))

    # Calculo da nova data
    nova_data = data_atual

    if opcao == 1:
        nova_data = data_atual + timedelta(days=qtd)
    elif opcao == 2:
        nova_data = data_atual + timedelta(hours=qtd)
    elif opcao == 3:
        nova_data = data_atual + timedelta(minutes=qtd)
    elif opcao == 4:
        nova_data = data_atual + timedelta(seconds=qtd)
    else:
        print("Opção inválida! Nada foi alterado.")

    print("-" * 40)
    print(f"Nova Data Calculada: {nova_data.strftime('%d/%m/%Y %H:%M:%S')}")

except ValueError:
    print("ERRO: Você digitou uma data ou horário inválido (ex: dia 32 ou mês 13).")