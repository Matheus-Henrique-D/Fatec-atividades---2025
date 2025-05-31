aluno = 1

while aluno <= 6:
    print(f"\nAluno {aluno}") #O \n é um atalho do Python para pular uma linha no terminal.
    nota1= float(input("Digite a primeira nota:"))
    nota2= float(input("Digite a segunda nota:"))


    media = (nota1 + nota2) / 2

    if media <= 3:
        print('reprovado')
    elif media <= 7:
        print('exame')
    elif media > 7:
        print('aprovado')
    else:
        print('não encontrado')

    aluno += 1