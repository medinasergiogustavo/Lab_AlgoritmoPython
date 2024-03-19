print("Programa que determina o turno que o aluno estuda")

print( 'Informe o turno em que voce estuda')
print( '[M]atutino')
print( '[V]espertino')
print( '[N]oturno')

turno = input('Opcao escolhida: ').upper() # n

if (turno == 'M'):
    print ('Bom dia!')
elif (turno == 'V'):
    print('Boa tarde!')
elif (turno == 'N'):
    print( 'Boa noite!')
else:
    print('Valor invalido. Favor digitar M, V ou N')

print("Fim do programa")
