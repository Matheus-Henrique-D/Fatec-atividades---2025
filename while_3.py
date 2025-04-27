numero_correto= 0
soma_erros= 0
tentativa= int(input("Adivinhe o número certo para terminar: "))

while tentativa != numero_correto:
    soma_erros += tentativa
    print("tente denovo")
    tentativa= int(input("Adivinhe o número certo para terminar: "))

print("Acertou")
print(f"quantidade somada de erros é: {soma_erros}")