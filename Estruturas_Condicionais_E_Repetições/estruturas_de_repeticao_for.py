texto = str(input('Digite um texto: ')).strip().upper()
VOGAIS = 'AEIOU'

# exemplo com string (in)

for letra in texto:
    if letra in VOGAIS:
        print(letra, end=' ')
        print('->', end=' ')
else:
    print('FIM !')


# exemplo com range()

    for numero in range(0, 51, 5):
        print(numero, end=' ')
        print('->', end=' ')
    else:
        print('FIM !')


# exemplo com break e continue
for numero in range(8000):
    if numero  == 101:
        break

    if numero % 2 == 0:
        continue
    else:
        print(numero, end=' ')
    
print('FIM !')

