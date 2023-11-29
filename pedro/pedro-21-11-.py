#receber o peso  e a altura do usuario
peso = int(input('digite o peso do usuario'))
altura = float (input('digite a altura do usuario'))

#realizar o calculo do indice de massa corporal
#armazenar o resultado
imc = peso/(altura * altura)

#mostrar o resultado 
print(' o indice de massa corporalé:' ,imc)