lista_numeros = [70, 10, 40, 30, 20, 80, 50, 90]
print("Lista original lista_numeros = ", lista_numeros)
print("Novo tamanho da lista de caracteres =", len(lista_numeros))

lista2 = 4 * [0]
print("Lista 2 = ", lista2)

print("Inclui um elemento no final da lista de numeros")
lista_numeros.append(100)
print("Nova lista de numeros =", lista_numeros)
print()
print("Novo tamanho da lista de caracteres =", len(lista_numeros))

lista2.insert(2,880)
print("Nova lista de caracteres =", lista2)
print("Novo tamanho da lista de caracteres =", len(lista2))
lista2.insert(1,555)
print("Nova lista de caracteres =", lista2)
print("Novo tamanho da lista de caracteres =", len(lista2))

lista_numeros.remove(90)
print("Nova lista de caracteres =", lista_numeros)
lista_numeros.append(100)
lista_numeros.append(100)
print("Retorna o numero de ocorrencia do elemento 100 =" ,lista_numeros.count(100))
print("Retorna a posição do elemento 880 = ", lista2.index(880))

print("Elementos da lista2 = ", lista2)
print("tamanho da lista 2 = ", len(lista2))

lista2.clear()
print("Elementos da lista2 = ", lista2)

print("Retorna a lista original dos numeros = ", lista_numeros)
print("Lista em ordem crescente", sorted(lista_numeros))
lista_numeros.reverse()
print("Retorna a lista invertida = ", lista_numeros)
print("Lista em ordem crescente", sorted(lista_numeros))



