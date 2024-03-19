# Iteração
"""
lista_num = [100, 200, 300, 400, 500]

for item in lista_num: # iteração com for
    print("Elementos da lista, lista_num", item)
"""
num = 5
lista_num = [500, 200, 300, 400, 100]
lista_nomes= ["Wladimir", "Carlos", "Andre", "Ana", "Anastacia"]

print("Tamanho da Lista inicial,  lista_num = ", len(lista_num))
print("Elementos da lista original lista_num = ", lista_num)

print ("Lista em ordem crescente da lista_num= ", sorted(lista_num))
print ("Lista em ordem alfabetica = ", sorted(lista_nomes))

for indice, elemento in enumerate(lista_num): #obter simultaneamente os índices e valores dos itens quando necessário.
    lista_num[indice] +=1000  # lista_num[indice] = lista_num[indice] +1000
    print("Posição ", indice+1, "Elemento da lista : ", lista_num[indice] )

print("Tamanho da Lista final,  lista_num = ",lista_num)
print("Tamanho da Lista final, lista_num = ", len(lista_num))

print("1ro elemento da = ",lista_num[0]) 
print("2ro elemento da = ",lista_num[1]) 
print("3ro elemento da = ",lista_num[2]) 

lista_num = [100, 200, 300, 400, 500]

for elemento in reversed(lista_num):
    print(elemento)

print("Lista reversa = ", lista_num)




