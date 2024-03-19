itens_compra = ["Arroz", "Leite", "Ovos", "Feijão", "Tomate", "Kimojo"]
x = ''

def add_in_list():
    global itens_compra
    itens_compra.append("óleo de canola")
    print('adicionado "óleo de canola"')

def remove_item():
    global itens_compra
    itens_compra.pop(4)
    print('tomate removido')

def save():
    arquivo = open('listacompras2.txt', 'w', encoding='utf-8')
    amount = 0
    for nome in itens_compra:
        arquivo.write(str(nome) + '\n' if amount < len(itens_compra) else '')
        amount += 1
    arquivo.close()
    print('arquivo salvo')


while( x != 'd'):
    x = input('aperte "a" para mostrar os itens "b" para Acrescente “óleo de canola” "c" para remover “tomate”  "d" para gravar e sair\n')
    if x == 'a':
        print(itens_compra)
    elif x == 'b':
        add_in_list()
    elif x == 'c':
        remove_item()
    elif x == 'd':
        save()
        print('saindo')
    else:
        print("nao existe essa opção no menu")
