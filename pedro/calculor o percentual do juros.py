#solicitar ao usuario um valor principal e o nuemro de anos
#valor = int(input('informe o valor da taxa de juros em porcentagem'))

#realizar o calculo do montante
#arnmazenar o calculo
principal = int(input('informe o montante principal'))
taxa = int(input('informe a taxa'))
anos = int(input('infomre o numero de anos '))
montante = principal+(principal * taxa * anos/100)

#mostrar o montante final 
print('o valor do montante final e:' ,montante)