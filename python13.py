# CALCULANDO IMC
#IMC =
#PESO
#(ALTURA)2
nome = "Jhonata Vênancio"
altura = 1.78
peso = 78
imc= (peso/ (altura*altura))

linha_1 = f'{nome} você tem {altura} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é:'
linha_3 = f'{imc:.3f}'

print(linha_1)
print(linha_2)
print(linha_3)