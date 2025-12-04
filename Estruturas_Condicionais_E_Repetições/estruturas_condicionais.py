MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Digite sua idade em anos: '))

if idade >= MAIOR_IDADE:
    print('Usuário é de maior idade.  Já pode tirar a CNH !')
if idade < MAIOR_IDADE:
    print('Usuário não é maior idade.  Não pode tirar a CNH !')


if idade >= MAIOR_IDADE:
    print('Usuário é de maior idade.  Já pode tirar a CNH !')
else:
    print('Usuário não é de maior idade.  Não pode tirar a CNH !')

if idade >= MAIOR_IDADE:
    print('Usuário é maior idade.  Já pode tirar a CNH !')
elif IDADE_ESPECIAL <= idade < MAIOR_IDADE:
    print('Usuário tem idade especial.  Pode realizar aulas teóricas, mas não pode realizar aulas práticas !')
else:
    print('Usuário não é maior idade.  Não pode tirar a CNH !')  
