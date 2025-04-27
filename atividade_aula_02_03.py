peso= float(input("Digite seu peso atualmente: "))
altura= float(input("Agora sua altura: "))

calculo= (peso/altura**2)
print(f"Sei IMC é {calculo:.2f}")
if calculo <= 18.5:
    print("Abaixo do peso")
elif calculo <= 24.9:
    print("peso normal")
elif calculo <= 29.9:
    print ("sobrepeso")
elif calculo <= 34.9:
    print("obesidade grau 1") 
elif calculo <= 39.9:
    print("obesidade grau 2")
else:
    print("Obesidade grau 3")