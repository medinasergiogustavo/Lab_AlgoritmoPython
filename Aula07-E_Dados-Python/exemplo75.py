"""
dicionario = {'1ra_chave':'1ro_valor’, '2a_chave':’2do_valor}
Chave = Nome
Valor = Telefone 
"""

retornar_ligacao = {
    		       "Andre": "(11) 3030-1122",
   		           "Carlos": "(11) 33547877",
                   "Ana": "(11) 3338-1245",
                   "Timoteo": "(11) 3645-8899"
                    }

print("Ligações pendentes", retornar_ligacao)

for nome in retornar_ligacao:
    print("Listagem de nomes do dicionario retornar Ligação = ", nome)

print()
for telefone in retornar_ligacao.values():
    print("Listagem dos numeros do dicionario retornar Ligação = ", telefone)

print()
print("Ligações pendentes", retornar_ligacao) 

for pessoa in retornar_ligacao.keys():
    print("Listagem das pessoas (chaves)  do dic retornar_ligacao = ", pessoa)

print(" Lista das pessoas (chaves): ", list(retornar_ligacao.keys()))
print(" Lista : ", list(retornar_ligacao.keys()))
print()    

for telefone in retornar_ligacao.values():
    print("Listagem dos telefones (valores)  do dic retornar_ligacao =", telefone) 
print()
print(" Lista dos telefones: ", list(retornar_ligacao.values()))

retornar_ligacao.popitem() # Exclui o ultimo par (chave/valor) do dicionario ("Timoteo": 36458899)
print("Lista atualizada: Ligações pendentes", retornar_ligacao) 

retornar_ligacao.popitem() # Exclui o ultimo par (chave/valor) do dicionario ("Ana": 33381245)
print("Lista atualizada: Ligações pendentes", retornar_ligacao) 