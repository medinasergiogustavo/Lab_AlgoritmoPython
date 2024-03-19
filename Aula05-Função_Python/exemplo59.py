print("Exempos da função Default")
def funcao_default(param1=1000):
    print("Resultado da 1ra função default = ", param1)

print(funcao_default()) # # Chamada da função default funcao_default()
print()

print("2da função default")
def login(sistema="Ubuntu", usuario="root", senha="123"):
    print("Valor da variavel Sistema =  ", sistema)
    print("Valor da variavel Usuário =  ", usuario)
    print("Valor da variavel da Senha = ", senha)

login() # Chamada da função default login()

print()
def dados_pessoais(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}".format(nome, sobrenome, idade, sexo))

dados_pessoais(nome="Henrique", sobrenome="Gustavo", idade=20, sexo="Masculino")

