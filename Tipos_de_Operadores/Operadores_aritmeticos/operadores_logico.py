print('Para ser verdadeiro ambos os os operadores de comparação devem ser verdadeiros: "and"')
print(f'10 > 5 and 5 < 10: {10 > 5 and 5 < 10}') # True

print('Para ser verdadeiro apenas um dos operadores de comparação deve ser verdadeiro: "or"')
print(f'10 > 5 or 5 > 10: {10 > 5 or 5 > 10}') # True

saldo = 500
saque = 200
limite = 250

print(f'\nSaldo: R$ {saldo:.2f}')
print(f'Saque: R$ {saque:.2f}')
print(f'Limite: R$ {limite:.2f}\n')

print('Exemplo de uso em uma condição real:')
print(f'Sado suficiente para saque: {saldo >= saque and saque <= limite}') # True
