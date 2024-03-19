"""
dicionario = {'1ra_chave':'1ro_valor’, '2a_chave':’2do_valor}
Chave = sinonimo
Valor = antonmo
""" 
antonimo= {'up': 'down', 'right': 'wrong', 'true': 'false'}
#alias = antonimo
alias = antonimo

print("Conteudo do dicionario antonimo = ",antonimo)
print("Uso do alias ", alias is antonimo)
 
alias['right'] = 'left'
print("Correção do valor de right =" , antonimo['right'])
print()
print("Conteudo do dicionario antonimo = ",antonimo)
print()
copiaAntonimo = antonimo.copy()
print("Conteudo do dicionario Copia Antonimo = ",copiaAntonimo)


