idade= int(input("Digite sua idade: "))

if idade < 14:
    print("Não pode entrar.")
elif idade <18:
    print("Pode entrar com acompanhamento dos pais, e sem beber.")
else:
    print("Pode entar e beber.")