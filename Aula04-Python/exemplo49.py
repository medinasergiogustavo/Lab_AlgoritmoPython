conta = 0
while(conta <= 10):
    conta += 1
    print(conta)
else:
    print("Valor da variável conta é: ", conta)

print("=========================")
x = 0
print("Estrutura de repetição while")
while(x<10):
    print(x)
    x=x+1;
    if (x == 6):
       break
else:
    print("else")
print("fim")


condicao = True
while(condicao):
    print("BLOCO while() e condicao==True")
    condicao = False
    break
else:
    print("BLOCO ELSE e condicao==False")


    
print("Tabuada do 4 utilizando o loop tipo while")
contador =0
while (contador<=10):
    tabuada = contador * 4
    print("4 x " +str(contador) + " = "+str(tabuada))
    contador= contador+1
print("Fim do loop")