#peça pra o usuario digitar uma letra
ltr = input('digite uma letra')
#determina se a letra e vogal ou consoante
if ltr == 'a'  or ltr == 'e' or ltr == 'i' or ltr == 'o' and ltr == 'u':
  print('e uma vogal') 
else:
    print('e uma consoante')