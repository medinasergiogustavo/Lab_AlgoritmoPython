"""
Exercício 2 (Com a estrutura for)
Imprimir a tabuada do número 3 (3 x 0 = 0........ 3 x 10 = 30)
"""

for i in range(0, 11):
  print('3 x {} = {}'.format(i, 3 * i))

print("--------------")

"""
Exercício 2 (Com a estrutura while)
Imprimir a tabuada do número 3 (3 x 0 = 0........ 3 x 10 = 30)
"""

numero = 0
while numero <= 10:
  print('3 x {} = {}'.format(numero, 3 * numero))
  numero += 1