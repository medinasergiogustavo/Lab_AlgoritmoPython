print("Programa que determina se o numero digitdo é a) par ou impar, b) positivo ou negativo ou c)  inteiro ou decimal")

print("1 - Par ou Impar")
print("2 - Positivo ou Negativo")
print("3 - Inteiro ou Decimal")
opcao = input('Escolha uma opcao: ') # Escopo global

##valor = float(input('Informe um numero: '))

def entrada():   # def = defition = definição
    valorFloat = float(input("Informe um numero = ")) # 8
    print(valorFloat)
    return valorFloat # 9.0

#print(valorFloat)

if (opcao == '1'):
    #valor = float(input('Informe um numero: '))
    valor = entrada() # 9.0
    if (valor % 2 == 0):  # valor/2, valor//2
        print("Valor é par")
    else:
        print("Valor é impar")
elif (opcao == '2'):
    valor = float(input('Informe um numero: '))
    if (valor < 0):
        print('Valor eh negativo')
    elif (valor > 0):
        print('Valor eh positivo')
    else:
        print('Valor eh igual a zero')
elif (opcao == '3'):
    valor = float(input('Informe um numero: '))
    if (valor == int(valor)):
        print('Valor eh inteiro')
    else:
        print( 'Valor eh decimal')
else:
    print('Opcao Invalida')

print(" A opção digitada foi = " +opcao)
print("Fim do programa")