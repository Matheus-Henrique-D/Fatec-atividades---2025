lab= 2
semes= 3
final= 5

nota_lab= float(input("Digite as notas: "))
nota_avaliacao_semestral= float(input("Digite as nota: "))
nota_final= float(input("Digite as nota: "))

media= (nota_lab * lab + nota_avaliacao_semestral * semes + nota_final * final) / 10

if media <= 4.9:
    print('E')
elif media <= 5.9:
    print('D')
elif media <= 6.9:
    print('C')
elif media <= 7.9:
    print('B')
elif media <= 10:
    print('A')
else: 
    print("0")
