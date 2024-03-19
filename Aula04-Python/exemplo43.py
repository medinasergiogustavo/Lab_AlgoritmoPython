print("Exemplo de for com a clausula break e else")

lista_num = [0,1,2,3,4,5,6,7,8,9,10]

for cont in lista_num:  # vi=0 e vf=10, range (11) ou range(0,11,1)
    print("Valor do contador =", cont)
    #break
else:
    print("Saida do else, executou o bloco da instrução else")
    print("Ultimo valor do contador =", cont)

print("Estrutura for NÃO executou todos os ciclos definidos e no final, executou o bloco da instrução else")

