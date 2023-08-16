#nome = 'Venâncio'
#print([4])
#print('Jhonata' in nome)
#print(10*'-')
#print('Jhonata'not in nome)

nome = input ('Digite seu nome e sobrenome: ')
encontrar = input('O que você deseja encontrar? ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else: 
    print(f'{encontrar} Não está em {nome}')
