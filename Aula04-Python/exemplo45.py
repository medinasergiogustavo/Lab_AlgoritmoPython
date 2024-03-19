#Implementação sem o uso da instrução ELSE
status = True
for cont in [0,1,2,3,4,5,6,7,8,9,10]: #range (11)
    print("valores do contador =",cont)
    if(not status): # True
        status = True
        break

if(status):
    print("Imprime o valor da variavel status", status)

print("Fim do programa")
