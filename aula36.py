contador = 0

while contador <= 100:
    contador   += 1

    if contador ==6 :
        print('aa')
        continue 
    if contador >= 10 and contador <= 27:
        print('não vou mostarr', contador)
        continue

    print(contador)
    if  contador == 40:
        break