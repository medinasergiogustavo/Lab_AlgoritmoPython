"""
Tuplas são sequências similares a listas, com a principal diferença
que seus itens não podem ser alterados individualmente. Por isso, 
dizemos que são sequências imutáveis.
"""

dupla = ( " abc " , 3) 
print("Conteudo da dupla = ", dupla)
print("Conteudo da tupla dupla = ", dupla)

tripla = ( 1 , True , " 1 " )
print("Conteudo da tripla = ", tripla)
print("Tipo de Estrutura de dados dupla= ",type(dupla))

print("O Elemento 3 pertence a tupla (dupla) = ", 3 in dupla)
print("O Elemento 8 NÃO pertence a tupla (tripla) = ", 8 not in tripla)

tupla1 = ("Maça","Laranja", "Banana","Mamão", "Tangerina", "Melão")

for elemento in tupla1:
    print("Fruta = ", elemento)

print("Determina a posição do elemento mamão do tupla1  ", tupla1.index('Mamão'))

aluno = ("Ricardo",7.2, 7.8)

print("Conteudo da tupla Aluno = ", aluno)
print("Tipo de Estrutura de dados de Aluno= ",type(aluno))

tupla2 = range(1,6)
if (6 in tupla2):
    print("Valor contido da tupla")
else:
    print("Valor Não contido da tupla")

#tupla2 = range(1,6)
if (6 not in tupla2):
    print("Valor não contido da tupla")
else:
    print("Valor contido da tupla")






