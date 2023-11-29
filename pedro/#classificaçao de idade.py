#classificaçao de idade 
#peça para digitar a idade
idade = int(input('digite a idade:'))
#classificar a idade para adulto,criança e adolecente

if idade >= 18:
    print("Você é um adulto.")
elif idade <=10:
    print("Você é uma criança.")
    
else:
    print("Você é um adolescente.")
    
        