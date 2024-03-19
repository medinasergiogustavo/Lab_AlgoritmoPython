
#Nome: Celso Zanquetta Junior
#ra: D76JCG-4
#Turma: CC5A41

numeros = [100, 20, 30, 90, 50, 60, 70, 80, 40, 100, 10]

def rodar(letra):
    if letra == 'a':
        listacompras()
    elif letra == 'b':
        tamanho()
    elif letra == 'c':
        ordenada()
    elif letra == 'd':
        Repetidos()
        
def listacompras():
    saveFile = open('listacompras.txt', 'w')
    for x in numeros:
        saveFile.write(str(x) + '\n')
        print(str(x))
        
def tamanho():
    saveFile = open('tamanho listacompras.txt', 'w')
    saveFile.write('Tamanho ' + str(len(numeros)))
    print('Tamanho ' + str(len(numeros)))
    
def ordenada():
    numeros.sort()
    saveFile = open('listacompras ordenada.txt', 'w')
    for x in numeros:
        saveFile.write(str(x) + '\n')
        print(str(x))
        
def Repetidos():
    numeros.sort()
    saveFile = open('listacompras ordenada.txt', 'w')
    for index, x in enumerate(numeros):
        if index == len(numeros)-1:
            break
        elif x == numeros[index+1]:
            saveFile.write('o numero ' + str(x) + ' se repete em ' + str(index) + ' e em ' + str(index+1))
            print('o numero ' + str(x) + ' se repete em ' + str(index) + ' e em ' + str(index+1))
            
escolha = input(' a: lista de compras \n b: imprimir o tamanho da lista \n c: organizar em ordem crescente \n d: listar repetidos\n selecione: ')

rodar(escolha)

    