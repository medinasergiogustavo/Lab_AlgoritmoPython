"""
Trechos de programa que recebem um determinado nome e podem ser chamados várias vezes durante a execução
Principais vantagens: 
a)	reutilização de código, 
b)	modularidade e
c)	facilidade de manutenção do sistema
"""

print("Funções internas - builtin ou embutidas")

maior_numero = max(3 * 11, 5**3, 512 - 9, 1024**0)
menor_numero = min(3, 6, 7, 10)
maior_letra = max('a', 'b', 'c')
menor_letra = min('a', 'b', 'c')

print("O Nro maximo da lista =", maior_numero)
print("O Nro minimo da lista =", menor_numero)
print("A maior letra da lista =", maior_letra)
print("A menor letra da lista =", menor_letra)

nome = input("Digite o seu nome ") #aNA
nome.lower()	 #ana
nome.upper()     #ANA
nome.capitalize()   #Ana

print(type(nome))
print("A variavel nome tem "+str(len(nome)) +" letras")

print("Nome em Upper case = " + nome.upper())
print("Nome em Lower case = " + nome.lower())
print("1ra letra com Maiscula = " + nome.capitalize())





