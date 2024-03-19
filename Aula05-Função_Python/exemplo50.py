print("Favor digitar uma vogal (a, e, i, o, u)") 
vogal = input("Digite uma vogal: ") # t

print("Tipo da variavel digitada vogal =", type(vogal))

if (vogal == 'a'):
	print('você digitou a vogal = "a"')

elif (vogal == 'e'):
	print('você digitou a vogal = "e"')

elif (vogal == 'i'):
	print('você digitou a vogal = "i"')

elif (vogal == 'o'):
	print('você digitou a vogal = "o"')

elif (vogal == 'u'):
	print('você digitou a vogal = "u"')

else:
	print('Não é uma vogal. Por favor recomeçe e digite uma vogal')


print("O conteudo da variavel vogal é = " +vogal)
print("Fim do programa")


