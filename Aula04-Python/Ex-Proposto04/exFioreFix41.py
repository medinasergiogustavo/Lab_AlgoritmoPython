
validar = False
repetir = 's'

while repetir == 's':

    while (validar == False):
        print("Digite um numero maior que 0 e menor que 10: ")
        num = input()
        try:
            num = int(num)
            if num <= 0 or num >= 10:
                print('valor inválido, numero deve ser maior que 0 e menor que 10')
            else:
                validar = True
        except:
            print('numero inválido, digite apenas números maiores que 0 e menores que 10')

    if num == 1 or num == 2:
        print('O numero elevado ao cubo é: ' + str(num*num))
    elif num == 3 or num == 6 or num == 9:
        i = int(1)
        fatora = 1
        while i <= num:
            fatora *= num
            num -= 1
            print("fatorando..." + str(num))
        print("O numero digitado fatorado é igual a: " + str(fatora))
    else:
        numeroDigitado = num
        num = num / 9
        print("O numero digitado ", str(numeroDigitado),
              " divido por 9 é igual a: " + str(num))

    sair = True

    while sair == True:
        print('')
        opcao = input('Deseja continuar [S/N]: ').lower()
        if opcao == 's' or opcao == 'n':
            if opcao == "s":
                repetir = 's'
                validar = False
                print('')
                break
            else:
                opcao = 'n'
                repetir = 'n'
                sair = False

        else:
            print('opcao invalida!, tente novamente...')
            sair = True
