# Adivinhar Número Pense em um número e faça com que o usuário adivinhe até acertar
n1 = 7

aux = 0

while aux ==0:
    numerousuario = int(input('chute um numero de 1 a 10:'))

    if(numerousuario == n1):
        print('voce acertou')
        aux = 1

    elif numerousuario < n1:
         print(' o seu chute foi menor que o numero secreto, tente novamente')
    elif  numerousuario > n1:
         print('o seu chute foi maior que o numero secreto tente novamente')