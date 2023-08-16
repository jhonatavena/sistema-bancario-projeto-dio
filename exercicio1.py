'''LISTA DE COMPRAS'''
import os
lista = []
validacao = len(lista)

while True:
    
    entrada = input('Selecione uma das opções abaixo \n[i]nserir [a]pagar [l]istar [s]air: ')
    if entrada == 'i':
        adicionar = input('O que deseja adicionar na lista?: ')

        lista.append(adicionar)

    if entrada == 'a':
            
        try:
            os.system('cls')   
            for nome, indice in enumerate(lista):
             print(f'[{nome}], {indice}')

            apagar = int(input('Qual item você deseja apagar?'))
            
            del lista[apagar]

        except ValueError:
            print('Indice Invalido! tente novamente')

            ...
    if entrada == 'l':
            os.system('cls')
            for nome, indice in enumerate(lista):
             print(nome, indice)
            

            if validacao == 0:
                print('Sua lista está vazia!')

    if entrada == 's':
        break

    


