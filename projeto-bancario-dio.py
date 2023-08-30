import os
saldo = 1000
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUE = 2

while True:
    menu = input('Bem vindo ao VenaBank! \n\nDigite a opção desejada:\n[D]epôsito [S]aque [E]xtrato [Q]uit: ')
    
    if menu == 'D' or menu == 'd':
        os.system('cls')
        deposito = int(input('DEPOSITO\nDigite o valor que deseja depositar: '))
        if deposito >= 0:
            
            saldo += deposito
            extrato.append(f'Deposito realizado de +R${deposito}')
            print(f'Operação realizada com sucesso!\n')
        
        else:
            print('Operação Invalida!\n\nTente novamente, por gentileza!\n')

    elif menu == 'S' or menu == 's':
        os.system('cls')
        saque = int(input('SAQUE\nDigite o valor que deseja sacar: '))

        if saque <= limite and saque >= 0:
            if saque <= saldo and saque >= 0:
                if numero_saques <= LIMITE_SAQUE:
                    numero_saques += 1
                    saldo -= saque
                    extrato.append(f'Saque realizado de -R${saque}') 
                    print(f'Operação realizada com sucesso!')
                else:
                    print('Você atingiu o limite de saques diário!\n')
            else:
                print('Saldo na conta insuficiente!')        
        else:
            print('Operação invalida!\nLimite de R$500 por dia atingido\nTente novamente por gentileza!\n')

    elif menu == 'E' or menu == 'e':
        os.system('cls')
        if len(extrato) >=1:
            print(f'SALDO ATUAL: R${saldo}\n\nHISTORICO DE TRANSAÇÕES:')
            for transacoes in extrato:
                print(transacoes)

        else:
            print(f'Seu saldo atual é R${saldo}\n\nNão Houve transações.\n')


    elif menu == 'Q' or menu == 'q':
        break
    else:
        print('Operação invalida! \n Selecione novamente a opção desejada.\n')