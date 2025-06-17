nota= float(input("Digite sua nota: "))
if nota <50:
    print("Reprovado")
elif nota > 50 and nota <= 69:
    print("Recuperação")
elif nota > 70 and nota <= 89:
    print("Aprovado")
elif nota >= 90:
    print("Aprovado com excelência")
else:
    print("erro")