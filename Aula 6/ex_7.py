numero= int(input("Digite o número: "))

def calcular_fatorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

resultado = calcular_fatorial(numero)
print("O fatorial de", numero, "é", resultado)