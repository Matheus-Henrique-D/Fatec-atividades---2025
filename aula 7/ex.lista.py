lista1=[10,11,12,13,14]
lista2=[6,7,8,9,10,11]


lista3=[]
for item in lista1:
    if not item in lista3:
        lista3.append(item)

for item in lista2:
    if not item in lista3:
        lista3.append(item)

print(lista3)

# Modo fácil de fazer o exercicio

lista1=[10,11,12,13,14]
lista2=[6,7,8,9,10,11]
lista3= list(set(lista1+lista2))

print(lista3)