print("Mostrar na tela os numero 1 a 5")
print(1)
print(2)
print(3)
print(4)
print(5)
print("")


# contador1 <= 5 ( vi= 1 e vf = 5)
"""
print("1ra estrutura for")
print()
lista_numeros = [1,2,3,4,5,6,7]
for contador1 in lista_numeros: #Contador crescente vi < vf
    print(" %i Posição, valor = %i" %(contador1, contador1))
print("Fim do 1ro for")
print("tamanho da variavel lista numeros = ", len(lista_numeros))
"""

"""
print("2da estrutura for (Contador crescente)")

for contador1 in range(0, 11, 1): #Contador crescente vi(0) < vf(11)
    print(" %i Posição " %contador1)
   # print(" Valor da Posição "+ str(contador1))
   # print(" Valor da Posição ", contador1)
print("Fim do 2do for")
"""

"""
print("3ra estrutura for(Contador crescente)")
for contador2 in range(5, 0, -1): #Contador decrescente vi(5) > vf(0)
    print(" %i Posição " %contador2)
print("")
"""
soma = 0
for numero in range(1, 6): #contador crescente vi(1) < vf(6)
  soma = soma + numero
  print("Resultado da soma parcial (dentro do loop for) = ",soma)
print("Resultado da soma total =", soma)
print("")
"""

"""
palavra = "Terere com gelo"
for letra in palavra:
  print(letra)
  if (letra == "g"):
    print("Achou a letra g")
    break
print("Fim do loop for")

print("tamanho da variavel palavra = ", len(palavra))



