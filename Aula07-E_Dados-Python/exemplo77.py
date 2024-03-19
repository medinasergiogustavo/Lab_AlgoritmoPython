"""
dicionario = {'1ra_chave':'1ro_valor’, '2a_chave':’2do_valor}
Chave = Frutas
Valor = Quantidade 
"""
estoqueFrutas1 = {
                'kiwis': 430, 
                'bananas': 312, 
                'laranjas': 525, 
                'peras': 217
                 }

estoqueFrutas2 = {
                'mangas': 130, 
                'abacaxis': 150, 
                'uvas': 325, 
                'ameixas': 517
                }

print("Conteúdo completo do dicionário (estoque 1) = " , estoqueFrutas1)

print("Conteúdo completo do dicionário (estoque 2) = " , estoqueFrutas2)

del estoqueFrutas1['peras']

print("Conteúdo do dicionário (estoque 1), após a exclusão do chave/valor = pera " , estoqueFrutas1)

estoqueFrutas1['bananas'] = estoqueFrutas1['bananas'] + 200

numItens = len(estoqueFrutas1)
print("Numero de itens = " , numItens)
print("Estoque de bananas = ", estoqueFrutas1['bananas'])

print("Estoque total de frutas = ", estoqueFrutas1)

print ("Tem peras no estoque de Frutas 1?")
print ("peras" in estoqueFrutas1)
print()
print ("Tem mangas no estoque de Frutas 1?")
print ("mangas" not in estoqueFrutas1)
print()

for frutas in estoqueFrutas1.keys():
    print("Listagem das frutas no estoque 1 = ", frutas) 
print()  
print(" Lista de frutas: ", list(estoqueFrutas1.keys()))

print()   
for quantidade in estoqueFrutas1.values():
    print("Listagem das quantidades de frutas no estoque 1 = ", quantidade) 
print()   
print(" Lista de quantidade: ", list(estoqueFrutas1.values()))
print()
for i in estoqueFrutas1:
    print("Listagem key e valor")
    print(i, estoqueFrutas1.items())
print()
print("Calculo da Soma (total) de frutas no estoque de frutas1 + estoque de frutas2")
estoqueFrutas1.update(estoqueFrutas2)
print("Total de frutas no estoque 1 ",estoqueFrutas1)



