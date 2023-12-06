#media de notas com condições
#digite uma nota

contador = 0
n = 0
soma = 0

while  n >= 0:
  n = int(input('digite a nota:'))


  if n>=  0:
 
    soma += n 
    
    contador = contador + 1
  else:
    print('nenhuma das notas e validas')

media = soma / contador 
print('a media das notas e:',media)