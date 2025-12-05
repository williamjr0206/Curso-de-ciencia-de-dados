nome = "William"
idade = 59
profissao = "Engenheiro"
linguagem = "Python"
pessoa = {'nome' : "William", 'idade' : 59}

print('Meu nome é %s, tenho %d anos, trabalho como %s e estou estudando %s.' % (nome, idade, profissao, linguagem))
# O comando acima utiliza a formatação antiga de strings com o operador %.

print('Meu nome é {}, tenho {} anos, trabalho como {} e estou estudando {}.'.format(nome, idade, profissao, linguagem))
print('Meu nome é {0}, tenho {1}.'.format(nome, idade))
# O comando acima utiliza o método format() para formatar a string.

print('Meu nome é {nome} e tenho {idade} anos.'.format(**pessoa))
# O comando acima utiliza o método format() com dicionário para formatar a string.
print(f'Meu nome é {nome}, tenho {idade} anos, trabaho como {profissao} e estou estudando {linguagem}')
# O comando acima utiliza f- strings para formatar o string.

PI = 3.14159
print(f'O valor de PI é aproximadamente {PI:.2f}.')
# O comando acima utiliza f- strings para formatar o valor de PI com duas casas decimais.
print(f'O valor de PI é aproximadamente {PI:10.2f}.')
# O comando acima utiliza o método format() para formatar o valor de PI com duas casas decimais e largura mínima de 10 caracteres.
