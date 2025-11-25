# Aluno: Victor Hugo Carlim
# Disciplina: Python Scripting - Pós Cibersegurança
# Lista 2 - Exercício 9

print(">>> Validador de CPF <<<")
print("-" * 40)

# Entrada
cpf_texto = input("Digite o CPF (apenas números, sem pontos/traço): ")

# Verificação inicial
if len(cpf_texto) != 11 or not cpf_texto.isdigit():
    print("ERRO: O CPF deve conter exatamente 11 números.")
else:
    # Converte o texto em uma lista de números inteiros para fazer a conta
    cpf = [int(digito) for digito in cpf_texto]

    # Validação do 1º dígito
    soma_1 = 0
    peso_1 = 10
    
    # 9 primeiros dígitos
    for i in range(9):
        soma_1 += cpf[i] * peso_1
        peso_1 -= 1 # O peso desce: 10, 9, 8...
    
    # Lógica do resto: (Soma * 10) / 11
    resto_1 = (soma_1 * 10) % 11
    
    # Regra: Se o resto for 10, o dígito é 0
    if resto_1 == 10:
        resto_1 = 0
        
    # Validação do 2º dígito
    soma_2 = 0
    peso_2 = 11
    
    # Pega os 10 primeiros dígitos (os 9 originais + o 1º verificador)
    for i in range(10):
        soma_2 += cpf[i] * peso_2
        peso_2 -= 1 # em decrescente
        
    resto_2 = (soma_2 * 10) % 11
    
    if resto_2 == 10:
        resto_2 = 0

    # Resultado final
    print("-" * 40)
    # Compara os restos calculados com os dígitos reais do CPF (posições 9 e 10 da lista)
    if resto_1 == cpf[9] and resto_2 == cpf[10]:
        print(f"CPF {cpf_texto} é VÁLIDO!")
    else:
        print(f"CPF {cpf_texto} é INVÁLIDO.")
        print(f"Esperado: {resto_1}{resto_2}")
        print(f"Encontrado: {cpf[9]}{cpf[10]}")