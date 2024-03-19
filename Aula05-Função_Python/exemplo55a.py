import math
 
print(math.ceil(1.001) )   # returns 2
print(math.floor(1.801))  # returns 1
print(math.factorial(10))  # returns 3628800
print(math.gcd(10,125) )   # returns 5
 
print(math.trunc(1.001))   # returns 1
print(math.trunc(1.999))   # returns 1

print(math.pow(12.5, 2.8)  )            
print("Resultado da potencia com expoente 1/2 = " + str(math.pow(144, 1/2) ))  # 144 ** 1/2
print("Resultado da potencia com expoente 0.5 =" +str(math.pow(144, 0.5) ) )            
print(("Resultado da raiz quadrada de 144 =" +str(math.sqrt(144)) ) )                 


print(dir(math))