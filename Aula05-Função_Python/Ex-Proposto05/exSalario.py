# Programa que utiliza função para determinar o cálculo do salário e retorna o valor a ser pago conforme o número de horas trabalhadas.

print("Programa que determina o salário")
def calcula_pagamento(qtd_horas, valor_hora):
    horas = qtd_horas
    taxa = valor_hora
    if horas <= 40:
        salario = horas*taxa
    else:
        h_excd = horas - 40
        salario = 40*taxa+(h_excd*(1.5*taxa))
    return salario


horas = float(input("Digite as horas: "))
taxa_valor = float(input("Digite a taxa: "))
total_salario = calcula_pagamento(horas,taxa_valor)

print('O valor a receber é R$',total_salario)
  