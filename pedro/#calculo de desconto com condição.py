#calculo de desconto com condição
#peça ao usuario pra digitar o valor do produto
produto = int(input('digite o valor do produto'))

if produto > 100: 
 des = int(input('digite o valor do desconto'))
 
 total = produto - produto * (des/100)
 
print('o desconto do produto:',total)


 
 
 
     
    
    
   