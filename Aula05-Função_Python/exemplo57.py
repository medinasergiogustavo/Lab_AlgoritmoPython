print("Exemplo de variavel local e global com funções")
num = 10 # variável global
def func():
    num = 1 # variável local na função
    print("Resultado da variavel local num = ", num)

func() # chama a função
print("Resultado da variavel global num = ", num)

print("Obs: Não é recomendavel utilizar o mesmo nome para as variavel local e global")
# Rsumindo
# Função (Variavel local) --> num = 1
# Aplicação (Variavel global) --> num = 10

def quadrado(x):
    y = x * x
    return y

aQuadrar = 10
resultado = quadrado(aQuadrar)
print("Resultado do quadrado da  10 = ", resultado)


def calcula_energia_potencial_gravitacional(m, h, g = 10):
    """
    Calcula a energia potencial gravitacional
    Argumentos:
    m: massa, entrada como uma variável float
     h: altura, entrada como uma variável float

    Argumento opcional:
    g: aceleração gravitacional, com valor default de 10
    """
    e = g * m * h
    return e

r1 = calcula_energia_potencial_gravitacional(30, 12)
print("Resultado da EPG = ", r1)
print("")
r2= calcula_energia_potencial_gravitacional(30, 12, 9.8)
print("Resultado da EPG = ", r2)