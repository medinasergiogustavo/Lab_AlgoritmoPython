def func():
    global num # variável local na função
    print("Resultado da variavel local num = ", num)

print("Exemplo de variavel local e global com funções")
num = 10 # variável global


func() # chama a função 
print("Resultado da variavel global num = ", num)

print("Caso seja necessario utilize o comando global")