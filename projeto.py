"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

invertido = (nome [::-1])
espacos = (' ' in nome)
letras = (len(nome))
letraum = (nome [0])
ultimaletra = (nome [-1:])


if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Sua idade é: {idade}')
    print(f'Seu nome invertido é: {invertido}')
    print(f'Seu nome possui espaços? {espacos}')
    print(f'Seu nome possui {letras} letras')
    print(f'Sua primeira letra é: {letraum}')
    print(f'Sua última letra é: {ultimaletra}')

else:
    print('Desculpe, você deixou campos vazios.')