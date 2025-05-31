salario= float(input('Digite seu sálario e saiba o quanto deve pagar de imposto: '))

imposto_a_pagar = 0
if salario <= 2112.00:
    print(f"Seu salario de {salario} não precisa pagar imposto")
elif salario <= 2826.65:
    imposto_a_pagar= salario * (7.5/100)- 158.40
    print(f'Seu imposto a pagar é {imposto_a_pagar:2f}')
elif salario <= 3751.05:
    imposto1= salario * (15/100)- 370.40
    print(f'Seu imposto a pagar é R$ {imposto_a_pagar:2f}')
elif salario <= 4664.68:
    imposto_a_pagar= salario * (22.5/100)- 651.73
    print(f'Seu imposto a pagar é {imposto_a_pagar:2f}')
elif salario >= 4664.68:
    imposto_a_pagar= salario * (27.5/100)- 884.96
    print(f'Seu imposto a pagar é {imposto_a_pagar:2f}')
else:
    print("invalido")