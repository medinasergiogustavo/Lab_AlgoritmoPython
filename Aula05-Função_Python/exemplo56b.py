import math

def retangulo(lado_a, lado_b):
    """Calcula a área de um retângulo"""
    area = lado_a * lado_b
    return area
    print("fim da função retangulo")

def triangulo(_base, _altura):
    """Calcula a área de um triângulo"""
    area = (_base * _altura) / 2
    return area

def circulo(_raio):
    """Calcula a área de um círculo"""
    area = math.pi * (math.pow(_raio, 2))
    return area

raio = int(input("Digite o raio do circulo = "))
lado_a = int(input("Digite o lado a = "))
lado_b = int(input("Digite o lado b = "))

base = int(input("Digite a base do triangulo = "))
altura = int(input("Digite a altura do triangulo = "))

print("Area do circulo = ", circulo(raio))
print("Area do retangulo = ", retangulo(lado_a, lado_b))
print("Area do trinagulo = ", triangulo(base, altura))



