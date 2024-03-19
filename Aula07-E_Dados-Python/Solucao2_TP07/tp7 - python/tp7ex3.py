from operator import itemgetter
pessoas = []
sex_pessoas = []
age_pessoas = []
x = ''

def writepeople():
    global pessoas
    print('escreva 10 nomes com sexo e idade separo por ","(virgular)\n')
    for index in range(0,10,1):
        dados = input()
        pessoas.append(dados.split(','))
    print(pessoas)

def ascending_order_sex():
    global sex_pessoas
    sex_pessoas = sorted(pessoas[0:], key=itemgetter(1))
    print(sex_pessoas)


def ascending_order_age():
    global age_pessoas
    age_pessoas = sorted(pessoas[0:], key=itemgetter(2))
    print(age_pessoas)

def ascending_order_name():
    global pessoas
    pessoas.sort()
    print(pessoas)

def save():
    global pessoas
    arquivo = open('ListaCLiente.txt', 'w', encoding='utf-8')
    amount = 0
    for nome in pessoas:
        print(nome)
        arquivo.write(nome[0]+', '+str(nome[1])+', '+(nome[2])+'\n' if amount < len(pessoas)-1 else '')
        amount += 1
    arquivo.close()
    print('arquivo salvo')

while( x != 'd'):
    x = input('aperte "a" para adicionar pessoas "b" para ordenar por sexo "c" para ordernar por idade "d" para ordenar por nome\n')
    if x == 'a':
        writepeople()
    elif x == 'b':
        ascending_order_sex()
    elif x == 'c':
        ascending_order_age()
    elif x == 'd':
        ascending_order_name()
        save()
        print('saindo')
    else:
        print("nao existe essa opção no menu")
