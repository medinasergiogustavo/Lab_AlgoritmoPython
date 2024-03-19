
#Nome: Celso Zanquetta Junior
#ra: D76JCG-4
#Turma: CC5A41

from operator import itemgetter

clientes = []

def rodar(letra):
    if letra == 'a':
        criarlista()
    elif letra == 'b':
        listarclientes()
    elif letra == 'c':
        idade()
    elif letra == 'd':
        nomealfabetica()
        
def criarlista():
    global clientes
    i = 0
    while i < 10:
        nome = input('Digite o nome do cliente: ').upper()
        sexo = input('Digite o sexo do cliente F para Feminino M para Masculino: ').upper()
        idade = int(input('Digite a idade do cliente: '))
        clientes.append([nome,sexo,idade])
        i+=1
        
def listarclientes():
    a = sorted(clientes, key = itemgetter(1))
    saveFile = open('listar clientes em ordem de sexo.txt', 'w')
    for x in a:
        for z in x:
            saveFile.write(str(z) + '\t')
        saveFile.write('\n')
    saveFile.close()
            
        
def idade():
    a = sorted(clientes, key = itemgetter(1,2), reverse=True)
    saveFile = open('listar clientes em ordem de idade e sexo.txt', 'w')
    for x in a:
        for z in x:
            saveFile.write(str(z) + '\t')
        saveFile.write('\n')
    saveFile.close()
    
def nomealfabetica():
    a = sorted(clientes, key = itemgetter(0))
    saveFile = open('listar clientes nome em ordem alfabetica.txt', 'w')
    for x in a:
        for z in x:
            saveFile.write(str(z) + '\t')
        saveFile.write('\n')
    saveFile.close()
        
for retry in range(6):            
    escolha = input(' a: inserir valores na lista \n b: classificar por genero \n c: ordenar por idade e genero \n d: odernar alfabetica\n selecione: ')

    rodar(escolha)

    