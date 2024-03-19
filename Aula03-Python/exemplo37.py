idade = int(input("Informe a sua idade: "))

if(idade <= 0):
    print("A sua idade %i não pode ser 0 ou menor do que 0!" %idade)
elif((idade >= 0) and (idade<16)) :
        print("Você precisa ter mais do que 16 anos! idade = %i" %idade)   
elif ((idade>=16) and (idade<70)):
    print("Parabens, vc pode votar! idade = %i"  %idade)
elif (idade>=70): 
    print("Parabens, vc pode votar! idade = %i"  %idade)




