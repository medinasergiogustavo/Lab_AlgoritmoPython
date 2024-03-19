num = 5
lista01 = [10, 20, 30, 40, 50]
lista02 = [60, 70, 80, 90, 100, 110, 120]

print("Elementos da lista 01 = ", lista01)
print(type(lista01))
print("Tamanho da lista 01 = ", len(lista01))
print()
print("Elementos da lista 02 = ", lista02)
print(type(lista02))
print("Tamanho da lista 02 = ", len(lista02))

print("Elemento da 1ra posição =", lista01[0])
print("Elemento da 5ta posição =", lista01[4])
print("Soma em uma lista ", (lista01[0] + lista01[4]))

lista_caracteres = ["a", "b", "c", "d", "e","f", "g"]

print("Conteudo da lista de caracteres =", lista_caracteres)
print("Elemento da 1ra posição =", lista_caracteres[0])
print("Elemento da 2da posição =", lista_caracteres[1])
print("Elemento da 3ra posição =", lista_caracteres[3])
print("Elemento da 6ta posição =", lista_caracteres[5])

lista03 = lista01 + lista02 # concatenando 2 listas
print("Soma dos elementos de 2 listas (lista01 + lista02) = ", lista03 )
print("Tamanho da lista 03 = ", len(lista03))

lista04 = lista01 *2
print("Multiplicano os elementos da lista01 = ", lista04 )

lista05= list("Python")
print ("Elemento da lista 5 =",lista05)

lista06= list(("Python 3.7",))
print ("Elemento da lista 3 =",lista06)

del lista04   # Exclui a lista04
print("Lista 04 = ", lista04)



