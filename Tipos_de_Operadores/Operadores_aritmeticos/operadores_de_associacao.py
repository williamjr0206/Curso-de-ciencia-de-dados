frutas = ['LIMÃO','UVA']
frase = 'Curso de Python'

fruta = str(input('Digite o nome de uma fruta: ')).strip().upper()
palavra = str(input('Digite uma palavra: ')).strip()

print(f'{fruta} está em frutas: {frutas} ?  {fruta in frutas}')
print(f'A palavra "{palavra}" está na frase "{frase}" ? {palavra in frase}')
