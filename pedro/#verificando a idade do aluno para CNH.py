#verificando a idade do aluno para CNH
#escreva o nome do aluno
aluno = input('informe o nome do aluno')
n1 = int(input('infome a idade do aluno'))
#se a idade for maior que 18 informe 
if n1 >=18:
  print('o',aluno,'estar apto para dirigir')
  if n1 <= 18:
   print('o:' ,aluno , 'nao estar apto para dirigir') 