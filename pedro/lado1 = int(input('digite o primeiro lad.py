lado1 = int(input('digite o primeiro lado:')) 
lado2 = int(input('digite o segundo lado:'))
lado3 = int(input('digite o terceiro lado:'))
#classificar se é equilatéro,isósceles ou escaleno
if lado1 == lado2 & lado1 == lado3:
    print('e um equilatéro')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
     print(' e um isocéles')
else:
    print('e um escaleno')