a = 'aaa'
b= 'BBBB'
c= 1.5

string = "a={nome1} b={nome2} c={nome3:.4f}"
formato = string.format(nome1=a,nome2=b,nome3=c)

print(formato)