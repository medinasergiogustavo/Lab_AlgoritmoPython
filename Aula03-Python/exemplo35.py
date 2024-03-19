nota1 = float(input("Informe a primeira nota = ")) # 6
nota2 = float(input("Informe a segunda nota =  ")) # 5

media = (nota1 + nota2) / 2.0 # media = 5.5

#print(type(media))
#print("A media do aluno é = ", media)

if (media >=7) and (media <= 10):
    print("Bloco verdadeiro")
    print("A media final do aluno  =  % .2f" %media)
    print("Parabens, vc foi aprovado")
else:
    print("Bloco falso")
    print("A media final do aluno  =  % .2f" %media)
    print("Vc precisa realizar o exame")

print("Fim do programa")

