#numeros divisível por 3 e 5
#peça ao usuario pra digitar um numero
n1 = int(input('digite um numero'))
#determinar se o numero e divisível por 3  e 5
if n1 % 3 == 0  and  n1 % 5 == 0:

    print(' e divisel por 3 e 5')
else:
    print('nao e divisivel')