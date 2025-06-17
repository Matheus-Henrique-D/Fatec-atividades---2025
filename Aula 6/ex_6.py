idade_escoteiro= int(input("Digite sua idade: "))
if idade_escoteiro < 6:
    print("nada")
elif idade_escoteiro < 11:
    print("Lobinho")
elif idade_escoteiro < 15:
    print("Escoteiro")
elif idade_escoteiro < 18:
    print("Sênior")
elif idade_escoteiro < 21:
    print("Pioneiro")
elif idade_escoteiro > 21:
    print("Líder")