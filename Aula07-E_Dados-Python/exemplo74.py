"""
dicionario = {'1ra_chave':'1ro_valor’, '2a_chave':’2do_valor}
Chave = Numero em ingles
Valor = Numero em español 
"""

english2spanish = { }
english2spanish['one'] = 'uno'
english2spanish['two'] = 'dos'
english2spanish['three'] = 'tres'
english2spanish['four'] = 'cuatro'

print("Conteudo do dicionario Ingles para Espanhol = ", english2spanish)

english2spanish2 = {
                    'one': 'uno',
                    'two': 'dos',
                    'three': 'tres',
                    'four': 'cuatro',
                    'five': 'cinco',
                    'six': 'seis'
                    }

for par_chave_valor in english2spanish2:
    print("Listagem das chaves do dicionario Ingles para Espanhol 2 = ", par_chave_valor)

print()
for chave in english2spanish2.keys():
    print("Listagem das chaves do dicionario Ingles para Espanhol 2 = ", chave)
print()

for palavra in english2spanish2.values():
    print("Listagem dos valores do dicionario Ingles para Espanhol 2 = ", palavra)

print()
#print("Conteudo do dicionario Ingles para Espanhol 2 = ",english2spanish)

valor = english2spanish['two']
print("Conteudo da chave two  = ", valor)

