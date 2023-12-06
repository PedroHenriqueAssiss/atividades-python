# Números Primos 
numero = int(input('digite o numero'))
x = 1
aux = 0
while x <=numero:
    if numero % x == 0:
       aux += 1
    x = x+1

if aux == 2:
    print('o numero é um numero primo')

else:
    print('o numero nao e um numero primo')