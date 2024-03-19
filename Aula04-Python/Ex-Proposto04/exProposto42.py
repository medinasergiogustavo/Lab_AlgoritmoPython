p1 = 7.5
p2 = 3.6
tp = 2.0
falta = 5

if (falta > 15):
  print(" Infelizmente vc está reprovado por falta")
elif ((p1 <= 0.0) or (p1 > 10.0) or(p2 <= 0.0) or (p2 >= 10.0)):
    print("Nota invalida!")
    print("Favor digitar valores entre 0 e 10")
else:
    media = (p1 + p2 + tp)/3
    
    if(media >= 7):
        print("Parabens, vc está aprovado")
        print("Sua media foi %.1f" %media)
    else:
         print("Infelizmente, vc está de exame. È hora de estudar")
         print("Sua media foi %.1f" %media)

print("fim do programa")