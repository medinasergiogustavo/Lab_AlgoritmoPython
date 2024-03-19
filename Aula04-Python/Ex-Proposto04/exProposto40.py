"""

#Ler 5 notas e informar a média com a estrutura For

nota = media = soma = 0.0
print("Valor inicial da nota = " +str(nota) )
print("Valor inical da media = " +str(media))
print("Valor inical da soma = " +str(soma))

for cont in range(1, 6):
  nota = float(input('Digite a nota '))
  soma = soma + nota
print(soma)

media = soma / 5
print('A média é ', media)

"""
#Ler 5 notas e informar a média com a estrutura While

nota = soma = 0
contador = 1

nota = media = soma = 0.0
print("Valor inicial da nota = " +str(nota) )
print("Valor inical da media = " +str(media))
print("Valor inical da soma = " +str(soma))

while contador <= 5:
  nota = float(input("Digite a nota ="))
  soma += nota
  contador += 1
print("A média é ", soma / 5)