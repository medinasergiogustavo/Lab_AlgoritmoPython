
#Nome: Celso Zanquetta Junior
#ra: D76JCG-4
#Turma: CC5A41

itens_compra = []

def rodar(letra):
    if letra == 'a':
        criarlista()
    elif letra == 'b':
        listacompras()
    elif letra == 'c':
        inserir()
    elif letra == 'd':
        remover()
        
def criarlista():
    global itens_compra
    itens_compra = ['Arroz', 'Leite', 'Ovos', 'Feijão', 'Tomate', 'Kimojo' ]
        
def listacompras():
    saveFile = open('listacomprasfix72.txt', 'w')
    for x in itens_compra:
        saveFile.write(x + '\n')
        print(x)
        
def inserir():
    itens_compra.append('oleo canola')
    
def remover():
    itens_compra.remove('Tomate')
    saveFile = open('listacompras ordenada.txt', 'w')
    for x in itens_compra:
        saveFile.write(x + '\n')
        print(x)
        
for retry in range(6):            
    escolha = input(' a: inserir valores na lista \n b: imprimir a lista \n c: inserir oleo canola na lista \n d: remover tomate\n selecione: ')

    rodar(escolha)

    