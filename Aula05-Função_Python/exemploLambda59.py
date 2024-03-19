# Programa para converter temperatura de Fahrenheit para Celsius
print("Conversor de temperatura de Fahrenheit para Celsius ")
temp_celsius = lambda f: (5/9) * (f - 32)

f = float(input('Entre com a temperatura em Fahrenheit: '))
print('A temperatura em Celsius é: {0:.2f}'.format(temp_celsius(f)))
print()

# Programa que calcula a área de um retângulo e  triângulo

retangulo = lambda lado_a, lado_b: lado_a * lado_b
triangulo = lambda lado, altura: (lado * altura) / 2
circulo = lambda raio: 3.14 * (raio ** 2)

print("Digite os lados do retangulo")
lado1 = float(input("Digite o lado 1 = "))
lado2 = float(input("Digite o lado 2 = "))
print("Area do retangulo = ", retangulo(lado1, lado2))
print()

print("Digite os valores do triangulo")
base = float(input("Digite o valor da base = "))
altura = float(input("Digite o valor da altura = "))
print("Area do triangulo = ", triangulo(base, altura))


escrever_nome_idade = lambda nome, idade: print(nome, "possui",idade,"anos.")
nome_digitado = str(input("Digite seu nome: "))
idade_digitada = int(input("Digite sua idade: "))

escrever_nome_idade(nome_digitado, idade_digitada)


multiplicar = lambda numero1, numero2: numero1 * numero2

numero = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
resultado = multiplicar(numero, numero2)
print("Resultado da Multiplicação = ", resultado)

