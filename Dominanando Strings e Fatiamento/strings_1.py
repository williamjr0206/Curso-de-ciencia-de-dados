nome = "wiLliAm"

print(nome.lower()) # Converte para minusculo
print(nome.upper()) # Converte para maíusculo
print(nome.title()) # Converte para formato de título

texto = "  Olá Mundo    "

print(texto, '.') # Mantém os espaços
print(texto.strip(), '.') # Remove os espaços do início e do fim
print(texto.rstrip(), '.') # Remove os espaços do fim (a direita)
print(texto.lstrip(), '.') # Remove os espços do início (a esquerda)

menu = " Python "

print('***',menu,'***')
print(menu.center(16, '*')) # Centraliza o texto em um campo de 20 caracteres, preenchendo com '*'
print('*'.join(menu)) # Adiciona '*' entre cada caractere da string

