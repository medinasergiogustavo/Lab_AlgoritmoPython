lista_caracteres = ["a", "b", "c", "d", "e", "f", "g"]
lista_numeros = [700, 100, 400, 300, 700, 600, 800, 500]
lista5 = [9, 4, 8 , 7, 3]

print("Elementos da lista de caracteres =", lista_caracteres)
print("Tamanho da lista de caracteres =", len(lista_caracteres))
print("Incluir um elemento no final da lista de caracteres ")
lista_caracteres.append("t")
print("Nova lista de caracteres =", lista_caracteres)
print()
print("Elementos da lista de caracteres =", lista_numeros)
print("Novo tamanho da lista de caracteres =", len(lista_numeros))
print("Incluir um elemento no final da lista de numeros")
lista_numeros.append(6500)
print("Nova lista de caracteres =", lista_numeros)
print("Novo tamanho da lista de caracteres =", len(lista_numeros))
print()

lista_numeros.insert(2,8000)
print("Nova lista de caracteres =", lista_numeros)
print("Novo tamanho da lista de caracteres =", len(lista_numeros))

lista_numeros.remove(400)
print("Nova lista de caracteres =", lista_numeros)

print(" Retorna o numero de ocorrencia do elemento 100 =" ,lista_numeros.count(100))
print("Retorna a posição do elemento 700 = ", lista_numeros.index(700))

print("Elementos da lista5 = ", lista5)
print("tamanho da lista 5 = ", len(lista5))
lista5.clear()
print("Elementos da lista5_vazia = ", lista5)

lista_numeros.reverse()
print("Retorna a lista invertida = ", lista_numeros)
print("Lista em ordem crescente", sorted(lista_numeros))

print("listagem dos elementos da lista numeros", lista_numeros)
lista_numeros.pop()
print("Nova lista com a eleminação do ultimo elemento", lista_numeros)

print("Numero minimo da Lista = ", min(lista_caracteres))
print("Numero maximo da Lista = ", max(lista_caracteres))

print("Numero minimo da Lista = ", min(lista_numeros)) 
print("Numero maximo da Lista = ", max(lista_numeros)) 
print("Soma de todos os elementos da Lista = ",sum(lista_numeros))
