total_homens = 0
total_mulheres = 0
soma_homens = 0
soma_mulheres = 0

for aluno in range(5):  
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M/F ou Homem/Mulher): ").strip().lower()

    if sexo in ["m", "masculino", "homem"]:
        total_homens += 1
        soma_homens += idade
    elif sexo in ["f", "feminino", "mulher"]:
        total_mulheres += 1
        soma_mulheres += idade
    else:
        print("Sexo inválido!")

# Cálculo das médias
if total_homens > 0:
    media_homens = soma_homens / total_homens
else:
    media_homens = 0

if total_mulheres > 0:
    media_mulheres = soma_mulheres / total_mulheres
else:
    media_mulheres = 0

print("Total de homens:", total_homens)
print("Média de idade dos homens:", media_homens)
print("Total de mulheres:", total_mulheres)
print("Média de idade das mulheres:", media_mulheres)
