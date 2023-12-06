#sequencia de fibonacci
#digite um nuemro
n = int(input('digite um numero'))
ultimo = 1
penultimo = 1
termo=0

print(1)
print(1)  
contador = 3

while contador <= n:
  termo = ultimo + penultimo
  penultimo = ultimo
  ultimo = termo
  contador +=1
  print(termo)