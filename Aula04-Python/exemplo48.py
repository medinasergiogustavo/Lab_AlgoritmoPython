"""
cont = 0
while (cont <=5):
    print("Valor da variavel contador = " +str(cont))
    cont = cont + 1 # cont +=1
    #break
print("---")
"""
"""
numero = 5
while (numero > 0):
    print("Valor da variavel numero = " +str(numero))
    numero -= 1  # numero = numero -1
print("---")
"""

"""
soma = 0
numero = 1
while (numero < 6):
    print("Valor da variavel numero = " +str(numero))
    soma = soma + numero
    numero += 1 # numero = numero + 1
print("Resultado da soma =" + str(soma))


"""
numero = 0
numero = int(input("Digite um número de 1 a 10: ")) #50
while (numero >= 1) and (numero <= 10):
    print(" O numero digitado é = " + str(numero))
    escolha = input("deseja continuar (digite N ou n para Não e S ou s para Sim)?")
    if (escolha == "n") or (escolha == "N"):
        print("Vc escolheu sair do loop")
        break
    else:
        print("Vc escolheu continuar do loop")
        numero = int(input("Digite um número de 1 a 10: ")) #50
else:
    print(" O numero digitado está fora do intervalo valido (1 a 10)!")

print("Fim do programa")




"""
condicao = True
while(condicao):
    print("BLOCO while() e condicao == True")
    condicao = False
else:
    print("BLOCO ELSE e condicao == False")

print("Fim do bloco do while(True)")
"""