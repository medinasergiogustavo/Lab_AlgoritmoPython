import math
import random

raiz = math.sqrt(25)
raiz = math.sqrt(9)
print("Funções do modulo math")
print("Potencia da base 2 e elevado a 3 = ", math.pow(2, 3)) # 2**3
print("Potencia da base 7 e elevado a 7 = ",math.pow(7, 4))

print("Valor absoluto de 5 = ", abs(5))
print("Valor absoluto de -5 = ", abs(-5))

raiz = math.sqrt(81)
print("Valor da raiz de 9 %.2f = " %raiz)
print("Valor de Pi= ", math.pi)
PI = math.pi
PI_1 = 3.14
print("Valor de Pi = %.5f" %PI)
print("Valor de e =",math.e)

seno= math.sin(math.radians(90))
print("Valor do senho de 90 Graus =",seno) # seno de 90 graus

print("")
print("Funções do modulo random")
print("Valor da função random.randran(50) =", random.randrange(50))
print( "Varlor da função random.randran(0, 50, 1) =",random.randrange(0, 50, 1))

range(11)
range(0,11)
range(0,11,1)

prob = random.random()
print("Varlor da função random.random() =",prob)

lanceDado = random.randrange(1,7)  # retorna um int, dentre 1,2,3,4,5,6
print("Valor do dado =", lanceDado)
print("Valor do PI = ", PI)
print("Ultimo valor da raiz de  = ", raiz)

range(1,7)







