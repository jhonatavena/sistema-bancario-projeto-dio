entrada = input('Você deseja [E]ntrar ou [S]air ')
senhadigitada = input('Digite sua senha: ')

bancodesenha = 'venaldo'
if entrada == 'E'and (senhadigitada == bancodesenha):
    print('Você entrou no sistema!')

elif entrada == 'S':
    print('Você errou a senha, tente novamente meu nobre')

else: 
    print('Você saiu do sistema!')