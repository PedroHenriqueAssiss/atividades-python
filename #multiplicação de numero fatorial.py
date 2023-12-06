#multiplicação de numero fatorial
numero = int(input('digite o numero'))
x = numero - 1
resultado = numero
while x >=1:
   resultado  = resultado * x
   x = x - 1
print(' o resultado do fatorial e:',resultado)