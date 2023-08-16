frase_crua = 'olha só que maneiro, olha só que legal'
frase = frase_crua.split(',')
backup = []

#print(frase)
for i, frase_crua in enumerate(frase):
    backup.append(frase_crua[i].strip())

print(frase)
print(frase_crua)
print(backup)