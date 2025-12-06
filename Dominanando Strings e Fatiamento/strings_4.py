# strings Triplas.
nome = "William"
esposa = "Zenilda"
filho = "Lucas"

texto = f'''Olá, meu nome é {nome},
Sou de São Paulo, mas vivo em Muzambinho com minha esposa {esposa}.
           Temos um filho chamado {filho}'''
print(texto)

menu = f'''***** Menu Princial **********
*    Nome: {nome}           *
*                            *
*    1 - Sacar               *
*    2 - Depositar           *
*    3 - Sair                *
*                            *
******************************
Escolha uma opção:  '''
opcao = int(input(menu))
print('*' * 30)
print(f'''Você escolheu a opção: {opcao}''')
print('*' * 30)