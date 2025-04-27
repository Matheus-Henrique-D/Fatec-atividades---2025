idade= int(input("Digite sua idade: "))
salario= int(input("Agora seu salário mensal: "))

if idade >= 18 and salario <= 2000:
    print("Você tem direito")
elif idade > 59: 
    print("Tem direito")
else:
    print("Você não tem direito")