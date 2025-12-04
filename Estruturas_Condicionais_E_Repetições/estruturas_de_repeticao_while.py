opcao = -1
while opcao != 0:
    opcao = int(input('''Escolha uma opção:
                      1 - Dizer olá !
                      2 - Dizer tchau !
                      0 - Sair
                      '''))
    if opcao == 1:
        print('Olá !')
    elif opcao == 2:
        print('Tchau !')
else:
    print('Obrigado pela brincadeira, até mais !')