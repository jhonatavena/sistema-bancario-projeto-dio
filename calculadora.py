while True:
    print('Bem vindo a calculadora')
    numero1 = input('Digite um numero: ')
    operador = input('qual seria o operador do calculo? LEMBRANDO : (+, -, *, /)')
    numero2 = input('Digite o segundo número: ')
  
    #Checar
    if numero1.isdigit():
        numero1_int = int(numero1)
    if numero2.isdigit():
        numero2_int = int(numero2)
    else:
        print('Erro!!!! DIGITE UM NUMERO VALIDO')
#SOMA
    if operador == "+":
        soma1 = (numero1_int + numero2_int)
        print(f'A soma de {numero1_int} e {numero2_int} é igual a {soma1}')
        
    if operador == "-":
        soma2 = (numero1_int - numero2_int)
        print(f'A subtração de {numero1_int} e {numero2_int} é igual a {soma2}')

    if operador == "*":
        soma3 = (numero1_int * numero2_int)
        print(f'A multiplicação de {numero1_int} e {numero2_int} é igual a {soma3}')

    if operador == "/":
        soma4 = (numero1_int / numero2_int)
        print(f'A divisão de {numero1_int} e {numero2_int} é igual a {soma4}')
    if operador != "+" and operador != "-" and operador != "*" and operador != "/":
        print('Erro!! Digite um operador válido na próxima')

    sair = input('Digite sim para sair:').lower().starts
    if sair == "sim":
        print('você saiu')
        break
    else:
        continue

