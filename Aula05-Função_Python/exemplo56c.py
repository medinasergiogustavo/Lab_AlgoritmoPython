"""
def calcular_pagamento(_horas, _taxa):
  horas = float(_horas) # horas é uma variavel local
  taxa = float(_taxa) # taxa é uma variavel local
  print(horas)
  if horas <= 40:
    salario = horas*taxa
  else:
    h_excd = _horas - 40
    salario = 40*taxa+(h_excd*(1.5*taxa))
  return salario


def entrada_dados( ):
  horas = float(input("Digite as horas: "))
  taxa = float(input("Digite a taxa: "))
  return (horas, taxa)

# h,t = 35,20
h,t = entrada_dados( )
total_salario = calcular_pagamento(h, t)
print('O valor de seus rendimentos é R$',total_salario)
print("Fim do 1ro Programa")
"""

def entrada():
  peso_dig = float(input("Digite o peso = "))
  altura_dig = float(input("Digite a altura = "))
  return (peso_dig, altura_dig)

def calculo_imc(peso, altura):
  print(peso / (altura ** 2))
  imc = peso / (altura ** 2)
  return (imc)

p,a = entrada()
print("Calculo do IMC =", calculo_imc(p, a))
