'''''
i= 1

while i < 20:
    print(i)
    i += 1

print("terminou")
print(i)

'''
#da para usar if,  a função break quebra o loop
senha= 1564
tentativa=int(input("Digite a senha: "))

while tentativa != senha:
    print("Senha errada. Tente novamente")
    tentativa=int(input("Digite a senha: "))

print("Acesso liberado")