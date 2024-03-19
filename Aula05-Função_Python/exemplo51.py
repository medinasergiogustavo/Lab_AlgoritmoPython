print("Programa que converte dias das semana numerico em texto")
#numero_dia =0
numero_dia = int(input("Informe um numero para saber o dia da semana (1, 2, 3, 4, 5, 6, 7): "))
texto ="Um bom dia para aprender Python"

print("A variavel numero_dia é do tipo = ",type(numero_dia))

if (numero_dia == 1):
    print("Domingo. " + texto)
elif (numero_dia == 2):
    print ("Segunda feira. " + texto)
elif (numero_dia == 3):
    print ("Terca feira. "+ texto)
elif (numero_dia == 4):
    print ("Quarta feira. "+ texto)
elif (numero_dia == 5):
    print ("Quinta feira. " + texto)
elif (numero_dia == 6):
    print ("Sexta feira. " + texto)
elif (numero_dia == 7):
    print ("Sabado. " + texto)
else:
    print ("Valor invalido. Favor digitar numeros entre o intervalo (1, 2, 3, 4, 5, 6, 7)")

print("Fim do programa")
