#Listas de listas ou sub-listas
lista1 = [ [],[],[],[], [] ] # Definição de uma lista contendo 3 sublistas como elementos
lista2= [ 
        ["a","b","c","d"],
        [5.4,6.5,7.3],
        [3, 4, 6, 7, 5],
        [] 
        ]
#lista2= [ ["a","b","c","d"], [5.4,6.5,7.3], [3, 4, 6, 7, 5], []  ]

lista_mista = ["d", True, 1,2,3,4, "Testando o Python"]

print("1ra sublista contida na lista02 =", lista2[0])
print("3ra sublista contida na lista02 =",lista2[2])
print("4ra sublista contida na lista02 =",lista2[3])
print()
print(lista2[0][1])
print(lista2[1][2])
print()

print("Tamanho da lista 1 = ",len(lista1))
print("Tamanho da lista 2 = ",len(lista2))


print("Elementos da lista mista = ", lista_mista)
print("Tamanho da lista mista = ", len(lista_mista))


