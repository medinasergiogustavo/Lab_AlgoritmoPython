"""
print("Exemplo de uma lista numerica")
for contador in [0,1,2,3,4,5,6,7]:  # range(0,8)
     print("Valor do contador = " +str(contador))
print("Valor da variavel contador (final) = ",contador)
print(type(contador))
"""


print("================================")
print("Exemplo de uma lista de palavras")
entrada ="UNIP"
for letras in entrada:
       print("ciclo: "+ letras)
print(type(letras))
print("Tamanho da variavel entrada = ", len(entrada))

num= 4
fatorial =  (num-1)*(num-2)*(num-3) # fatorial de 4 = 4*3*2*1 
print("Fatorial de 4 = ", fatorial)