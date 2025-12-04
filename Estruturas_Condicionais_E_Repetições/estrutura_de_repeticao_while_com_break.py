opcao = -1
nome = str(input('Digite seu nome: ')).strip().title()

while True:
    opcao = int(input('''Escolha uma opção:
                      1 - Dizer olá !
                      2 - Dizer Tchau !
                      0 - Sair
                      '''))
    if opcao == 1:
        print(f'Olá, {nome} !')
    elif opcao == 2:
        print(f'Tchau, {nome} !')
    elif opcao == 0:
        break
print(f'Obrigado {nome} pela brincadeira, até mais !')