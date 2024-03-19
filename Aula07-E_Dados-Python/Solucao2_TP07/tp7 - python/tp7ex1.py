numeros = [100, 20, 30, 90, 50, 60, 70, 80, 40, 100, 10]
ordenados = []
x = '' 

def printNumbers():
    print(numeros)

def sizeNumbers():
    print(len(numeros))
    
def ascendingOrder():
    global ordenados
    ordenados = sorted(numeros)
    print(ordenados)

def equalNumbers():   
    for numero in range( 0, len(ordenados)-1, 1):
        if (numero < len(ordenados)) & (ordenados[numero] == ordenados[numero+1]):
            print('posição ',numero+1,' e igual a ',numero+2)

def save():
    arquivo = open('ListaCompras.txt', 'w', encoding='utf-8')
    global ordenados
    amount = 0
    for nome in ordenados:
        arquivo.write(str(nome) + '\n' if amount < len(ordenados) else '')
        amount += 1
    arquivo.close()

while( x != 'e'):
    x = input('aperte "a" para mostrar os numeros "b" para mostrar a quantidade "c" deixar em ordem crescente "d" para mostrar numeros repetidos "e" para gravar e sair\n')
    if x == 'a':
        printNumbers()
    elif x == 'b':
        sizeNumbers()
    elif x == 'c':
        ascendingOrder()
    elif x == 'd':
        equalNumbers()
    elif x == 'e':
        save()
        print('saindo')
    else:
        print("nao existe essa opção no menu")