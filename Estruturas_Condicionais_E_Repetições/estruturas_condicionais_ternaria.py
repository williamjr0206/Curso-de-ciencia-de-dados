saldo = 1500
saque = float(input('Digite o valor do saque em R$: '))

status = "Sucesso !" if saldo >= saque else "Falha !"
print(f'{status} ao realizar o saque.')