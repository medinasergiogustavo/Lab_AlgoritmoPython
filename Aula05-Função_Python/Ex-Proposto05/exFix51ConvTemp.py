"""
Elaborar um programa em Python que receba um valor (via teclado) que 
representa a temperatura em Graus celcius.
E mostre o resutado em graus Fahrenheit
"""

print("Inicio do progrma")
def ler_temperatura():
    temperatura = float(input('Digite a temperatura em graus Celsius: '))
    print(temperatura)
    return (temperatura)

def converter(temperatura_celsius):
    temperatura_f = (9 * temperatura_celsius + 160) / 5
    return (temperatura_f)

def mostrar(temperatura_f):
    print("Temperatura em Fahrenheit = ", temperatura_f)

#temperatura_c = float(input("Digite a temperatura"))

temperatura_c = ler_temperatura()
temperatura_f = converter(temperatura_c)

mostrar(temperatura_f)
