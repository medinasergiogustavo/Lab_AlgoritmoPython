
def saudacao1(meu_nome): # Função saudacao1
    print('Olá',meu_nome)

def saudacao2(meu_nome,idade): # Função saudacao2
    print('Olá',meu_nome,'\nSua idade é:',idade)
    print("Seu nome é =", meu_nome) #meu_nome é variavel local
    print(type(meu_nome))
    print("Sua idade é = ", idade) #meu_nome é variavel local
    print( type(idade))

nome = input("Digite o seu nome = ")

idade_digitada = 10 # variavel GLOBAL
print(idade_digitada)

saudacao1(nome) # invocar a função = chama a função saudacao1 ()
saudacao2("Henrique Gustavo", 10) # chama a função saudacao2 ()

print(type(nome))
print(type(idade_digitada))

"""

def func_soma(n1,n2):  # n1=5 e  n2=8
    resultado = n1+n2   # 13 = 5+8
    return resultado    # 13
    print(n1)
    print(n2)

print("Resultado da função soma = ". func_soma(5,8))
#func_soma(2,5,7)

"""