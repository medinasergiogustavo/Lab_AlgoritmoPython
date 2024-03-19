"""
dicionario = {'1ra_chave':'1ro_valor’, '2a_chave':’2do_valor}
Chave = Estado
Valor = Capital 
"""

dicEstadoCapital1 = {
                   "Rio de Janeiro": "Rio de Janeiro",
                   "São Paulo": "São Paulo",
                   "Minas Gerais": "Belo Horizonte",
                   "Bahia": "Salvador",
                   "Amazonas": "Manaus"
                   }

dicEstadoCapital2= {
                   "Parana": "Curitiba",
                   "Rio Grande do Sul": "Porto Alegre",
                   "Santa Catarina": "Florianopolis",
                   }

print("Dicionario completo do dicEstadoCapital1 ", dicEstadoCapital1.items())   
print()
print("Relatorio completo dos Estados com as Capitais (dicEstadoCapital1 )")
print(dicEstadoCapital1)
print()
print(" A capital de Rio de Janeiro é ", dicEstadoCapital1["Rio de Janeiro"])
print()
print("Relatorio completo dos Estados com as Capitais (dicEstadoCapital2 )")
print(dicEstadoCapital2)
print()
dicEstadoCapital1.update(dicEstadoCapital2)

print(dicEstadoCapital1)

for chave in dicEstadoCapital1: # Chave = Estado
    print("Listagem das chaves do dicEstadoCapital1,  Estado = ", chave)

print()
for valor in dicEstadoCapital1.values(): # Valor = Capital 
    print("Listagem dos valores do dicEstadoCapital1, Capital = ", valor) 

print(" Lista de estados: ", list(dicEstadoCapital1.keys()))
print()    
print(" Lista de capitais: ", list(dicEstadoCapital1.values()))

print()
for estado, capital in dicEstadoCapital1.items():
    print(f"Estado: {estado}, Capital: {capital}")