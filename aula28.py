numero = input('Digite um número para ser dobrado: ')

try:
    print(numero)
    numero_fl = float(numero)
    print(f'Seu número escolhido é {numero_fl} e ele dobrado é {numero_fl * 2}')

except:
    print('Você não digitou um número válido.')