import math
num = int(input('Digite um valor: '))
if ((num == 1) or (num == 2)):
    print (num**3)
elif (num%3 == 0):
    print (math.factorial(num))
elif ((num == 4) or (num == 5) or (num ==7) or (num == 8)):
    print (num/9.0)
else:
    print ('Valor inválido')
