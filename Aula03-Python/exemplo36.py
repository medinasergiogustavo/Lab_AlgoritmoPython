"""
Leia a idade do usuário e classifique-o em:
Criança: 0 a 12 anos
Adolescente: 13 a 17 anos
Adulto: acima de 18 anos
Se o usuário digitar um número negativo, mostrar a mensagem que a
idade é inválida
"""


idade = int(input('Digite a idade: ')) # idade = -25

if (idade >= 0) and (idade <= 12):
  print("A pessoa é uma criança")
elif (idade > 12) and (idade < 18):
  print("A pessoa é uma adolescente, idade = %i" %idade)
elif (idade >= 18):
  print("A pessoa é um adulto, idade = %i" %idade)
else:
  print('Idade inválida, por favor digite um valor maior que 0')

print("Fim do programa")

