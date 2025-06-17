''''
#exercício 1:
for x in range(1,10):
    print(x)


#exercício 2 "(1,10,2) o 1 é o inicio, o 10 é o fim, e o 2 é divisor":
for i in range(5,51,5):
    print(i)


'''
#exercício 3:
numero= int(input("digite um número inteiro: "))
soma= 0

for i in range(1,numero + 1):
    if i % 2 ==0:
        soma += i
    
print(soma)
